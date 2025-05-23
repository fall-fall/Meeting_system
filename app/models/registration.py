"""会议注册相关的数据模型"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.conference import ConferenceResponse
from app.models.user import UserResponse


class RegistrationBase(BaseModel):
    """注册基础模型"""
    conference_id: int  # 会议ID


class RegistrationCreate(RegistrationBase):
    """注册创建模型"""
    pass


class RegistrationResponse(RegistrationBase):
    """注册响应模型"""
    id: int  # 注册ID
    user_id: int  # 用户ID
    registered_at: datetime  # 注册时间
    conference: Optional[ConferenceResponse] = None  # 会议信息

    class Config:
        orm_mode = True  # 启用ORM模式


class UserRegistrationResponse(BaseModel):
    """用户注册响应模型，包含用户和会议信息"""
    id: int  # 注册ID
    user: UserResponse  # 用户信息
    conference: ConferenceResponse  # 会议信息
    registered_at: datetime  # 注册时间

    class Config:
        orm_mode = True  # 启用ORM模式
