"""会议和议程项相关的数据模型"""

from datetime import datetime
from typing import List

from pydantic import BaseModel


class AgendaItemBase(BaseModel):
    """议程项基础模型"""
    start_time: str  # 开始时间
    end_time: str  # 结束时间
    title: str  # 标题
    speaker: str  # 演讲者


class AgendaItemCreate(AgendaItemBase):
    """议程项创建模型"""
    pass


class AgendaItemResponse(AgendaItemBase):
    """议程项响应模型"""
    id: int  # 议程项ID
    conference_id: int  # 所属会议ID
    created_at: datetime  # 创建时间

    class Config:
        orm_mode = True  # 启用ORM模式


class ConferenceBase(BaseModel):
    """会议基础模型"""
    title: str  # 会议标题
    description: str  # 会议描述
    date: datetime  # 会议日期
    location: str  # 会议地点


class ConferenceCreate(ConferenceBase):
    """会议创建模型"""
    pass


class ConferenceUpdate(ConferenceBase):
    """会议更新模型"""
    pass


class ConferenceResponse(ConferenceBase):
    """会议响应模型"""
    id: int  # 会议ID
    creator_id: int  # 创建者ID
    created_at: datetime  # 创建时间
    agenda_items: List[AgendaItemResponse] = []  # 议程项列表

    class Config:
        orm_mode = True  # 启用ORM模式
