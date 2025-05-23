"""
删除指定用户的脚本。
运行方式：python -m app.scripts.delete_users
"""

from sqlalchemy.orm import Session

from app.database import SessionLocal, create_tables, User


def delete_users():
    """删除指定的用户。"""
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 要删除的用户名列表
        usernames_to_delete = ["1", "2", "rain fall"]
        
        for username in usernames_to_delete:
            # 查找用户
            user = db.query(User).filter(User.username == username).first()
            
            if user:
                # 删除用户
                db.delete(user)
                print(f"已删除用户: {username}")
            else:
                print(f"未找到用户: {username}")
        
        # 提交更改
        db.commit()
        
        print("用户删除操作完成")
    
    finally:
        db.close()


if __name__ == "__main__":
    # 确保数据库表已创建
    create_tables()
    
    # 删除指定用户
    delete_users()
