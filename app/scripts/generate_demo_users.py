"""
生成示例用户的脚本。
运行方式：python -m app.scripts.generate_demo_users
"""

from sqlalchemy.orm import Session

from app.database import SessionLocal, create_tables
from app.crud import user as user_crud
from app.models.user import UserCreate


def generate_demo_users():
    """生成示例用户。"""
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 示例用户数据
        demo_users = [
            {"username": "user1", "email": "user1@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user2", "email": "user2@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user3", "email": "user3@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user4", "email": "user4@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user5", "email": "user5@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user6", "email": "user6@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user7", "email": "user7@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user8", "email": "user8@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user9", "email": "user9@meeting.cn", "password": "password123", "is_admin": False},
            {"username": "user10", "email": "user10@meeting.cn", "password": "password123", "is_admin": True},
        ]
        
        # 创建用户
        created_count = 0
        for user_data in demo_users:
            # 检查用户是否已存在
            existing_user = user_crud.get_user_by_username(db, username=user_data["username"])
            if not existing_user:
                user = UserCreate(**user_data)
                user_crud.create_user(db=db, user=user)
                created_count += 1
                print(f"已创建用户: {user_data['username']}")
            else:
                print(f"用户已存在: {user_data['username']}")
        
        print(f"成功创建 {created_count} 个示例用户")
    
    finally:
        db.close()


if __name__ == "__main__":
    # 确保数据库表已创建
    create_tables()
    
    # 生成示例用户
    generate_demo_users()
