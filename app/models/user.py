##
# @file user.py
# @brief 用户相关的数据模型
# @details 定义了用户的各种数据模型，包括创建、登录、响应和令牌模型
# @author Meeting System Team
# @date 2024
# @version 1.0
##

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


##
# @class UserBase
# @brief 用户基础模型
# @details 包含用户名和邮箱的基础信息
##
class UserBase(BaseModel):
    username: str  ##< 用户名
    email: str  ##< 电子邮箱


##
# @class UserCreate
# @brief 用户创建模型
# @details 用于注册新用户，包含密码和管理员权限
##
class UserCreate(UserBase):
    password: str  ##< 密码
    is_admin: bool = False  ##< 是否为管理员


##
# @class UserLogin
# @brief 用户登录模型
# @details 用于用户登录验证
##
class UserLogin(BaseModel):
    username: str  ##< 用户名
    password: str  ##< 密码


##
# @class UserResponse
# @brief 用户响应模型
# @details 用于返回用户信息，不包含敏感数据
##
class UserResponse(UserBase):
    id: int  ##< 用户ID
    is_admin: bool  ##< 是否为管理员
    created_at: datetime  ##< 创建时间

    class Config:
        orm_mode = True  ##< 启用ORM模式


##
# @class Token
# @brief 令牌模型
# @details 用于JWT认证的令牌信息
##
class Token(BaseModel):
    access_token: str  ##< 访问令牌
    token_type: str  ##< 令牌类型


##
# @class TokenData
# @brief 令牌数据模型
# @details 用于存储令牌中的数据
##
class TokenData(BaseModel):
    username: Optional[str] = None  ##< 用户名
