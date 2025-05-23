"""
生成会议邀请通知的脚本。
运行方式：python -m app.scripts.generate_invitations
"""

import random

from sqlalchemy.orm import Session

from app.database import SessionLocal, create_tables, NotificationType
from app.crud import user as user_crud
from app.crud import conference as conference_crud
from app.crud import notification as notification_crud
from app.crud import registration as registration_crud


def generate_invitations():
    """生成会议邀请通知。"""
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 获取所有用户
        users = user_crud.get_users(db)
        if len(users) < 2:
            print("用户数量不足，无法生成邀请")
            return
        
        # 获取所有会议
        conferences = conference_crud.get_conferences(db)
        if not conferences:
            print("没有会议，无法生成邀请")
            return
        
        # 为每个用户生成1-3个会议邀请
        for user in users:
            # 随机选择1-3个会议
            num_invitations = min(random.randint(1, 3), len(conferences))
            selected_conferences = random.sample(conferences, num_invitations)
            
            for conference in selected_conferences:
                # 检查用户是否已经注册参加会议
                registration = registration_crud.get_registration_by_user_and_conference(
                    db, user_id=user.id, conference_id=conference.id
                )
                if registration:
                    continue
                
                # 随机选择一个发送者（不能是自己）
                potential_senders = [u for u in users if u.id != user.id]
                if not potential_senders:
                    continue
                sender = random.choice(potential_senders)
                
                # 创建通知
                notification_crud.create_notification(
                    db,
                    user_id=user.id,
                    type=NotificationType.MEETING_INVITATION,
                    content=f"{sender.username} 邀请您参加会议 '{conference.title}'",
                    sender_id=sender.id,
                    related_id=conference.id
                )
                
                print(f"已创建会议邀请通知: {sender.username} -> {user.username} (会议: {conference.title})")
        
        print("会议邀请通知生成完成")
    
    finally:
        db.close()


if __name__ == "__main__":
    # 确保数据库表已创建
    create_tables()
    
    # 生成会议邀请通知
    generate_invitations()
