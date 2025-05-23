"""通知相关的数据模型"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.database import NotificationType


class NotificationBase(BaseModel):
    """通知基础模型"""
    user_id: int  # 接收者ID
    type: NotificationType  # 通知类型
    content: str  # 通知内容
    sender_id: Optional[int] = None  # 发送者ID
    related_id: Optional[int] = None  # 相关ID


class NotificationCreate(NotificationBase):
    """通知创建模型"""
    pass


class NotificationUpdate(BaseModel):
    """通知更新模型"""
    is_read: bool = True  # 是否已读


class NotificationResponse(NotificationBase):
    """通知响应模型"""
    id: int  # 通知ID
    is_read: bool  # 是否已读
    created_at: datetime  # 创建时间
    sender_username: Optional[str] = None  # 发送者用户名

    class Config:
        from_attributes = True  # 启用ORM模式
