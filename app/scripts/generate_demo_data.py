"""
生成示例数据的脚本，包括会议、好友关系和通知。
运行方式：python -m app.scripts.generate_demo_data
"""

import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.database import SessionLocal, create_tables, FriendshipStatus, NotificationType
from app.crud import user as user_crud
from app.crud import conference as conference_crud
from app.crud import friendship as friendship_crud
from app.crud import notification as notification_crud
from app.crud import registration as registration_crud
from app.models.conference import ConferenceCreate
from app.models.registration import RegistrationCreate


def generate_demo_data():
    """生成示例数据。"""
    # 创建数据库会话
    db = SessionLocal()

    try:
        # 获取所有用户
        users = user_crud.get_users(db)
        if len(users) < 5:
            print("请先运行 generate_demo_users.py 创建示例用户")
            return

        # 创建示例会议
        conferences = create_demo_conferences(db, users)

        # 创建示例好友关系
        create_demo_friendships(db, users)

        # 创建示例会议注册
        create_demo_registrations(db, users, conferences)

        # 创建示例通知
        create_demo_notifications(db, users, conferences)

        print("示例数据生成完成！")

    finally:
        db.close()


def create_demo_conferences(db: Session, users):
    """创建示例会议。"""
    # 示例会议数据
    conference_data = [
        {
            "title": "Python 技术交流会",
            "description": "讨论 Python 最新技术和应用，包括 FastAPI、Django、Flask 等框架的使用经验。",
            "date": datetime.now() + timedelta(days=7),
            "location": "线上会议",
        },
        {
            "title": "人工智能与机器学习研讨会",
            "description": "探讨人工智能和机器学习的最新进展，包括深度学习、强化学习、自然语言处理等领域。",
            "date": datetime.now() + timedelta(days=14),
            "location": "北京市海淀区中关村科技园",
        },
        {
            "title": "Web 前端开发技术分享",
            "description": "分享 Web 前端开发的最新技术和趋势，包括 React、Vue、Angular 等框架的使用经验。",
            "date": datetime.now() + timedelta(days=21),
            "location": "上海市浦东新区张江高科技园区",
        },
        {
            "title": "数据库技术与应用",
            "description": "讨论各种数据库技术的应用和优化，包括关系型数据库和 NoSQL 数据库。",
            "date": datetime.now() + timedelta(days=28),
            "location": "广州市天河区科技园",
        },
        {
            "title": "云计算与微服务架构",
            "description": "探讨云计算和微服务架构的最佳实践，包括 Docker、Kubernetes、AWS、Azure 等技术。",
            "date": datetime.now() + timedelta(days=35),
            "location": "深圳市南山区科技园",
        },
    ]

    # 获取管理员用户
    admin_users = [user for user in users if user.is_admin]
    if not admin_users:
        admin_users = [users[0]]  # 如果没有管理员，使用第一个用户

    # 创建会议
    conferences = []
    for data in conference_data:
        creator = random.choice(admin_users)
        conference = ConferenceCreate(**data)
        db_conference = conference_crud.create_conference(db, conference=conference, creator_id=creator.id)
        conferences.append(db_conference)
        print(f"已创建会议: {data['title']}")

    return conferences


def create_demo_friendships(db: Session, users):
    """创建示例好友关系。"""
    # 为每个用户创建 2-4 个好友
    for user in users:
        # 随机选择 2-4 个其他用户作为好友
        potential_friends = [u for u in users if u.id != user.id]
        num_friends = min(random.randint(2, 4), len(potential_friends))
        friends = random.sample(potential_friends, num_friends)

        for friend in friends:
            # 检查是否已经是好友
            existing = friendship_crud.get_friendship_by_users(db, user.id, friend.id)
            if not existing:
                # 创建好友关系，50% 概率为已接受状态
                status = random.choice([FriendshipStatus.PENDING, FriendshipStatus.ACCEPTED])
                friendship = friendship_crud.create_friendship(db, user.id, friend.id)
                if status == FriendshipStatus.ACCEPTED:
                    friendship_crud.update_friendship_status(db, friendship.id, FriendshipStatus.ACCEPTED)
                print(f"已创建好友关系: {user.username} -> {friend.username} ({status.value})")


def create_demo_registrations(db: Session, users, conferences):
    """创建示例会议注册。"""
    # 为每个会议随机注册 3-6 个用户
    for conference in conferences:
        # 排除创建者（因为创建者不需要注册）
        potential_attendees = [u for u in users if u.id != conference.creator_id]
        num_attendees = min(random.randint(3, 6), len(potential_attendees))
        attendees = random.sample(potential_attendees, num_attendees)

        for attendee in attendees:
            # 检查是否已经注册
            existing = registration_crud.get_registration_by_user_and_conference(db, user_id=attendee.id, conference_id=conference.id)
            if not existing:
                # 创建注册
                registration = RegistrationCreate(conference_id=conference.id)
                registration_crud.create_registration(db, registration=registration, user_id=attendee.id)
                print(f"已创建会议注册: {attendee.username} -> {conference.title}")


def create_demo_notifications(db: Session, users, conferences):
    """创建示例通知。"""
    # 为每个用户创建 3-5 个随机通知
    notification_types = list(NotificationType)

    for user in users:
        num_notifications = random.randint(3, 5)

        for _ in range(num_notifications):
            # 随机选择通知类型
            notification_type = random.choice(notification_types)

            # 随机选择发送者（可能为空）
            sender = random.choice([None] + [u for u in users if u.id != user.id])
            sender_id = sender.id if sender else None

            # 根据通知类型生成内容和相关 ID
            content = ""
            related_id = None

            if notification_type == NotificationType.FRIEND_REQUEST:
                if sender:
                    content = f"{sender.username} 向您发送了好友请求"
                    # 查找或创建一个好友关系作为相关 ID
                    friendship = friendship_crud.get_friendship_by_users(db, sender_id, user.id)
                    if not friendship:
                        friendship = friendship_crud.create_friendship(db, sender_id, user.id)
                    related_id = friendship.id

            elif notification_type == NotificationType.FRIEND_ACCEPTED:
                if sender:
                    content = f"{sender.username} 接受了您的好友请求"
                    # 查找或创建一个好友关系作为相关 ID
                    friendship = friendship_crud.get_friendship_by_users(db, user.id, sender_id)
                    if not friendship:
                        friendship = friendship_crud.create_friendship(db, user.id, sender_id)
                        friendship_crud.update_friendship_status(db, friendship.id, FriendshipStatus.ACCEPTED)
                    related_id = friendship.id

            elif notification_type == NotificationType.MEETING_INVITATION:
                if sender and conferences:
                    conference = random.choice(conferences)
                    content = f"{sender.username} 邀请您参加会议 '{conference.title}'"
                    related_id = conference.id

            elif notification_type == NotificationType.MEETING_JOINED:
                if conferences:
                    conference = random.choice(conferences)
                    content = f"您已成功加入会议 '{conference.title}'"
                    related_id = conference.id

            elif notification_type == NotificationType.MEETING_LEFT:
                if conferences:
                    conference = random.choice(conferences)
                    content = f"您已退出会议 '{conference.title}'"
                    related_id = conference.id

            # 创建通知
            if content:
                # 随机设置已读状态
                is_read = random.choice([True, False])
                notification = notification_crud.create_notification(
                    db, user_id=user.id, type=notification_type, content=content,
                    sender_id=sender_id, related_id=related_id
                )
                if is_read:
                    notification_crud.mark_notification_as_read(db, notification.id)
                print(f"已创建通知: {user.username} <- {notification_type.value} ({content[:30]}...)")


if __name__ == "__main__":
    # 确保数据库表已创建
    create_tables()

    # 生成示例数据
    generate_demo_data()
