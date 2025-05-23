from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.crud import registration as registration_crud
from app.crud import conference as conference_crud
from app.crud import friendship as friendship_crud
from app.crud import notification as notification_crud
from app.crud import user as user_crud
from app.database import get_db, User, NotificationType, FriendshipStatus
from app.dependencies import get_current_active_user
from app.models.registration import RegistrationCreate

router = APIRouter(prefix="/registrations", tags=["registrations"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def my_registrations(
    request: Request,
    db: Session = Depends(get_db),
):
    """List registrations for the current user."""
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

    registrations = registration_crud.get_registrations_by_user(db, user_id=current_user.id)
    return templates.TemplateResponse(
        "user/registrations.html",
        {"request": request, "registrations": registrations, "current_user": current_user},
    )


@router.get("/register/{conference_id}", response_class=HTMLResponse)
async def register_for_conference(
    conference_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Register for a conference."""
    # Check if conference exists
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if already registered
    existing_registration = registration_crud.get_registration_by_user_and_conference(
        db, user_id=current_user.id, conference_id=conference_id
    )
    if existing_registration:
        raise HTTPException(status_code=400, detail="您已经注册了此会议")

    # Create registration
    registration = RegistrationCreate(conference_id=conference_id)
    registration_crud.create_registration(db=db, registration=registration, user_id=current_user.id)

    # Redirect to conference detail
    return RedirectResponse(url=f"/api/conferences/{conference_id}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/unregister/{conference_id}", response_class=HTMLResponse)
async def unregister_from_conference(
    conference_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Unregister from a conference."""
    # Check if conference exists
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if registered
    registration = registration_crud.get_registration_by_user_and_conference(
        db, user_id=current_user.id, conference_id=conference_id
    )
    if not registration:
        raise HTTPException(status_code=400, detail="您尚未注册此会议")

    # Delete registration
    registration_crud.delete_registration(db=db, registration_id=registration.id)

    # Redirect to conference detail
    return RedirectResponse(url=f"/api/conferences/{conference_id}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/attendees/{conference_id}", response_class=HTMLResponse)
async def conference_attendees(
    request: Request,
    conference_id: int,
    db: Session = Depends(get_db),
):
    """List attendees for a conference."""
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

    # Check if conference exists
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if user is the creator
    if conference.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="您无权查看此会议的参会者")

    # Get registrations
    registrations = registration_crud.get_registrations_by_conference(db, conference_id=conference_id)

    # 获取用户的好友列表（用于邀请）
    friends = friendship_crud.get_friends(db, user_id=current_user.id)

    # 如果是管理员但没有好友，添加所有非参会者用户作为可邀请对象
    if current_user.is_admin and not friends:
        all_users = user_crud.get_users(db)
        registered_user_ids = [reg.user_id for reg in registrations]
        # 排除已参会用户和当前用户
        available_friends = [user for user in all_users
                            if user.id != current_user.id and user.id not in registered_user_ids]
    else:
        # 过滤掉已经注册的好友
        registered_user_ids = [reg.user_id for reg in registrations]
        available_friends = [friend for friend in friends if friend.id not in registered_user_ids]

    return templates.TemplateResponse(
        "conferences/attendees.html",
        {
            "request": request,
            "conference": conference,
            "registrations": registrations,
            "current_user": current_user,
            "available_friends": available_friends,
        },
    )


@router.post("/invite", response_class=HTMLResponse)
async def invite_friend(
    request: Request,
    conference_id: int = Form(...),
    friend_id: int = Form(...),
    db: Session = Depends(get_db),
):
    """邀请好友参加会议。"""
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

    # 检查会议是否存在
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # 检查用户是否存在
    friend = user_crud.get_user(db, user_id=friend_id)
    if not friend:
        raise HTTPException(status_code=404, detail="用户不存在")

    # 如果不是管理员，检查是否是好友
    if not current_user.is_admin:
        friendship = friendship_crud.get_friendship_by_users(db, current_user.id, friend_id)
        if not friendship or friendship.status != FriendshipStatus.ACCEPTED:
            raise HTTPException(status_code=400, detail="该用户不是您的好友")

    # 检查好友是否已经注册参加会议
    registration = registration_crud.get_registration_by_user_and_conference(db, user_id=friend_id, conference_id=conference_id)
    if registration:
        raise HTTPException(status_code=400, detail="该好友已经参加此会议")

    # 创建通知
    notification_crud.create_notification(
        db,
        user_id=friend_id,
        type=NotificationType.MEETING_INVITATION,
        content=f"{current_user.username} 邀请您参加会议 '{conference.title}'",
        sender_id=current_user.id,
        related_id=conference_id
    )

    # 重定向回参会者页面
    return RedirectResponse(url=f"/api/registrations/attendees/{conference_id}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/accept-invitation/{conference_id}", response_class=HTMLResponse)
async def accept_invitation(
    request: Request,
    conference_id: int,
    direct_accept: bool = False,
    db: Session = Depends(get_db),
):
    """接受会议邀请。"""
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

    # 检查会议是否存在
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # 如果不是直接接受，显示确认页面
    if not direct_accept:
        return templates.TemplateResponse(
            "direct_accept.html",
            {
                "request": request,
                "current_user": current_user,
                "conference": conference,
            },
        )

    # 检查用户是否已经注册参加会议
    registration = registration_crud.get_registration_by_user_and_conference(db, user_id=current_user.id, conference_id=conference_id)
    if registration:
        # 已经注册，直接重定向到会议详情页面
        return RedirectResponse(url=f"/api/conferences/{conference_id}", status_code=status.HTTP_303_SEE_OTHER)

    # 创建注册
    registration = RegistrationCreate(conference_id=conference_id)
    registration_crud.create_registration(db, registration=registration, user_id=current_user.id)

    # 创建通知
    notification_crud.create_notification(
        db,
        user_id=current_user.id,
        type=NotificationType.MEETING_JOINED,
        content=f"您已成功加入会议 '{conference.title}'",
        related_id=conference_id
    )

    # 重定向到会议详情页面
    return RedirectResponse(url=f"/api/conferences/{conference_id}", status_code=status.HTTP_303_SEE_OTHER)
