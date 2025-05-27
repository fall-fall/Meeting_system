##
# @file database.py
# @brief 数据库模型和配置模块
# @details 定义了所有数据库模型、枚举类型和数据库连接配置
# @author Meeting System Team
# @date 2024
# @version 1.0
##

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from enum import Enum as PyEnum

from app.config import settings

##
# @brief SQLAlchemy数据库引擎
# @details 创建数据库连接引擎，配置了SQLite特有参数
##
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}  # SQLite特有的参数，允许多线程访问
)

##
# @brief 数据库会话工厂
# @details 用于创建数据库会话的工厂类
##
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

##
# @brief SQLAlchemy模型基类
# @details 所有数据库模型的基类
##
Base = declarative_base()

##
# @brief 获取数据库会话的依赖函数
# @details 用于FastAPI依赖注入，创建数据库会话并在请求结束时自动关闭
# @return Generator[数据库会话对象]
##
def get_db():
    db = SessionLocal()
    try:
        yield db  # 返回数据库会话
    finally:
        db.close()  # 确保会话被关闭


##
# @class User
# @brief 用户数据库模型
# @details 存储用户的基本信息，包括认证信息和权限设置
##
class User(Base):
    __tablename__ = "users"  ##< 数据库表名

    # 基本字段
    id = Column(Integer, primary_key=True, index=True)  # 用户ID，主键
    username = Column(String, unique=True, index=True)  # 用户名，唯一
    email = Column(String, unique=True, index=True)  # 电子邮箱，唯一
    hashed_password = Column(String)  # 哈希后的密码
    is_admin = Column(Boolean, default=False)  # 是否为管理员
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间

    # 关系定义
    conferences = relationship("Conference", back_populates="creator")  # 用户创建的会议
    registrations = relationship("Registration", back_populates="user")  # 用户参加的会议
    sent_friendships = relationship("Friendship", foreign_keys="Friendship.user_id", back_populates="user")  # 发起的好友关系
    received_friendships = relationship("Friendship", foreign_keys="Friendship.friend_id", back_populates="friend")  # 接收的好友关系
    notifications = relationship("Notification", foreign_keys="Notification.user_id", back_populates="user")  # 用户的通知


##
# @class Conference
# @brief 会议数据库模型
# @details 存储会议的基本信息，包括标题、描述、时间和地点
##
class Conference(Base):
    __tablename__ = "conferences"  ##< 数据库表名

    # 基本字段
    id = Column(Integer, primary_key=True, index=True)  # 会议ID，主键
    title = Column(String, index=True)  # 会议标题
    description = Column(Text)  # 会议描述
    date = Column(DateTime)  # 会议日期
    location = Column(String)  # 会议地点
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间
    creator_id = Column(Integer, ForeignKey("users.id"))  # 创建者ID，外键

    # 关系定义
    creator = relationship("User", back_populates="conferences")  # 会议创建者
    agenda_items = relationship("AgendaItem", back_populates="conference", cascade="all, delete-orphan")  # 会议议程项
    registrations = relationship("Registration", back_populates="conference", cascade="all, delete-orphan")  # 会议参与者


class AgendaItem(Base):
    """会议议程项模型"""
    __tablename__ = "agenda_items"  # 数据库表名

    # 基本字段
    id = Column(Integer, primary_key=True, index=True)  # 议程项ID，主键
    conference_id = Column(Integer, ForeignKey("conferences.id"))  # 所属会议ID，外键
    start_time = Column(String)  # 开始时间
    end_time = Column(String)  # 结束时间
    title = Column(String)  # 议程标题
    speaker = Column(String)  # 演讲者
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间

    # 关系定义
    conference = relationship("Conference", back_populates="agenda_items")  # 所属会议


class Registration(Base):
    """会议注册模型（用户参加会议的记录）"""
    __tablename__ = "registrations"  # 数据库表名

    # 基本字段
    id = Column(Integer, primary_key=True, index=True)  # 注册ID，主键
    user_id = Column(Integer, ForeignKey("users.id"))  # 用户ID，外键
    conference_id = Column(Integer, ForeignKey("conferences.id"))  # 会议ID，外键
    registered_at = Column(DateTime, default=datetime.utcnow)  # 注册时间

    # 关系定义
    user = relationship("User", back_populates="registrations")  # 参会用户
    conference = relationship("Conference", back_populates="registrations")  # 参加的会议


##
# @enum FriendshipStatus
# @brief 好友关系状态枚举
# @details 定义好友关系的各种状态
##
class FriendshipStatus(PyEnum):
    PENDING = "pending"  ##< 等待接受
    ACCEPTED = "accepted"  ##< 已接受
    REJECTED = "rejected"  ##< 已拒绝


##
# @enum NotificationType
# @brief 通知类型枚举
# @details 定义系统中各种通知类型
##
class NotificationType(PyEnum):
    FRIEND_REQUEST = "friend_request"  ##< 好友请求
    FRIEND_ACCEPTED = "friend_accepted"  ##< 好友请求已接受
    MEETING_INVITATION = "meeting_invitation"  ##< 会议邀请
    MEETING_JOINED = "meeting_joined"  ##< 已加入会议
    MEETING_LEFT = "meeting_left"  ##< 已退出会议


# 好友关系模型
class Friendship(Base):
    """好友关系模型"""
    __tablename__ = "friendships"  # 数据库表名

    # 基本字段
    id = Column(Integer, primary_key=True, index=True)  # 关系ID，主键
    user_id = Column(Integer, ForeignKey("users.id"))  # 发起者ID，外键
    friend_id = Column(Integer, ForeignKey("users.id"))  # 接收者ID，外键
    status = Column(Enum(FriendshipStatus), default=FriendshipStatus.PENDING)  # 关系状态
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # 更新时间

    # 关系定义
    user = relationship("User", foreign_keys=[user_id], back_populates="sent_friendships")  # 发起者
    friend = relationship("User", foreign_keys=[friend_id], back_populates="received_friendships")  # 接收者


# 通知模型
class Notification(Base):
    """通知模型"""
    __tablename__ = "notifications"  # 数据库表名

    # 基本字段
    id = Column(Integer, primary_key=True, index=True)  # 通知ID，主键
    user_id = Column(Integer, ForeignKey("users.id"))  # 接收者ID，外键
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # 发送者ID，外键，可为空
    type = Column(Enum(NotificationType))  # 通知类型
    content = Column(Text)  # 通知内容
    is_read = Column(Boolean, default=False)  # 是否已读
    related_id = Column(Integer, nullable=True)  # 相关ID，如会议ID或好友关系ID
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间

    # 关系定义
    user = relationship("User", foreign_keys=[user_id], back_populates="notifications")  # 接收者
    sender = relationship("User", foreign_keys=[sender_id])  # 发送者


##
# @brief 创建数据库表
# @details 使用SQLAlchemy创建所有定义的数据库表
##
def create_tables():
    Base.metadata.create_all(bind=engine)  # 使用SQLAlchemy创建所有定义的表
