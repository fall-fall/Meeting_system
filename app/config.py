##
# @file config.py
# @brief 应用程序配置模块
# @details 定义了应用程序的各项配置参数，包括数据库、认证等设置
# @author Meeting System Team
# @date 2024
# @version 1.0
##

from pydantic import BaseModel


##
# @class Settings
# @brief 应用程序设置类
# @details 使用Pydantic模型定义应用程序的所有配置参数
##
class Settings(BaseModel):

    ##
    # @brief 应用程序基本设置
    ##
    APP_NAME: str = "会议管理系统"  ##< 应用名称
    API_PREFIX: str = "/api"  ##< API前缀
    DEBUG: bool = True  ##< 调试模式

    ##
    # @brief 认证相关设置
    ##
    SECRET_KEY: str = "your-secret-key-for-jwt-token"  ##< JWT令牌的密钥（生产环境中应使用安全密钥）
    ALGORITHM: str = "HS256"  ##< 加密算法
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  ##< 访问令牌过期时间（1天）

    ##
    # @brief 数据库设置
    ##
    DATABASE_URL: str = "sqlite:///./meeting_management.db"  ##< 数据库URL


##
# @brief 全局设置实例
# @details 应用程序中使用的全局配置对象
##
settings = Settings()
