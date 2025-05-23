from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db, User

# 密码哈希工具
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # 使用bcrypt算法进行密码哈希

# OAuth2认证方案
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")  # 设置获取令牌的URL


def verify_password(plain_password, hashed_password):
    """验证密码

    比较明文密码与哈希密码是否匹配

    Args:
        plain_password: 明文密码
        hashed_password: 哈希后的密码

    Returns:
        bool: 密码是否匹配
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """生成密码哈希

    对明文密码进行哈希处理

    Args:
        password: 明文密码

    Returns:
        str: 哈希后的密码
    """
    return pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str):
    """用户认证

    验证用户名和密码是否正确

    Args:
        db: 数据库会话
        username: 用户名
        password: 明文密码

    Returns:
        User|False: 认证成功返回用户对象，失败返回False
    """
    # 根据用户名查找用户
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False  # 用户不存在
    if not verify_password(password, user.hashed_password):
        return False  # 密码错误
    return user  # 认证成功，返回用户对象


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """创建访问令牌

    生成JWT访问令牌

    Args:
        data: 要编码到令牌中的数据
        expires_delta: 令牌过期时间增量，如果为None则使用默认值

    Returns:
        str: 编码后的JWT令牌
    """
    # 复制数据，避免修改原始数据
    to_encode = data.copy()

    # 设置过期时间
    now = datetime.now(timezone.utc)  # 使用带时区的UTC时间
    if expires_delta:
        expire = now + expires_delta  # 使用指定的过期时间
    else:
        expire = now + timedelta(minutes=15)  # 默认15分钟过期

    # 添加过期时间到令牌数据
    to_encode.update({"exp": expire})

    # 使用密钥和算法对数据进行编码
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """获取当前用户

    从JWT令牌中解析并获取当前用户

    Args:
        token: JWT令牌
        db: 数据库会话

    Returns:
        User: 当前用户对象

    Raises:
        HTTPException: 如果令牌无效或用户不存在
    """
    # 定义认证失败异常
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # 解码JWT令牌
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")  # 获取用户名
        if username is None:
            raise credentials_exception  # 令牌中没有用户名
    except JWTError:
        raise credentials_exception  # JWT解码失败

    # 根据用户名查找用户
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception  # 用户不存在

    return user  # 返回用户对象


async def get_current_active_user(request: Request = None, db: Session = Depends(get_db)):
    """获取当前活跃用户或重定向到登录页面

    从请求中获取当前用户，如果未登录则重定向到登录页面

    Args:
        request: HTTP请求对象
        db: 数据库会话

    Returns:
        User|RedirectResponse: 当前用户对象或重定向响应
    """
    # 检查请求对象是否存在
    if request is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 从Cookie中获取访问令牌
    token = request.cookies.get("access_token")
    if not token or not token.startswith("Bearer "):
        # 未找到有效令牌，重定向到登录页面
        response = RedirectResponse(url="/api/auth/login")
        return response

    try:
        # 验证令牌并获取用户
        user = await get_current_user(token.replace("Bearer ", ""), db)
        return user  # 返回用户对象
    except:
        # 令牌验证失败，重定向到登录页面
        response = RedirectResponse(url="/api/auth/login")
        return response


async def get_current_admin_user(request: Request, db: Session = Depends(get_db)):
    """获取当前管理员用户或重定向

    从请求中获取当前用户，验证是否为管理员，如果不是则重定向

    Args:
        request: HTTP请求对象
        db: 数据库会话

    Returns:
        User|RedirectResponse: 当前管理员用户对象或重定向响应
    """
    # 从Cookie中获取访问令牌
    token = request.cookies.get("access_token")
    if not token or not token.startswith("Bearer "):
        # 未找到有效令牌，重定向到登录页面
        return RedirectResponse(url="/api/auth/login")

    try:
        # 验证令牌并获取用户
        user = await get_current_user(token.replace("Bearer ", ""), db)
        if not user.is_admin:
            # 用户不是管理员，权限不足，重定向到首页
            return RedirectResponse(url="/")
        return user  # 返回管理员用户对象
    except:
        # 令牌验证失败，重定向到登录页面
        return RedirectResponse(url="/api/auth/login")
