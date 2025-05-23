"""
会议相关的路由处理模块

包含会议列表、详情、创建、编辑、删除和议程管理等功能
"""

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.crud import conference as conference_crud
from app.crud import notification as notification_crud
from app.database import get_db, User
from app.dependencies import get_current_admin_user
from app.models.conference import ConferenceCreate, ConferenceUpdate, AgendaItemCreate

# 创建路由器
router = APIRouter(prefix="/conferences", tags=["conferences"])
# 设置模板引擎
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def list_conferences(
    request: Request,  # 请求对象
    db: Session = Depends(get_db),  # 数据库会话
):
    """显示所有会议列表"""
    # 获取当前用户（如果已登录）
    current_user = None
    unread_notification_count = 0
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        try:
            from app.dependencies import get_current_user
            current_user = await get_current_user(token.replace("Bearer ", ""), db)
            # 获取未读通知数量
            if current_user:
                unread_notification_count = notification_crud.get_unread_notification_count(db, current_user.id)
        except:
            pass

    conferences = conference_crud.get_conferences(db)
    return templates.TemplateResponse(
        "conferences/list.html",
        {
            "request": request,
            "conferences": conferences,
            "current_user": current_user,
            "unread_notification_count": unread_notification_count
        },
    )


@router.get("/create", response_class=HTMLResponse)
async def create_conference_page(
    request: Request,  # 请求对象
    current_user: User = Depends(get_current_admin_user),  # 当前管理员用户
):
    """渲染创建会议页面"""
    return templates.TemplateResponse(
        "conferences/create.html",
        {"request": request, "current_user": current_user},
    )


@router.post("/create", response_class=HTMLResponse)
async def create_conference(
    request: Request,  # 请求对象
    title: str = Form(...),  # 会议标题
    description: str = Form(...),  # 会议描述
    date: str = Form(...),  # 会议日期时间
    location: str = Form(...),  # 会议地点
    db: Session = Depends(get_db),  # 数据库会话
    current_user: User = Depends(get_current_admin_user),  # 当前管理员用户
):
    """创建新会议"""
    # Parse date string to datetime
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M")
    except ValueError:
        return templates.TemplateResponse(
            "conferences/create.html",
            {
                "request": request,
                "error": "日期格式无效",
                "current_user": current_user,
                "title": title,
                "description": description,
                "date": date,
                "location": location,
            },
        )

    # Create conference
    conference = ConferenceCreate(
        title=title,
        description=description,
        date=date_obj,
        location=location,
    )
    conference_crud.create_conference(db=db, conference=conference, creator_id=current_user.id)

    # Redirect to conferences list
    return RedirectResponse(url="/conferences/admin", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/admin", response_class=HTMLResponse)
async def admin_conferences(
    request: Request,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user),
):
    """List conferences created by the current admin user."""
    conferences = conference_crud.get_conferences_by_creator(db, creator_id=current_user.id)
    return templates.TemplateResponse(
        "conferences/admin.html",
        {"request": request, "conferences": conferences, "current_user": current_user},
    )


@router.get("/{conference_id}", response_class=HTMLResponse)
async def conference_detail(
    request: Request,
    conference_id: int,
    db: Session = Depends(get_db),
):
    """Get a conference by ID."""
    # 获取当前用户（如果已登录）
    current_user = None
    unread_notification_count = 0
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        try:
            from app.dependencies import get_current_user
            current_user = await get_current_user(token.replace("Bearer ", ""), db)
            # 获取未读通知数量
            if current_user:
                unread_notification_count = notification_crud.get_unread_notification_count(db, current_user.id)
        except:
            pass

    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Get agenda items
    agenda_items = conference_crud.get_agenda_items(db, conference_id=conference_id)

    # Check if user is registered
    is_registered = False
    if current_user:
        for registration in conference.registrations:
            if registration.user_id == current_user.id:
                is_registered = True
                break

    return templates.TemplateResponse(
        "conferences/detail.html",
        {
            "request": request,
            "conference": conference,
            "agenda_items": agenda_items,
            "current_user": current_user,
            "is_registered": is_registered,
            "unread_notification_count": unread_notification_count,
        },
    )


@router.get("/{conference_id}/edit", response_class=HTMLResponse)
async def edit_conference_page(
    request: Request,
    conference_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user),
):
    """Render the edit conference page."""
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if user is the creator
    if conference.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="您无权编辑此会议")

    # Get agenda items
    agenda_items = conference_crud.get_agenda_items(db, conference_id=conference_id)

    return templates.TemplateResponse(
        "conferences/edit.html",
        {
            "request": request,
            "conference": conference,
            "agenda_items": agenda_items,
            "current_user": current_user,
        },
    )


@router.post("/{conference_id}/edit", response_class=HTMLResponse)
async def edit_conference(
    request: Request,
    conference_id: int,
    title: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    location: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user),
):
    """Edit a conference."""
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if user is the creator
    if conference.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="您无权编辑此会议")

    # Parse date string to datetime
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M")
    except ValueError:
        return templates.TemplateResponse(
            "conferences/edit.html",
            {
                "request": request,
                "error": "日期格式无效",
                "conference": conference,
                "current_user": current_user,
            },
        )

    # Update conference
    conference_update = ConferenceUpdate(
        title=title,
        description=description,
        date=date_obj,
        location=location,
    )
    conference_crud.update_conference(db=db, conference_id=conference_id, conference=conference_update)

    # Redirect to conference detail
    return RedirectResponse(url=f"/conferences/{conference_id}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/{conference_id}/delete", response_class=HTMLResponse)
async def delete_conference(
    conference_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user),
):
    """Delete a conference."""
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if user is the creator
    if conference.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="您无权删除此会议")

    # Delete conference
    conference_crud.delete_conference(db=db, conference_id=conference_id)

    # Redirect to admin conferences
    return RedirectResponse(url="/conferences/admin", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/{conference_id}/agenda", response_class=HTMLResponse)
async def add_agenda_item(
    request: Request,
    conference_id: int,
    start_time: str = Form(...),
    end_time: str = Form(...),
    title: str = Form(...),
    speaker: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user),
):
    """Add an agenda item to a conference."""
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if user is the creator
    if conference.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="您无权向此会议添加议程项目")

    # Create agenda item
    agenda_item = AgendaItemCreate(
        start_time=start_time,
        end_time=end_time,
        title=title,
        speaker=speaker,
    )
    conference_crud.create_agenda_item(db=db, agenda_item=agenda_item, conference_id=conference_id)

    # Redirect to edit conference page
    return RedirectResponse(url=f"/conferences/{conference_id}/edit", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/{conference_id}/agenda/{agenda_item_id}/delete", response_class=HTMLResponse)
async def delete_agenda_item(
    conference_id: int,
    agenda_item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user),
):
    """Delete an agenda item."""
    conference = conference_crud.get_conference(db, conference_id=conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail="未找到会议")

    # Check if user is the creator
    if conference.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="您无权从此会议中删除议程项目")

    # Delete agenda item
    conference_crud.delete_agenda_item(db=db, agenda_item_id=agenda_item_id)

    # Redirect to edit conference page
    return RedirectResponse(url=f"/conferences/{conference_id}/edit", status_code=status.HTTP_303_SEE_OTHER)
