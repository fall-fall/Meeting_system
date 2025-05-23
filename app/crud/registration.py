"""
会议注册数据库操作模块

本模块提供会议注册相关的数据库CRUD操作函数
"""

from sqlalchemy.orm import Session

from app.database import Registration
from app.models.registration import RegistrationCreate


def get_registration(db: Session, registration_id: int):
    """根据ID获取注册记录

    Args:
        db: 数据库会话
        registration_id: 注册记录ID

    Returns:
        Registration: 注册记录对象，如果不存在则返回None
    """
    return db.query(Registration).filter(Registration.id == registration_id).first()


def get_registration_by_user_and_conference(db: Session, user_id: int, conference_id: int):
    """根据用户ID和会议ID获取注册记录

    Args:
        db: 数据库会话
        user_id: 用户ID
        conference_id: 会议ID

    Returns:
        Registration: 注册记录对象，如果不存在则返回None
    """
    return db.query(Registration).filter(
        Registration.user_id == user_id,
        Registration.conference_id == conference_id
    ).first()


def get_registrations_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    """根据用户ID获取注册记录列表

    Args:
        db: 数据库会话
        user_id: 用户ID
        skip: 跳过的记录数
        limit: 返回的最大记录数

    Returns:
        List[Registration]: 注册记录对象列表
    """
    return db.query(Registration).filter(Registration.user_id == user_id).offset(skip).limit(limit).all()


def get_registrations_by_conference(db: Session, conference_id: int, skip: int = 0, limit: int = 100):
    """根据会议ID获取注册记录列表

    Args:
        db: 数据库会话
        conference_id: 会议ID
        skip: 跳过的记录数
        limit: 返回的最大记录数

    Returns:
        List[Registration]: 注册记录对象列表
    """
    return db.query(Registration).filter(Registration.conference_id == conference_id).offset(skip).limit(limit).all()


def create_registration(db: Session, registration: RegistrationCreate, user_id: int):
    """创建新的注册记录

    Args:
        db: 数据库会话
        registration: 注册记录创建模型
        user_id: 用户ID

    Returns:
        Registration: 创建的注册记录对象
    """
    # 创建注册记录对象
    db_registration = Registration(
        user_id=user_id,  # 用户ID
        conference_id=registration.conference_id,  # 会议ID
    )

    # 添加到数据库并提交
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)

    return db_registration


def delete_registration(db: Session, registration_id: int):
    """删除注册记录

    Args:
        db: 数据库会话
        registration_id: 注册记录ID

    Returns:
        Registration: 被删除的注册记录对象，如果不存在则返回None
    """
    # 获取注册记录对象
    db_registration = get_registration(db, registration_id)
    if db_registration:
        # 删除注册记录
        db.delete(db_registration)
        db.commit()

    return db_registration
