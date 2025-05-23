"""
将admin用户的密码重置为admin123的脚本。
运行方式：python -m app.scripts.fix_admin_password
"""

from sqlalchemy.orm import Session

from app.database import SessionLocal, create_tables
from app.crud import user as user_crud
from app.dependencies import get_password_hash


def fix_admin_password():
    """将admin用户的密码重置为'admin123'。"""
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 获取admin用户
        admin_user = user_crud.get_user_by_username(db, username="admin")
        
        if admin_user:
            # 设置新密码
            new_password = "admin123"
            hashed_password = get_password_hash(new_password)
            
            # 更新密码
            admin_user.hashed_password = hashed_password
            db.commit()
            
            print(f"已将admin用户的密码重置为 '{new_password}'")
        else:
            print("未找到admin用户")
    
    finally:
        db.close()


if __name__ == "__main__":
    # 确保数据库表已创建
    create_tables()
    
    # 修复admin密码
    fix_admin_password()
