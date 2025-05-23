"""
列出所有用户及其管理员状态的脚本。
运行方式：python -m app.scripts.list_admin_users
"""

from sqlalchemy.orm import Session

from app.database import SessionLocal, create_tables
from app.crud import user as user_crud


def list_admin_users():
    """列出所有用户及其管理员状态。"""
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 获取所有用户
        users = user_crud.get_users(db)
        
        # 打印表头
        print("\n{:<5} {:<20} {:<30} {:<10}".format("ID", "用户名", "电子邮箱", "管理员"))
        print("-" * 70)
        
        # 打印用户信息
        admin_count = 0
        for user in users:
            is_admin = "是" if user.is_admin else "否"
            if user.is_admin:
                admin_count += 1
            print("{:<5} {:<20} {:<30} {:<10}".format(
                user.id, user.username, user.email, is_admin
            ))
        
        # 打印统计信息
        print("-" * 70)
        print(f"总用户数: {len(users)}")
        print(f"管理员用户数: {admin_count}")
        print(f"普通用户数: {len(users) - admin_count}")
    
    finally:
        db.close()


if __name__ == "__main__":
    # 确保数据库表已创建
    create_tables()
    
    # 列出管理员用户
    list_admin_users()
