# 会议管理系统 API 文档

## 📋 目录

- [项目概述](#项目概述)
- [系统架构](#系统架构)
- [核心模块](#核心模块)
  - [配置模块 (app.config)](#配置模块-appconfig)
  - [数据库模块 (app.database)](#数据库模块-appdatabase)
  - [数据模型 (app.models)](#数据模型-appmodels)
  - [数据库操作 (app.crud)](#数据库操作-appcrud)
  - [路由处理 (app.routers)](#路由处理-approuters)
- [数据库模型详解](#数据库模型详解)
- [API 接口说明](#api-接口说明)
- [工具脚本](#工具脚本)

---

## 项目概述

**会议管理系统**是一个基于 FastAPI 构建的现代化 Web 应用程序，提供完整的会议管理功能，包括：

- 🔐 用户认证与权限管理
- 📅 会议创建与管理
- 👥 用户好友系统
- 📝 会议注册与参与
- 🔔 实时通知系统
- 📋 会议议程管理

### 技术栈

- **后端框架**: FastAPI
- **数据库**: SQLite (支持其他关系型数据库)
- **ORM**: SQLAlchemy
- **认证**: JWT Token
- **模板引擎**: Jinja2
- **前端**: HTML + CSS + JavaScript

---

## 系统架构

```
Meeting_system/
├── app/
│   ├── main.py              # 应用程序入口点
│   ├── config.py            # 配置管理
│   ├── database.py          # 数据库模型定义
│   ├── dependencies.py      # 依赖注入
│   ├── init_db.py          # 数据库初始化
│   ├── models/             # Pydantic 数据模型
│   ├── crud/               # 数据库操作
│   ├── routers/            # API 路由
│   ├── templates/          # HTML 模板
│   ├── static/             # 静态文件
│   └── scripts/            # 工具脚本
├── docs/                   # 生成的文档
├── run.py                  # 启动脚本
└── README.md              # 项目说明
```

---

## 核心模块

### 配置模块 (app.config)

#### Settings 类

应用程序的核心配置类，使用 Pydantic 进行配置管理：

```python
class Settings(BaseModel):
    # 应用程序基本设置
    APP_NAME: str = "会议管理系统"
    API_PREFIX: str = "/api"
    DEBUG: bool = True
    
    # 认证相关设置
    SECRET_KEY: str = "your-secret-key-for-jwt-token"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    
    # 数据库设置
    DATABASE_URL: str = "sqlite:///./meeting_management.db"
```

**主要配置项：**
- `APP_NAME`: 应用程序名称
- `API_PREFIX`: API 路由前缀
- `SECRET_KEY`: JWT 令牌加密密钥
- `DATABASE_URL`: 数据库连接字符串

---

### 数据库模块 (app.database)

#### 核心函数

##### `get_db()`
- **功能**: 获取数据库会话的依赖函数
- **用途**: FastAPI 依赖注入，自动管理数据库连接
- **返回**: 数据库会话对象

##### `create_tables()`
- **功能**: 创建所有数据库表
- **用途**: 应用程序初始化时创建数据库结构

#### 数据库模型

##### User (用户模型)
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
```

##### Conference (会议模型)
```python
class Conference(Base):
    __tablename__ = "conferences"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    date = Column(DateTime)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    creator_id = Column(Integer, ForeignKey("users.id"))
```

##### AgendaItem (议程项模型)
```python
class AgendaItem(Base):
    __tablename__ = "agenda_items"
    
    id = Column(Integer, primary_key=True, index=True)
    conference_id = Column(Integer, ForeignKey("conferences.id"))
    start_time = Column(String)
    end_time = Column(String)
    title = Column(String)
    speaker = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
```

##### Registration (注册模型)
```python
class Registration(Base):
    __tablename__ = "registrations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    conference_id = Column(Integer, ForeignKey("conferences.id"))
    registered_at = Column(DateTime, default=datetime.utcnow)
```

##### Friendship (好友关系模型)
```python
class Friendship(Base):
    __tablename__ = "friendships"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    friend_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum(FriendshipStatus), default=FriendshipStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

##### Notification (通知模型)
```python
class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    type = Column(Enum(NotificationType))
    content = Column(Text)
    is_read = Column(Boolean, default=False)
    related_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
```

#### 枚举类型

##### FriendshipStatus (好友关系状态)
- `PENDING`: 等待接受
- `ACCEPTED`: 已接受
- `REJECTED`: 已拒绝

##### NotificationType (通知类型)
- `FRIEND_REQUEST`: 好友请求
- `FRIEND_ACCEPTED`: 好友请求已接受
- `MEETING_INVITATION`: 会议邀请
- `MEETING_JOINED`: 已加入会议
- `MEETING_LEFT`: 已退出会议

---

### 数据模型 (app.models)

#### 用户相关模型

##### UserBase
```python
class UserBase(BaseModel):
    username: str  # 用户名
    email: str     # 电子邮箱
```

##### UserCreate
```python
class UserCreate(UserBase):
    password: str           # 密码
    is_admin: bool = False  # 是否为管理员
```

##### UserLogin
```python
class UserLogin(BaseModel):
    username: str  # 用户名
    password: str  # 密码
```

##### UserResponse
```python
class UserResponse(UserBase):
    id: int                    # 用户ID
    is_admin: bool            # 是否为管理员
    created_at: datetime      # 创建时间
    
    class Config:
        orm_mode = True
```

##### Token
```python
class Token(BaseModel):
    access_token: str  # 访问令牌
    token_type: str    # 令牌类型
```

#### 会议相关模型

##### ConferenceBase
```python
class ConferenceBase(BaseModel):
    title: str              # 会议标题
    description: str        # 会议描述
    date: datetime         # 会议日期
    location: str          # 会议地点
```

##### ConferenceCreate
```python
class ConferenceCreate(ConferenceBase):
    pass
```

##### ConferenceResponse
```python
class ConferenceResponse(ConferenceBase):
    id: int                           # 会议ID
    creator_id: int                   # 创建者ID
    created_at: datetime             # 创建时间
    agenda_items: List[AgendaItemResponse] = []  # 议程项列表
    
    class Config:
        orm_mode = True
```

---

### 数据库操作 (app.crud)

#### 用户操作 (app.crud.user)

##### 主要函数

- `get_user(db, user_id)`: 根据ID获取用户
- `get_user_by_username(db, username)`: 根据用户名获取用户
- `get_user_by_email(db, email)`: 根据邮箱获取用户
- `get_users(db, skip, limit)`: 获取用户列表
- `create_user(db, user)`: 创建新用户

#### 会议操作 (app.crud.conference)

##### 主要函数

- `get_conference(db, conference_id)`: 根据ID获取会议
- `get_conferences(db, skip, limit)`: 获取会议列表
- `get_conferences_by_creator(db, creator_id, skip, limit)`: 获取用户创建的会议
- `create_conference(db, conference, creator_id)`: 创建新会议
- `update_conference(db, conference_id, conference)`: 更新会议
- `delete_conference(db, conference_id)`: 删除会议
- `create_agenda_item(db, agenda_item, conference_id)`: 创建议程项
- `get_agenda_items(db, conference_id)`: 获取会议议程
- `delete_agenda_item(db, agenda_item_id)`: 删除议程项
- `get_upcoming_conferences(db, skip, limit)`: 获取即将举行的会议

#### 注册操作 (app.crud.registration)

##### 主要函数

- `get_registration(db, registration_id)`: 根据ID获取注册记录
- `get_registration_by_user_and_conference(db, user_id, conference_id)`: 获取用户会议注册记录
- `get_registrations_by_user(db, user_id, skip, limit)`: 获取用户的注册记录
- `get_registrations_by_conference(db, conference_id, skip, limit)`: 获取会议的注册记录
- `create_registration(db, registration, user_id)`: 创建注册记录
- `delete_registration(db, registration_id)`: 删除注册记录

#### 好友操作 (app.crud.friendship)

##### 主要函数

- `get_friendship(db, friendship_id)`: 根据ID获取好友关系
- `get_friendship_by_users(db, user_id, friend_id)`: 获取两用户间的好友关系
- `get_friendships_by_user(db, user_id, status)`: 获取用户的好友关系
- `get_friends(db, user_id)`: 获取用户的好友列表
- `get_pending_friend_requests(db, user_id)`: 获取待处理的好友请求
- `create_friendship(db, user_id, friend_id)`: 创建好友关系
- `update_friendship_status(db, friendship_id, status)`: 更新好友关系状态
- `delete_friendship(db, friendship_id)`: 删除好友关系

#### 通知操作 (app.crud.notification)

##### 主要函数

- `get_notification(db, notification_id)`: 获取通知
- `get_notifications_by_user(db, user_id, skip, limit, unread_only)`: 获取用户通知
- `create_notification(db, user_id, type, content, sender_id, related_id)`: 创建通知
- `mark_notification_as_read(db, notification_id)`: 标记通知为已读
- `mark_all_notifications_as_read(db, user_id)`: 标记所有通知为已读
- `delete_notification(db, notification_id)`: 删除通知
- `get_unread_notification_count(db, user_id)`: 获取未读通知数量

---

### 路由处理 (app.routers)

#### 认证路由 (app.routers.auth)

**功能**: 处理用户认证相关的请求

**主要端点**:
- `POST /api/register`: 用户注册
- `POST /api/login`: 用户登录
- `GET /api/logout`: 用户登出
- `GET /api/me`: 获取当前用户信息

#### 会议路由 (app.routers.conferences)

**功能**: 处理会议管理相关的请求

**主要端点**:
- `GET /api/conferences`: 获取会议列表
- `POST /api/conferences`: 创建新会议
- `GET /api/conferences/{conference_id}`: 获取会议详情
- `PUT /api/conferences/{conference_id}`: 更新会议
- `DELETE /api/conferences/{conference_id}`: 删除会议
- `POST /api/conferences/{conference_id}/agenda`: 添加议程项
- `DELETE /api/agenda/{agenda_id}`: 删除议程项

#### 注册路由 (app.routers.registrations)

**功能**: 处理会议注册相关的请求

**主要端点**:
- `POST /api/conferences/{conference_id}/register`: 注册参加会议
- `DELETE /api/registrations/{registration_id}`: 取消注册
- `GET /api/conferences/{conference_id}/participants`: 获取会议参与者

#### 好友路由 (app.routers.friends)

**功能**: 处理好友关系相关的请求

**主要端点**:
- `GET /api/friends`: 获取好友列表
- `POST /api/friends/request`: 发送好友请求
- `PUT /api/friends/{friendship_id}/accept`: 接受好友请求
- `PUT /api/friends/{friendship_id}/reject`: 拒绝好友请求
- `DELETE /api/friends/{friendship_id}`: 删除好友关系

#### 通知路由 (app.routers.notifications)

**功能**: 处理通知相关的请求

**主要端点**:
- `GET /api/notifications`: 获取通知列表
- `PUT /api/notifications/{notification_id}/read`: 标记通知为已读
- `PUT /api/notifications/read-all`: 标记所有通知为已读
- `DELETE /api/notifications/{notification_id}`: 删除通知

---

## 工具脚本

系统提供了多个实用的管理脚本：

### 用户管理脚本

#### `delete_users.py`
- **功能**: 删除指定用户
- **运行方式**: `python -m app.scripts.delete_users`

#### `fix_admin_password.py`
- **功能**: 重置admin用户密码为admin123
- **运行方式**: `python -m app.scripts.fix_admin_password`

#### `list_admin_users.py`
- **功能**: 列出所有用户及其管理员状态
- **运行方式**: `python -m app.scripts.list_admin_users`

#### `update_all_passwords.py`
- **功能**: 更新所有用户密码
- **运行方式**: `python -m app.scripts.update_all_passwords`

### 数据生成脚本

#### `generate_demo_users.py`
- **功能**: 生成示例用户数据
- **运行方式**: `python -m app.scripts.generate_demo_users`

#### `generate_demo_data.py`
- **功能**: 生成示例数据（会议、好友关系、通知）
- **运行方式**: `python -m app.scripts.generate_demo_data`

#### `generate_invitations.py`
- **功能**: 生成会议邀请通知
- **运行方式**: `python -m app.scripts.generate_invitations`

---

## API 接口说明

### 认证机制

系统使用 JWT (JSON Web Token) 进行用户认证：

1. 用户登录后获得访问令牌
2. 后续请求需在 Header 中携带令牌
3. 令牌格式: `Authorization: Bearer <token>`
4. 令牌有效期: 24小时

### 响应格式

所有 API 响应都遵循统一的格式：

```json
{
    "success": true,
    "data": {...},
    "message": "操作成功"
}
```

### 错误处理

系统提供详细的错误信息：

```json
{
    "success": false,
    "error": "错误类型",
    "message": "详细错误信息",
    "details": {...}
}
```

### 分页参数

列表接口支持分页查询：

- `skip`: 跳过的记录数（默认: 0）
- `limit`: 返回的最大记录数（默认: 100）

---

## 部署说明

### 开发环境

1. 安装依赖: `pip install -r requirements.txt`
2. 启动应用: `python run.py`
3. 访问地址: `http://localhost:8010`

### 生产环境

1. 配置环境变量
2. 使用 WSGI 服务器（如 Gunicorn）
3. 配置反向代理（如 Nginx）
4. 设置 HTTPS

---

## 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

---

*本文档由 Doxygen 和 moxygen 自动生成，最后更新时间: 2024年5月27日*
