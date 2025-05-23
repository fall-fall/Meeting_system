from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.crud import friendship as friendship_crud
from app.crud import user as user_crud
from app.crud import notification as notification_crud
from app.database import get_db, User, FriendshipStatus, NotificationType
from app.dependencies import get_current_active_user

router = APIRouter(prefix="/friends", tags=["friends"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def list_friends(
    request: Request,
    db: Session = Depends(get_db),
):
    """显示好友列表页面。"""
    # 获取当前用户
    current_user = None
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        try:
            from app.dependencies import get_current_user
            current_user = await get_current_user(token.replace("Bearer ", ""), db)
        except:
            # 未登录，重定向到登录页面
            return RedirectResponse(url="/api/auth/login")
    else:
        # 未登录，重定向到登录页面
        return RedirectResponse(url="/api/auth/login")

    # 获取好友列表
    friends = friendship_crud.get_friends(db, user_id=current_user.id)

    # 获取待处理的好友请求
    pending_requests = friendship_crud.get_pending_friend_requests(db, user_id=current_user.id)

    # 获取所有用户（用于添加好友）
    all_users = user_crud.get_users(db)

    # 过滤掉已经是好友的用户和自己
    friend_ids = [friend.id for friend in friends]
    pending_friend_ids = [req.user_id for req in pending_requests]
    available_users = [user for user in all_users if user.id != current_user.id and user.id not in friend_ids and user.id not in pending_friend_ids]

    # 获取未读通知数量
    unread_notification_count = notification_crud.get_unread_notification_count(db, current_user.id)

    return templates.TemplateResponse(
        "user/friends.html",
        {
            "request": request,
            "current_user": current_user,
            "friends": friends,
            "pending_requests": pending_requests,
            "available_users": available_users,
            "unread_notification_count": unread_notification_count,
        },
    )


@router.post("/add", response_class=HTMLResponse)
async def add_friend(
    request: Request,
    friend_id: int = Form(...),
    db: Session = Depends(get_db),
):
    """发送好友请求。"""
    # 获取当前用户
    current_user = None
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        try:
            from app.dependencies import get_current_user
            current_user = await get_current_user(token.replace("Bearer ", ""), db)
        except:
            # 未登录，重定向到登录页面
            return RedirectResponse(url="/api/auth/login")
    else:
        # 未登录，重定向到登录页面
        return RedirectResponse(url="/api/auth/login")

    # 检查好友是否存在
    friend = user_crud.get_user(db, user_id=friend_id)
    if not friend:
        raise HTTPException(status_code=404, detail="用户不存在")

    # 检查是否已经是好友
    existing_friendship = friendship_crud.get_friendship_by_users(db, current_user.id, friend_id)
    if existing_friendship:
        if existing_friendship.status == FriendshipStatus.ACCEPTED:
            raise HTTPException(status_code=400, detail="已经是好友")
        elif existing_friendship.status == FriendshipStatus.PENDING:
            raise HTTPException(status_code=400, detail="好友请求已发送，等待对方接受")

    # 创建好友关系
    friendship = friendship_crud.create_friendship(db, current_user.id, friend_id)

    # 创建通知
    notification_crud.create_notification(
        db,
        user_id=friend_id,
        type=NotificationType.FRIEND_REQUEST,
        content=f"{current_user.username} 向您发送了好友请求",
        sender_id=current_user.id,
        related_id=friendship.id
    )

    # 重定向到好友列表页面
    return RedirectResponse(url="/api/friends/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/accept/{friendship_id}", response_class=HTMLResponse)
async def accept_friend_request(
    request: Request,
    friendship_id: int,
    db: Session = Depends(get_db),
):
    """接受好友请求。"""
    # 获取当前用户
    current_user = None
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        try:
            from app.dependencies import get_current_user
            current_user = await get_current_user(token.replace("Bearer ", ""), db)
        except:
            # 未登录，重定向到登录页面
            return RedirectResponse(url="/api/auth/login")
    else:
        # 未登录，重定向到登录页面
        return RedirectResponse(url="/api/auth/login")

    # 获取好友关系
    friendship = friendship_crud.get_friendship(db, friendship_id=friendship_id)
    if not friendship:
        raise HTTPException(status_code=404, detail="好友请求不存在")

    # 检查是否是请求的接收者
    if friendship.friend_id != current_user.id:
        raise HTTPException(status_code=403, detail="无权接受此好友请求")

    # 更新好友关系状态
    friendship = friendship_crud.update_friendship_status(db, friendship_id, FriendshipStatus.ACCEPTED)

    # 创建通知
    notification_crud.create_notification(
        db,
        user_id=friendship.user_id,
        type=NotificationType.FRIEND_ACCEPTED,
        content=f"{current_user.username} 接受了您的好友请求",
        sender_id=current_user.id,
        related_id=friendship.id
    )

    # 重定向到好友列表页面
    return RedirectResponse(url="/api/friends/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/reject/{friendship_id}", response_class=HTMLResponse)
async def reject_friend_request(
    request: Request,
    friendship_id: int,
    db: Session = Depends(get_db),
):
    """拒绝好友请求。"""
    # 获取当前用户
    current_user = None
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        try:
            from app.dependencies import get_current_user
            current_user = await get_current_user(token.replace("Bearer ", ""), db)
        except:
            # 未登录，重定向到登录页面
            return RedirectResponse(url="/api/auth/login")
    else:
        # 未登录，重定向到登录页面
        return RedirectResponse(url="/api/auth/login")

    # 获取好友关系
    friendship = friendship_crud.get_friendship(db, friendship_id=friendship_id)
    if not friendship:
        raise HTTPException(status_code=404, detail="好友请求不存在")

    # 检查是否是请求的接收者
    if friendship.friend_id != current_user.id:
        raise HTTPException(status_code=403, detail="无权拒绝此好友请求")

    # 更新好友关系状态
    friendship = friendship_crud.update_friendship_status(db, friendship_id, FriendshipStatus.REJECTED)

    # 重定向到好友列表页面
    return RedirectResponse(url="/api/friends/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/delete/{friend_id}", response_class=HTMLResponse)
async def delete_friend(
    request: Request,
    friend_id: int,
    db: Session = Depends(get_db),
):
    """删除好友。"""
    # 获取当前用户
    current_user = None
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        try:
            from app.dependencies import get_current_user
            current_user = await get_current_user(token.replace("Bearer ", ""), db)
        except:
            # 未登录，重定向到登录页面
            return RedirectResponse(url="/api/auth/login")
    else:
        # 未登录，重定向到登录页面
        return RedirectResponse(url="/api/auth/login")

    # 获取好友关系
    friendship = friendship_crud.get_friendship_by_users(db, current_user.id, friend_id)
    if not friendship:
        raise HTTPException(status_code=404, detail="好友关系不存在")

    # 删除好友关系
    friendship_crud.delete_friendship(db, friendship.id)

    # 重定向到好友列表页面
    return RedirectResponse(url="/api/friends/", status_code=status.HTTP_303_SEE_OTHER)
