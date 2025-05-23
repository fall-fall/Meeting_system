"""
认证相关的路由处理模块

包含用户注册、登录、登出和令牌获取等功能
"""

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import settings
from app.crud import user as user_crud
from app.database import get_db
from app.dependencies import authenticate_user, create_access_token
from app.models.user import UserCreate, Token

# 创建路由器
router = APIRouter(prefix="/auth", tags=["auth"])
# 设置模板引擎
templates = Jinja2Templates(directory="app/templates")


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """渲染注册页面"""
    return templates.TemplateResponse("auth/register.html", {"request": request})


@router.post("/register", response_class=HTMLResponse)
async def register(
    request: Request,
    username: str = Form(...),  # 用户名
    email: str = Form(...),  # 电子邮箱
    password: str = Form(...),  # 密码
    confirm_password: str = Form(...),  # 确认密码
    is_admin: bool = Form(False),  # 是否为管理员
    db: Session = Depends(get_db),  # 数据库会话
):
    """注册新用户"""
    if password != confirm_password:
        return templates.TemplateResponse(
            "auth/register.html",
            {"request": request, "error": "密码不匹配"},
        )

    # Check if username already exists
    db_user = user_crud.get_user_by_username(db, username=username)
    if db_user:
        return templates.TemplateResponse(
            "auth/register.html",
            {"request": request, "error": "用户名已被注册"},
        )

    # Check if email already exists
    db_user = user_crud.get_user_by_email(db, email=email)
    if db_user:
        return templates.TemplateResponse(
            "auth/register.html",
            {"request": request, "error": "邮箱已被注册"},
        )

    # Create user
    user = UserCreate(username=username, email=email, password=password, is_admin=is_admin)
    user_crud.create_user(db=db, user=user)

    # Create access token and login user automatically
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )

    # Set cookie and redirect to home page
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """渲染登录页面"""
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),  # 用户名
    password: str = Form(...),  # 密码
    db: Session = Depends(get_db),  # 数据库会话
):
    """用户登录"""
    user = authenticate_user(db, username, password)
    if not user:
        return templates.TemplateResponse(
            "auth/login.html",
            {"request": request, "error": "用户名或密码不正确"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    # Set cookie and redirect to home page
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response


@router.get("/logout", response_class=HTMLResponse)
async def logout():
    """用户登出"""
    # 创建重定向响应
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    # 删除认证Cookie
    response.delete_cookie(key="access_token")
    return response


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),  # OAuth2表单数据
    db: Session = Depends(get_db),  # 数据库会话
):
    """获取访问令牌（用于API认证）"""
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码不正确",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
