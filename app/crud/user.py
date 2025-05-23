"""
用户数据库操作模块

本模块提供用户相关的数据库CRUD操作函数
"""

from sqlalchemy.orm import Session

from app.database import User
from app.dependencies import get_password_hash
from app.models.user import UserCreate


def get_user(db: Session, user_id: int):
    """根据ID获取用户

    Args:
        db: 数据库会话
        user_id: 用户ID

    Returns:
        User: 用户对象，如果不存在则返回None
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    """根据用户名获取用户

    Args:
        db: 数据库会话
        username: 用户名

    Returns:
        User: 用户对象，如果不存在则返回None
    """
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    """根据电子邮箱获取用户

    Args:
        db: 数据库会话
        email: 电子邮箱

    Returns:
        User: 用户对象，如果不存在则返回None
    """
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """获取所有用户

    Args:
        db: 数据库会话
        skip: 跳过的记录数
        limit: 返回的最大记录数

    Returns:
        List[User]: 用户对象列表
    """
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    """创建新用户

    Args:
        db: 数据库会话
        user: 用户创建模型

    Returns:
        User: 创建的用户对象
    """
    # 对密码进行哈希处理
    hashed_password = get_password_hash(user.password)

    # 创建用户对象
    db_user = User(
        username=user.username,  # 用户名
        email=user.email,  # 电子邮箱
        hashed_password=hashed_password,  # 哈希后的密码
        is_admin=user.is_admin,  # 是否为管理员
    )

    # 添加到数据库并提交
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
