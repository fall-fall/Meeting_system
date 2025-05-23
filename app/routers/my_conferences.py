from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.crud import conference as conference_crud
from app.crud import registration as registration_crud
from app.crud import notification as notification_crud
from app.database import get_db, User
from app.dependencies import get_current_active_user

router = APIRouter(prefix="/my-conferences", tags=["my_conferences"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def my_conferences(
    request: Request,
    db: Session = Depends(get_db),
):
    """显示用户的会议页面，包括参与的会议和创建的会议（如果是管理员）。"""
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

    # 获取用户参与的会议
    registrations = registration_crud.get_registrations_by_user(db, user_id=current_user.id)
    registered_conferences = []
    for registration in registrations:
        conference = conference_crud.get_conference(db, conference_id=registration.conference_id)
        if conference:
            registered_conferences.append(conference)

    # 如果是管理员，获取创建的会议
    created_conferences = []
    if current_user.is_admin:
        created_conferences = conference_crud.get_conferences_by_creator(db, creator_id=current_user.id)

    # 获取未读通知数量
    unread_notification_count = notification_crud.get_unread_notification_count(db, current_user.id)

    return templates.TemplateResponse(
        "user/my_conferences.html",
        {
            "request": request,
            "current_user": current_user,
            "registered_conferences": registered_conferences,
            "created_conferences": created_conferences,
            "unread_notification_count": unread_notification_count,
        },
    )
