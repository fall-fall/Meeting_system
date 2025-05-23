from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.database import get_db, create_tables
from app.routers import auth, conferences, registrations, my_conferences, friends, notifications
from app.crud import conference as conference_crud
from app.crud import notification as notification_crud
from app.init_db import init_db

# 创建数据库表并初始化数据
create_tables()  # 创建所有数据库表
init_db()  # 初始化基础数据（如管理员账号）

# 创建FastAPI应用实例
app = FastAPI(title=settings.APP_NAME)  # 设置应用名称

# 添加会话中间件（用于管理用户会话）
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

# 挂载静态文件目录（CSS、JavaScript等）
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 包含各个路由模块
app.include_router(auth.router, prefix=settings.API_PREFIX)  # 认证相关路由
app.include_router(conferences.router, prefix=settings.API_PREFIX)  # 会议相关路由
app.include_router(registrations.router, prefix=settings.API_PREFIX)  # 会议注册相关路由
app.include_router(my_conferences.router, prefix=settings.API_PREFIX)  # 我的会议相关路由
app.include_router(friends.router, prefix=settings.API_PREFIX)  # 好友相关路由
app.include_router(notifications.router, prefix=settings.API_PREFIX)  # 通知相关路由

# 设置模板引擎
templates = Jinja2Templates(directory="app/templates")  # 指定模板目录


@app.get("/", response_class=HTMLResponse)
async def home(
    request: Request,
    db: Session = Depends(get_db),
):
    """首页路由处理函数"""
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
            pass  # 如果获取用户失败，则视为未登录

    # 获取所有会议列表
    conferences = conference_crud.get_conferences(db)

    # 返回渲染后的首页模板
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,  # 请求对象（Jinja2模板需要）
            "conferences": conferences,  # 会议列表
            "current_user": current_user,  # 当前用户
            "unread_notification_count": unread_notification_count  # 未读通知数量
        },
    )


@app.get("/api/health")
async def health_check():
    """健康检查接口

    用于监控系统是否正常运行
    """
    return {"status": "ok", "message": "系统运行正常"}
