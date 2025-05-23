"""用户相关的数据模型"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    """用户基础模型，包含用户名和邮箱"""
    username: str  # 用户名
    email: str  # 电子邮箱


class UserCreate(UserBase):
    """用户创建模型，用于注册新用户"""
    password: str  # 密码
    is_admin: bool = False  # 是否为管理员


class UserLogin(BaseModel):
    """用户登录模型，用于用户登录"""
    username: str  # 用户名
    password: str  # 密码


class UserResponse(UserBase):
    """用户响应模型，用于返回用户信息"""
    id: int  # 用户ID
    is_admin: bool  # 是否为管理员
    created_at: datetime  # 创建时间

    class Config:
        orm_mode = True  # 启用ORM模式


class Token(BaseModel):
    """令牌模型，用于JWT认证"""
    access_token: str  # 访问令牌
    token_type: str  # 令牌类型


class TokenData(BaseModel):
    """令牌数据模型，用于存储令牌中的数据"""
    username: Optional[str] = None  # 用户名
