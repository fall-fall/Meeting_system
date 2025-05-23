from pydantic import BaseModel


class Settings(BaseModel):
    """应用程序设置类"""

    # 应用程序基本设置
    APP_NAME: str = "会议管理系统"  # 应用名称
    API_PREFIX: str = "/api"  # API前缀
    DEBUG: bool = True  # 调试模式

    # 认证相关设置
    SECRET_KEY: str = "your-secret-key-for-jwt-token"  # JWT令牌的密钥（生产环境中应使用安全密钥）
    ALGORITHM: str = "HS256"  # 加密算法
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 访问令牌过期时间（1天）

    # 数据库设置
    DATABASE_URL: str = "sqlite:///./meeting_management.db"  # 数据库URL


# 创建全局设置实例
settings = Settings()
