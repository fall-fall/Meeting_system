from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.crud import notification as notification_crud
from app.crud import user as user_crud
from app.database import get_db

router = APIRouter(prefix="/notifications", tags=["notifications"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def list_notifications(
    request: Request,
    db: Session = Depends(get_db),
):
    """显示通知列表页面。"""
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

    # 获取通知列表
    notifications = notification_crud.get_notifications_by_user(db, user_id=current_user.id)

    # 加载发送者信息
    for notification in notifications:
        if notification.sender_id:
            sender = user_crud.get_user(db, user_id=notification.sender_id)
            if sender:
                notification.sender = sender

    # 获取未读通知数量
    unread_notification_count = notification_crud.get_unread_notification_count(db, current_user.id)

    # 检查是否使用测试页面
    use_test_page = request.query_params.get("test") == "1"
    template_name = "test_notifications.html" if use_test_page else "user/notifications.html"

    return templates.TemplateResponse(
        template_name,
        {
            "request": request,
            "current_user": current_user,
            "notifications": notifications,
            "unread_notification_count": unread_notification_count,
        },
    )


@router.get("/mark-read/{notification_id}", response_class=HTMLResponse)
async def mark_notification_as_read(
    request: Request,
    notification_id: int,
    db: Session = Depends(get_db),
):
    """将通知标记为已读。"""
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

    # 获取通知
    notification = notification_crud.get_notification(db, notification_id=notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="通知不存在")

    # 检查是否是通知的接收者
    if notification.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="无权标记此通知")

    # 标记为已读
    notification_crud.mark_notification_as_read(db, notification_id)

    # 重定向到通知列表页面
    return RedirectResponse(url="/api/notifications/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/mark-all-read", response_class=HTMLResponse)
async def mark_all_notifications_as_read(
    request: Request,
    db: Session = Depends(get_db),
):
    """将所有通知标记为已读。"""
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

    # 标记所有通知为已读
    notification_crud.mark_all_notifications_as_read(db, current_user.id)

    # 重定向到通知列表页面
    return RedirectResponse(url="/api/notifications/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/delete/{notification_id}", response_class=HTMLResponse)
async def delete_notification(
    request: Request,
    notification_id: int,
    db: Session = Depends(get_db),
):
    """删除通知。"""
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

    # 获取通知
    notification = notification_crud.get_notification(db, notification_id=notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="通知不存在")

    # 检查是否是通知的接收者
    if notification.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="无权删除此通知")

    # 删除通知
    notification_crud.delete_notification(db, notification_id)

    # 重定向到通知列表页面
    return RedirectResponse(url="/api/notifications/", status_code=status.HTTP_303_SEE_OTHER)
