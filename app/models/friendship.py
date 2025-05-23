"""好友关系相关的数据模型"""

from datetime import datetime

from pydantic import BaseModel

from app.database import FriendshipStatus


class FriendshipBase(BaseModel):
    """好友关系基础模型"""
    user_id: int  # 发起者ID
    friend_id: int  # 接收者ID


class FriendshipCreate(FriendshipBase):
    """好友关系创建模型"""
    pass


class FriendshipUpdate(BaseModel):
    """好友关系更新模型"""
    status: FriendshipStatus  # 关系状态


class FriendshipResponse(FriendshipBase):
    """好友关系响应模型"""
    id: int  # 关系ID
    status: FriendshipStatus  # 关系状态
    created_at: datetime  # 创建时间
    updated_at: datetime  # 更新时间

    class Config:
        from_attributes = True  # 启用ORM模式


class FriendResponse(BaseModel):
    """好友响应模型，用于返回好友信息"""
    id: int  # 用户ID
    username: str  # 用户名
    email: str  # 电子邮箱
    is_admin: bool  # 是否为管理员

    class Config:
        from_attributes = True  # 启用ORM模式
