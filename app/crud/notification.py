from sqlalchemy.orm import Session

from app.database import Notification, NotificationType


def get_notification(db: Session, notification_id: int):
    """获取通知。"""
    return db.query(Notification).filter(Notification.id == notification_id).first()


def get_notifications_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100, unread_only: bool = False):
    """获取用户的通知。"""
    query = db.query(Notification).filter(Notification.user_id == user_id)
    
    if unread_only:
        query = query.filter(Notification.is_read == False)
    
    return query.order_by(Notification.created_at.desc()).offset(skip).limit(limit).all()


def create_notification(
    db: Session,
    user_id: int,
    type: NotificationType,
    content: str,
    sender_id: int = None,
    related_id: int = None
):
    """创建通知。"""
    db_notification = Notification(
        user_id=user_id,
        sender_id=sender_id,
        type=type,
        content=content,
        related_id=related_id,
        is_read=False
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


def mark_notification_as_read(db: Session, notification_id: int):
    """将通知标记为已读。"""
    db_notification = get_notification(db, notification_id)
    if db_notification:
        db_notification.is_read = True
        db.commit()
        db.refresh(db_notification)
    return db_notification


def mark_all_notifications_as_read(db: Session, user_id: int):
    """将用户的所有通知标记为已读。"""
    db.query(Notification).filter(
        Notification.user_id == user_id,
        Notification.is_read == False
    ).update({"is_read": True})
    db.commit()


def delete_notification(db: Session, notification_id: int):
    """删除通知。"""
    db_notification = get_notification(db, notification_id)
    if db_notification:
        db.delete(db_notification)
        db.commit()
    return db_notification


def get_unread_notification_count(db: Session, user_id: int):
    """获取用户未读通知数量。"""
    return db.query(Notification).filter(
        Notification.user_id == user_id,
        Notification.is_read == False
    ).count()
