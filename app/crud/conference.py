"""
会议数据库操作模块

本模块提供会议和议程项相关的数据库CRUD操作函数
"""

from datetime import datetime
from sqlalchemy.orm import Session

from app.database import Conference, AgendaItem
from app.models.conference import ConferenceCreate, ConferenceUpdate, AgendaItemCreate


def get_conference(db: Session, conference_id: int):
    """根据ID获取会议

    Args:
        db: 数据库会话
        conference_id: 会议ID

    Returns:
        Conference: 会议对象，如果不存在则返回None
    """
    return db.query(Conference).filter(Conference.id == conference_id).first()


def get_conferences(db: Session, skip: int = 0, limit: int = 100):
    """获取所有会议

    Args:
        db: 数据库会话
        skip: 跳过的记录数
        limit: 返回的最大记录数

    Returns:
        List[Conference]: 会议对象列表
    """
    return db.query(Conference).offset(skip).limit(limit).all()


def get_conferences_by_creator(db: Session, creator_id: int, skip: int = 0, limit: int = 100):
    """根据创建者ID获取会议

    Args:
        db: 数据库会话
        creator_id: 创建者ID
        skip: 跳过的记录数
        limit: 返回的最大记录数

    Returns:
        List[Conference]: 会议对象列表，按日期降序排序
    """
    return (
        db.query(Conference)
        .filter(Conference.creator_id == creator_id)  # 筛选创建者
        .order_by(Conference.date.desc())  # 按日期降序排序
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_conference(db: Session, conference: ConferenceCreate, creator_id: int):
    """创建新会议

    Args:
        db: 数据库会话
        conference: 会议创建模型
        creator_id: 创建者ID

    Returns:
        Conference: 创建的会议对象
    """
    # 创建会议对象
    db_conference = Conference(
        title=conference.title,  # 会议标题
        description=conference.description,  # 会议描述
        date=conference.date,  # 会议日期
        location=conference.location,  # 会议地点
        creator_id=creator_id,  # 创建者ID
    )

    # 添加到数据库并提交
    db.add(db_conference)
    db.commit()
    db.refresh(db_conference)

    return db_conference


def update_conference(db: Session, conference_id: int, conference: ConferenceUpdate):
    """更新会议

    Args:
        db: 数据库会话
        conference_id: 会议ID
        conference: 会议更新模型

    Returns:
        Conference: 更新后的会议对象，如果不存在则返回None
    """
    # 获取会议对象
    db_conference = get_conference(db, conference_id)
    if db_conference:
        # 更新会议属性
        for key, value in conference.model_dump().items():  # 使用model_dump替代已弃用的dict
            setattr(db_conference, key, value)

        # 提交更改
        db.commit()
        db.refresh(db_conference)

    return db_conference


def delete_conference(db: Session, conference_id: int):
    """删除会议

    Args:
        db: 数据库会话
        conference_id: 会议ID

    Returns:
        Conference: 被删除的会议对象，如果不存在则返回None
    """
    # 获取会议对象
    db_conference = get_conference(db, conference_id)
    if db_conference:
        # 删除会议
        db.delete(db_conference)
        db.commit()

    return db_conference


def create_agenda_item(db: Session, agenda_item: AgendaItemCreate, conference_id: int):
    """创建新议程项

    Args:
        db: 数据库会话
        agenda_item: 议程项创建模型
        conference_id: 所属会议ID

    Returns:
        AgendaItem: 创建的议程项对象
    """
    # 创建议程项对象
    db_agenda_item = AgendaItem(
        conference_id=conference_id,  # 所属会议ID
        start_time=agenda_item.start_time,  # 开始时间
        end_time=agenda_item.end_time,  # 结束时间
        title=agenda_item.title,  # 议程标题
        speaker=agenda_item.speaker,  # 演讲者
    )

    # 添加到数据库并提交
    db.add(db_agenda_item)
    db.commit()
    db.refresh(db_agenda_item)

    return db_agenda_item


def get_agenda_items(db: Session, conference_id: int):
    """获取会议的议程项

    Args:
        db: 数据库会话
        conference_id: 会议ID

    Returns:
        List[AgendaItem]: 议程项对象列表
    """
    return db.query(AgendaItem).filter(AgendaItem.conference_id == conference_id).all()


def delete_agenda_item(db: Session, agenda_item_id: int):
    """删除议程项

    Args:
        db: 数据库会话
        agenda_item_id: 议程项ID

    Returns:
        AgendaItem: 被删除的议程项对象，如果不存在则返回None
    """
    # 获取议程项对象
    db_agenda_item = db.query(AgendaItem).filter(AgendaItem.id == agenda_item_id).first()
    if db_agenda_item:
        # 删除议程项
        db.delete(db_agenda_item)
        db.commit()

    return db_agenda_item


def get_upcoming_conferences(db: Session, skip: int = 0, limit: int = 100):
    """获取即将举行的会议

    Args:
        db: 数据库会话
        skip: 跳过的记录数
        limit: 返回的最大记录数

    Returns:
        List[Conference]: 会议对象列表，按日期升序排序
    """
    # 获取当前时间
    now = datetime.now()

    # 查询日期大于等于当前时间的会议
    return (
        db.query(Conference)
        .filter(Conference.date >= now)  # 筛选未来的会议
        .order_by(Conference.date)  # 按日期升序排序
        .offset(skip)
        .limit(limit)
        .all()
    )
