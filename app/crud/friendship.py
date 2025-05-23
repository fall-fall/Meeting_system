"""
好友关系数据库操作模块

本模块提供好友关系相关的数据库CRUD操作函数
"""

from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

from app.database import User, Friendship, FriendshipStatus


def get_friendship(db: Session, friendship_id: int):
    """根据ID获取好友关系

    Args:
        db: 数据库会话
        friendship_id: 好友关系ID

    Returns:
        Friendship: 好友关系对象，如果不存在则返回None
    """
    return db.query(Friendship).filter(Friendship.id == friendship_id).first()


def get_friendship_by_users(db: Session, user_id: int, friend_id: int):
    """获取两个用户之间的好友关系

    Args:
        db: 数据库会话
        user_id: 用户ID
        friend_id: 好友ID

    Returns:
        Friendship: 好友关系对象，如果不存在则返回None

    Note:
        此函数会查找两个用户之间的好友关系，无论谁是发起者
    """
    return (
        db.query(Friendship)
        .filter(
            or_(
                # 用户是发起者，好友是接收者
                and_(Friendship.user_id == user_id, Friendship.friend_id == friend_id),
                # 好友是发起者，用户是接收者
                and_(Friendship.user_id == friend_id, Friendship.friend_id == user_id),
            )
        )
        .first()
    )


def get_friendships_by_user(db: Session, user_id: int, status: FriendshipStatus = None):
    """获取用户的所有好友关系

    Args:
        db: 数据库会话
        user_id: 用户ID
        status: 好友关系状态（可选）

    Returns:
        List[Friendship]: 好友关系对象列表
    """
    # 查询用户参与的所有好友关系（作为发起者或接收者）
    query = db.query(Friendship).filter(
        or_(Friendship.user_id == user_id, Friendship.friend_id == user_id)
    )

    # 如果指定了状态，则进一步筛选
    if status:
        query = query.filter(Friendship.status == status)

    return query.all()


def get_friends(db: Session, user_id: int):
    """获取用户的所有好友

    Args:
        db: 数据库会话
        user_id: 用户ID

    Returns:
        List[User]: 好友用户对象列表
    """
    # 获取用户发起的已接受的好友关系
    sent_friendships = (
        db.query(Friendship)
        .filter(
            Friendship.user_id == user_id,  # 用户是发起者
            Friendship.status == FriendshipStatus.ACCEPTED  # 状态为已接受
        )
        .all()
    )

    # 获取用户接收的已接受的好友关系
    received_friendships = (
        db.query(Friendship)
        .filter(
            Friendship.friend_id == user_id,  # 用户是接收者
            Friendship.status == FriendshipStatus.ACCEPTED  # 状态为已接受
        )
        .all()
    )

    # 提取好友ID
    friend_ids = [f.friend_id for f in sent_friendships] + [f.user_id for f in received_friendships]

    # 获取好友用户对象
    return db.query(User).filter(User.id.in_(friend_ids)).all()


def get_pending_friend_requests(db: Session, user_id: int):
    """获取用户收到的待处理好友请求

    Args:
        db: 数据库会话
        user_id: 用户ID

    Returns:
        List[Friendship]: 待处理好友请求列表
    """
    return (
        db.query(Friendship)
        .filter(
            Friendship.friend_id == user_id,  # 用户是接收者
            Friendship.status == FriendshipStatus.PENDING  # 状态为待处理
        )
        .all()
    )


def create_friendship(db: Session, user_id: int, friend_id: int):
    """创建好友关系

    Args:
        db: 数据库会话
        user_id: 发起者用户ID
        friend_id: 接收者用户ID

    Returns:
        Friendship: 创建或已存在的好友关系对象
    """
    # 检查是否已存在好友关系
    existing_friendship = get_friendship_by_users(db, user_id, friend_id)
    if existing_friendship:
        return existing_friendship  # 如果已存在，直接返回

    # 创建新的好友关系
    db_friendship = Friendship(
        user_id=user_id,  # 发起者ID
        friend_id=friend_id,  # 接收者ID
        status=FriendshipStatus.PENDING  # 初始状态为待处理
    )

    # 添加到数据库并提交
    db.add(db_friendship)
    db.commit()
    db.refresh(db_friendship)

    return db_friendship


def update_friendship_status(db: Session, friendship_id: int, status: FriendshipStatus):
    """更新好友关系状态

    Args:
        db: 数据库会话
        friendship_id: 好友关系ID
        status: 新的状态

    Returns:
        Friendship: 更新后的好友关系对象，如果不存在则返回None
    """
    # 获取好友关系对象
    db_friendship = get_friendship(db, friendship_id)
    if db_friendship:
        # 更新状态
        db_friendship.status = status
        db.commit()
        db.refresh(db_friendship)

    return db_friendship


def delete_friendship(db: Session, friendship_id: int):
    """删除好友关系

    Args:
        db: 数据库会话
        friendship_id: 好友关系ID

    Returns:
        Friendship: 被删除的好友关系对象，如果不存在则返回None
    """
    # 获取好友关系对象
    db_friendship = get_friendship(db, friendship_id)
    if db_friendship:
        # 删除好友关系
        db.delete(db_friendship)
        db.commit()

    return db_friendship
