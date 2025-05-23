"""
更新所有用户密码的脚本。
运行方式：python -m app.scripts.update_all_passwords
"""

from sqlalchemy.orm import Session

from app.database import SessionLocal, create_tables
from app.crud import user as user_crud
from app.dependencies import get_password_hash


def update_all_passwords():
    """将所有用户的密码更新为'1'。"""
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 获取所有用户
        users = user_crud.get_users(db)
        
        # 新密码
        new_password = "1"
        hashed_password = get_password_hash(new_password)
        
        # 更新每个用户的密码
        updated_count = 0
        for user in users:
            user.hashed_password = hashed_password
            updated_count += 1
            print(f"已更新用户密码: {user.username}")
        
        # 提交更改
        db.commit()
        
        print(f"成功更新 {updated_count} 个用户的密码为 '{new_password}'")
    
    finally:
        db.close()


if __name__ == "__main__":
    # 确保数据库表已创建
    create_tables()
    
    # 更新所有用户密码
    update_all_passwords()
