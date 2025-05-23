# 数据库初始化脚本

from app.database import SessionLocal, create_tables
from app.crud import user as user_crud
from app.models.user import UserCreate


def init_db():
    """初始化数据库

    创建数据库表并添加默认数据（如管理员账号）
    """
    # 创建数据库表
    create_tables()

    # 创建数据库会话
    db = SessionLocal()

    try:
        # 检查管理员用户是否存在
        admin_user = user_crud.get_user_by_username(db, username="admin")
        if not admin_user:
            # 创建管理员用户
            admin = UserCreate(
                username="admin",  # 用户名
                email="admin@example.com",  # 电子邮箱
                password="admin123",  # 密码
                is_admin=True,  # 管理员权限
            )
            user_crud.create_user(db=db, user=admin)
            print("管理员用户创建成功。")
        else:
            print("管理员用户已存在。")
    finally:
        # 确保会话被关闭
        db.close()


# 如果直接运行此脚本，则执行初始化
if __name__ == "__main__":
    init_db()
