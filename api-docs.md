# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`app::config`](#namespaceapp_1_1config) | 
`namespace `[`app::crud::conference`](#namespaceapp_1_1crud_1_1conference) | 会议数据库操作模块
`namespace `[`app::crud::friendship`](#namespaceapp_1_1crud_1_1friendship) | 好友关系数据库操作模块
`namespace `[`app::crud::notification`](#namespaceapp_1_1crud_1_1notification) | 
`namespace `[`app::crud::registration`](#namespaceapp_1_1crud_1_1registration) | 会议注册数据库操作模块
`namespace `[`app::crud::user`](#namespaceapp_1_1crud_1_1user) | 用户数据库操作模块
`namespace `[`app::database`](#namespaceapp_1_1database) | 
`namespace `[`app::dependencies`](#namespaceapp_1_1dependencies) | 
`namespace `[`app::init_db`](#namespaceapp_1_1init__db) | 
`namespace `[`app::main`](#namespaceapp_1_1main) | 
`namespace `[`app::models::conference`](#namespaceapp_1_1models_1_1conference) | 会议和议程项相关的数据模型
`namespace `[`app::models::friendship`](#namespaceapp_1_1models_1_1friendship) | 好友关系相关的数据模型
`namespace `[`app::models::notification`](#namespaceapp_1_1models_1_1notification) | 通知相关的数据模型
`namespace `[`app::models::registration`](#namespaceapp_1_1models_1_1registration) | 会议注册相关的数据模型
`namespace `[`app::models::user`](#namespaceapp_1_1models_1_1user) | 
`namespace `[`app::routers::auth`](#namespaceapp_1_1routers_1_1auth) | 认证相关的路由处理模块
`namespace `[`app::routers::conferences`](#namespaceapp_1_1routers_1_1conferences) | 会议相关的路由处理模块
`namespace `[`app::routers::friends`](#namespaceapp_1_1routers_1_1friends) | 
`namespace `[`app::routers::my_conferences`](#namespaceapp_1_1routers_1_1my__conferences) | 
`namespace `[`app::routers::notifications`](#namespaceapp_1_1routers_1_1notifications) | 
`namespace `[`app::routers::registrations`](#namespaceapp_1_1routers_1_1registrations) | 
`namespace `[`delete_users`](#namespacedelete__users) | 删除指定用户的脚本。 运行方式：python -m app.scripts.delete_users
`namespace `[`fix_admin_password`](#namespacefix__admin__password) | 将admin用户的密码重置为admin123的脚本。 运行方式：python -m app.scripts.fix_admin_password
`namespace `[`generate_demo_data`](#namespacegenerate__demo__data) | 生成示例数据的脚本，包括会议、好友关系和通知。 运行方式：python -m app.scripts.generate_demo_data
`namespace `[`generate_demo_users`](#namespacegenerate__demo__users) | 生成示例用户的脚本。 运行方式：python -m app.scripts.generate_demo_users
`namespace `[`generate_invitations`](#namespacegenerate__invitations) | 生成会议邀请通知的脚本。 运行方式：python -m app.scripts.generate_invitations
`namespace `[`list_admin_users`](#namespacelist__admin__users) | 列出所有用户及其管理员状态的脚本。 运行方式：python -m app.scripts.list_admin_users
`namespace `[`update_all_passwords`](#namespaceupdate__all__passwords) | 更新所有用户密码的脚本。 运行方式：python -m app.scripts.update_all_passwords
`class `[`app::models::conference::AgendaItemResponse::Config`](#classapp_1_1models_1_1conference_1_1_agenda_item_response_1_1_config) | 
`class `[`app::models::conference::ConferenceResponse::Config`](#classapp_1_1models_1_1conference_1_1_conference_response_1_1_config) | 
`class `[`app::models::friendship::FriendResponse::Config`](#classapp_1_1models_1_1friendship_1_1_friend_response_1_1_config) | 
`class `[`app::models::friendship::FriendshipResponse::Config`](#classapp_1_1models_1_1friendship_1_1_friendship_response_1_1_config) | 
`class `[`app::models::notification::NotificationResponse::Config`](#classapp_1_1models_1_1notification_1_1_notification_response_1_1_config) | 
`class `[`app::models::registration::RegistrationResponse::Config`](#classapp_1_1models_1_1registration_1_1_registration_response_1_1_config) | 
`class `[`app::models::registration::UserRegistrationResponse::Config`](#classapp_1_1models_1_1registration_1_1_user_registration_response_1_1_config) | 
`class `[`app::models::user::UserResponse::Config`](#classapp_1_1models_1_1user_1_1_user_response_1_1_config) | 用户ID

# namespace `app::config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`app::config::Settings`](#classapp_1_1config_1_1_settings) | 应用程序设置类

# class `app::config::Settings` 

```
class app::config::Settings
  : public BaseModel
```  

应用程序设置类

使用Pydantic模型定义应用程序的所有配置参数

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `app::crud::conference` 

会议数据库操作模块

本模块提供会议和议程项相关的数据库CRUD操作函数

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`get_conference`](#namespaceapp_1_1crud_1_1conference_1aea884062eeb5cd7d05b02f2a1ca0329b)`(Session db,int conference_id)`            | 根据ID获取会议
`public  `[`get_conferences`](#namespaceapp_1_1crud_1_1conference_1a7b008e31486fa505559fe1ff5eff165a)`(Session db,int skip,int limit)`            | 获取所有会议
`public  `[`get_conferences_by_creator`](#namespaceapp_1_1crud_1_1conference_1ae104a904decd6c7ddbc876115e0a3090)`(Session db,int creator_id,int skip,int limit)`            | 根据创建者ID获取会议
`public  `[`create_conference`](#namespaceapp_1_1crud_1_1conference_1a29060124eb2ecfafb657f79d1ebcf6eb)`(Session db,`[`ConferenceCreate`](#classapp_1_1models_1_1conference_1_1_conference_create)` conference,int creator_id)`            | 创建新会议
`public  `[`update_conference`](#namespaceapp_1_1crud_1_1conference_1acffbc05ae2103ae3c4997ca1d0dedd41)`(Session db,int conference_id,`[`ConferenceUpdate`](#classapp_1_1models_1_1conference_1_1_conference_update)` conference)`            | 更新会议
`public  `[`delete_conference`](#namespaceapp_1_1crud_1_1conference_1ae5b06751313084e1fb9a3354d1e9de1d)`(Session db,int conference_id)`            | 删除会议
`public  `[`create_agenda_item`](#namespaceapp_1_1crud_1_1conference_1a3676c275fd2008435ec100c754e7076e)`(Session db,`[`AgendaItemCreate`](#classapp_1_1models_1_1conference_1_1_agenda_item_create)` agenda_item,int conference_id)`            | 创建新议程项
`public  `[`get_agenda_items`](#namespaceapp_1_1crud_1_1conference_1ab940be8b87bd00804d652a31b5eb1675)`(Session db,int conference_id)`            | 获取会议的议程项
`public  `[`delete_agenda_item`](#namespaceapp_1_1crud_1_1conference_1a6507ed4cdc1d66a237bc6644533283ea)`(Session db,int agenda_item_id)`            | 删除议程项
`public  `[`get_upcoming_conferences`](#namespaceapp_1_1crud_1_1conference_1ac333a986c83db46f58fa3ee9a19e0460)`(Session db,int skip,int limit)`            | 获取即将举行的会议

## Members

#### `public  `[`get_conference`](#namespaceapp_1_1crud_1_1conference_1aea884062eeb5cd7d05b02f2a1ca0329b)`(Session db,int conference_id)` 

根据ID获取会议

Args: db: 数据库会话 conference_id: 会议ID

Returns: [Conference](#classapp_1_1database_1_1_conference): 会议对象，如果不存在则返回None

#### `public  `[`get_conferences`](#namespaceapp_1_1crud_1_1conference_1a7b008e31486fa505559fe1ff5eff165a)`(Session db,int skip,int limit)` 

获取所有会议

Args: db: 数据库会话 skip: 跳过的记录数 limit: 返回的最大记录数

Returns: List[[Conference](#classapp_1_1database_1_1_conference)]: 会议对象列表

#### `public  `[`get_conferences_by_creator`](#namespaceapp_1_1crud_1_1conference_1ae104a904decd6c7ddbc876115e0a3090)`(Session db,int creator_id,int skip,int limit)` 

根据创建者ID获取会议

Args: db: 数据库会话 creator_id: 创建者ID skip: 跳过的记录数 limit: 返回的最大记录数

Returns: List[[Conference](#classapp_1_1database_1_1_conference)]: 会议对象列表，按日期降序排序

#### `public  `[`create_conference`](#namespaceapp_1_1crud_1_1conference_1a29060124eb2ecfafb657f79d1ebcf6eb)`(Session db,`[`ConferenceCreate`](#classapp_1_1models_1_1conference_1_1_conference_create)` conference,int creator_id)` 

创建新会议

Args: db: 数据库会话 conference: 会议创建模型 creator_id: 创建者ID

Returns: [Conference](#classapp_1_1database_1_1_conference): 创建的会议对象

#### `public  `[`update_conference`](#namespaceapp_1_1crud_1_1conference_1acffbc05ae2103ae3c4997ca1d0dedd41)`(Session db,int conference_id,`[`ConferenceUpdate`](#classapp_1_1models_1_1conference_1_1_conference_update)` conference)` 

更新会议

Args: db: 数据库会话 conference_id: 会议ID conference: 会议更新模型

Returns: [Conference](#classapp_1_1database_1_1_conference): 更新后的会议对象，如果不存在则返回None

#### `public  `[`delete_conference`](#namespaceapp_1_1crud_1_1conference_1ae5b06751313084e1fb9a3354d1e9de1d)`(Session db,int conference_id)` 

删除会议

Args: db: 数据库会话 conference_id: 会议ID

Returns: [Conference](#classapp_1_1database_1_1_conference): 被删除的会议对象，如果不存在则返回None

#### `public  `[`create_agenda_item`](#namespaceapp_1_1crud_1_1conference_1a3676c275fd2008435ec100c754e7076e)`(Session db,`[`AgendaItemCreate`](#classapp_1_1models_1_1conference_1_1_agenda_item_create)` agenda_item,int conference_id)` 

创建新议程项

Args: db: 数据库会话 agenda_item: 议程项创建模型 conference_id: 所属会议ID

Returns: [AgendaItem](#classapp_1_1database_1_1_agenda_item): 创建的议程项对象

#### `public  `[`get_agenda_items`](#namespaceapp_1_1crud_1_1conference_1ab940be8b87bd00804d652a31b5eb1675)`(Session db,int conference_id)` 

获取会议的议程项

Args: db: 数据库会话 conference_id: 会议ID

Returns: List[[AgendaItem](#classapp_1_1database_1_1_agenda_item)]: 议程项对象列表

#### `public  `[`delete_agenda_item`](#namespaceapp_1_1crud_1_1conference_1a6507ed4cdc1d66a237bc6644533283ea)`(Session db,int agenda_item_id)` 

删除议程项

Args: db: 数据库会话 agenda_item_id: 议程项ID

Returns: [AgendaItem](#classapp_1_1database_1_1_agenda_item): 被删除的议程项对象，如果不存在则返回None

#### `public  `[`get_upcoming_conferences`](#namespaceapp_1_1crud_1_1conference_1ac333a986c83db46f58fa3ee9a19e0460)`(Session db,int skip,int limit)` 

获取即将举行的会议

Args: db: 数据库会话 skip: 跳过的记录数 limit: 返回的最大记录数

Returns: List[[Conference](#classapp_1_1database_1_1_conference)]: 会议对象列表，按日期升序排序

# namespace `app::crud::friendship` 

好友关系数据库操作模块

本模块提供好友关系相关的数据库CRUD操作函数

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`get_friendship`](#namespaceapp_1_1crud_1_1friendship_1acef68670d9425ca3afefff58d2dbff63)`(Session db,int friendship_id)`            | 根据ID获取好友关系
`public  `[`get_friendship_by_users`](#namespaceapp_1_1crud_1_1friendship_1a2b8cd4fb3bcd59ff88270c64e1507fc1)`(Session db,int user_id,int friend_id)`            | 获取两个用户之间的好友关系
`public  `[`get_friendships_by_user`](#namespaceapp_1_1crud_1_1friendship_1a8cdf22a94668df2675d72be9170afa42)`(Session db,int user_id,`[`FriendshipStatus`](#classapp_1_1database_1_1_friendship_status)` status)`            | 获取用户的所有好友关系
`public  `[`get_friends`](#namespaceapp_1_1crud_1_1friendship_1a5702721bd79372a8cc7d2239ca542abc)`(Session db,int user_id)`            | 获取用户的所有好友
`public  `[`get_pending_friend_requests`](#namespaceapp_1_1crud_1_1friendship_1aded65d272569b05221b0c0e953a5dcd7)`(Session db,int user_id)`            | 获取用户收到的待处理好友请求
`public  `[`create_friendship`](#namespaceapp_1_1crud_1_1friendship_1af9a1e1cc4050d08de99d2450ffaa52f4)`(Session db,int user_id,int friend_id)`            | 创建好友关系
`public  `[`update_friendship_status`](#namespaceapp_1_1crud_1_1friendship_1a24da2bc223a62c78cd67018e2f687e88)`(Session db,int friendship_id,`[`FriendshipStatus`](#classapp_1_1database_1_1_friendship_status)` status)`            | 更新好友关系状态
`public  `[`delete_friendship`](#namespaceapp_1_1crud_1_1friendship_1a0f72a1e212471d19cf6830c8a16e5cce)`(Session db,int friendship_id)`            | 删除好友关系

## Members

#### `public  `[`get_friendship`](#namespaceapp_1_1crud_1_1friendship_1acef68670d9425ca3afefff58d2dbff63)`(Session db,int friendship_id)` 

根据ID获取好友关系

Args: db: 数据库会话 friendship_id: 好友关系ID

Returns: [Friendship](#classapp_1_1database_1_1_friendship): 好友关系对象，如果不存在则返回None

#### `public  `[`get_friendship_by_users`](#namespaceapp_1_1crud_1_1friendship_1a2b8cd4fb3bcd59ff88270c64e1507fc1)`(Session db,int user_id,int friend_id)` 

获取两个用户之间的好友关系

Args: db: 数据库会话 user_id: 用户ID friend_id: 好友ID

Returns: [Friendship](#classapp_1_1database_1_1_friendship): 好友关系对象，如果不存在则返回None

Note: 此函数会查找两个用户之间的好友关系，无论谁是发起者

#### `public  `[`get_friendships_by_user`](#namespaceapp_1_1crud_1_1friendship_1a8cdf22a94668df2675d72be9170afa42)`(Session db,int user_id,`[`FriendshipStatus`](#classapp_1_1database_1_1_friendship_status)` status)` 

获取用户的所有好友关系

Args: db: 数据库会话 user_id: 用户ID status: 好友关系状态（可选）

Returns: List[[Friendship](#classapp_1_1database_1_1_friendship)]: 好友关系对象列表

#### `public  `[`get_friends`](#namespaceapp_1_1crud_1_1friendship_1a5702721bd79372a8cc7d2239ca542abc)`(Session db,int user_id)` 

获取用户的所有好友

Args: db: 数据库会话 user_id: 用户ID

Returns: List[[User](#classapp_1_1database_1_1_user)]: 好友用户对象列表

#### `public  `[`get_pending_friend_requests`](#namespaceapp_1_1crud_1_1friendship_1aded65d272569b05221b0c0e953a5dcd7)`(Session db,int user_id)` 

获取用户收到的待处理好友请求

Args: db: 数据库会话 user_id: 用户ID

Returns: List[[Friendship](#classapp_1_1database_1_1_friendship)]: 待处理好友请求列表

#### `public  `[`create_friendship`](#namespaceapp_1_1crud_1_1friendship_1af9a1e1cc4050d08de99d2450ffaa52f4)`(Session db,int user_id,int friend_id)` 

创建好友关系

Args: db: 数据库会话 user_id: 发起者用户ID friend_id: 接收者用户ID

Returns: [Friendship](#classapp_1_1database_1_1_friendship): 创建或已存在的好友关系对象

#### `public  `[`update_friendship_status`](#namespaceapp_1_1crud_1_1friendship_1a24da2bc223a62c78cd67018e2f687e88)`(Session db,int friendship_id,`[`FriendshipStatus`](#classapp_1_1database_1_1_friendship_status)` status)` 

更新好友关系状态

Args: db: 数据库会话 friendship_id: 好友关系ID status: 新的状态

Returns: [Friendship](#classapp_1_1database_1_1_friendship): 更新后的好友关系对象，如果不存在则返回None

#### `public  `[`delete_friendship`](#namespaceapp_1_1crud_1_1friendship_1a0f72a1e212471d19cf6830c8a16e5cce)`(Session db,int friendship_id)` 

删除好友关系

Args: db: 数据库会话 friendship_id: 好友关系ID

Returns: [Friendship](#classapp_1_1database_1_1_friendship): 被删除的好友关系对象，如果不存在则返回None

# namespace `app::crud::notification` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`get_notification`](#crud_2notification_8py_1adb7aee39d3d257e4bef689e61afe0a25)`(Session db,int notification_id)`            | 获取通知。
`public  `[`get_notifications_by_user`](#crud_2notification_8py_1aba34281f840d1c11b151e2242d376b5d)`(Session db,int user_id,int skip,int limit,bool unread_only)`            | 获取用户的通知。
`public  `[`create_notification`](#crud_2notification_8py_1afe46f4a35e67db17e04f4844893e88a2)`(Session db,int user_id,`[`NotificationType`](#classapp_1_1database_1_1_notification_type)` type,str content,int sender_id,int related_id)`            | 创建通知。
`public  `[`mark_notification_as_read`](#crud_2notification_8py_1aaab0c2fedd977234f7433ca9de4ffd0b)`(Session db,int notification_id)`            | 将通知标记为已读。
`public  `[`mark_all_notifications_as_read`](#crud_2notification_8py_1a09d92b03c5fd48d247c64ec941bfa568)`(Session db,int user_id)`            | 将用户的所有通知标记为已读。
`public  `[`delete_notification`](#crud_2notification_8py_1a319558e8a6165a2d331e053ae8b9bb90)`(Session db,int notification_id)`            | 删除通知。
`public  `[`get_unread_notification_count`](#crud_2notification_8py_1a2812c619781e66a340a88871675fa64e)`(Session db,int user_id)`            | 获取用户未读通知数量。

## Members

#### `public  `[`get_notification`](#crud_2notification_8py_1adb7aee39d3d257e4bef689e61afe0a25)`(Session db,int notification_id)` 

获取通知。

#### `public  `[`get_notifications_by_user`](#crud_2notification_8py_1aba34281f840d1c11b151e2242d376b5d)`(Session db,int user_id,int skip,int limit,bool unread_only)` 

获取用户的通知。

#### `public  `[`create_notification`](#crud_2notification_8py_1afe46f4a35e67db17e04f4844893e88a2)`(Session db,int user_id,`[`NotificationType`](#classapp_1_1database_1_1_notification_type)` type,str content,int sender_id,int related_id)` 

创建通知。

#### `public  `[`mark_notification_as_read`](#crud_2notification_8py_1aaab0c2fedd977234f7433ca9de4ffd0b)`(Session db,int notification_id)` 

将通知标记为已读。

#### `public  `[`mark_all_notifications_as_read`](#crud_2notification_8py_1a09d92b03c5fd48d247c64ec941bfa568)`(Session db,int user_id)` 

将用户的所有通知标记为已读。

#### `public  `[`delete_notification`](#crud_2notification_8py_1a319558e8a6165a2d331e053ae8b9bb90)`(Session db,int notification_id)` 

删除通知。

#### `public  `[`get_unread_notification_count`](#crud_2notification_8py_1a2812c619781e66a340a88871675fa64e)`(Session db,int user_id)` 

获取用户未读通知数量。

# namespace `app::crud::registration` 

会议注册数据库操作模块

本模块提供会议注册相关的数据库CRUD操作函数

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`get_registration`](#namespaceapp_1_1crud_1_1registration_1a16f43f64b5220bd81ff7df2d3fe73b7a)`(Session db,int registration_id)`            | 根据ID获取注册记录
`public  `[`get_registration_by_user_and_conference`](#namespaceapp_1_1crud_1_1registration_1ab63e8855114d554c10ec29e10cf73f4e)`(Session db,int user_id,int conference_id)`            | 根据用户ID和会议ID获取注册记录
`public  `[`get_registrations_by_user`](#namespaceapp_1_1crud_1_1registration_1a9c4071c19b46210a3ff0b48c9c3b30f0)`(Session db,int user_id,int skip,int limit)`            | 根据用户ID获取注册记录列表
`public  `[`get_registrations_by_conference`](#namespaceapp_1_1crud_1_1registration_1adeb0bb7dcdfa79f3aa34d6ac56e6a98c)`(Session db,int conference_id,int skip,int limit)`            | 根据会议ID获取注册记录列表
`public  `[`create_registration`](#namespaceapp_1_1crud_1_1registration_1a20733d661f9a082b648c0c6d881ebcbd)`(Session db,`[`RegistrationCreate`](#classapp_1_1models_1_1registration_1_1_registration_create)` registration,int user_id)`            | 创建新的注册记录
`public  `[`delete_registration`](#namespaceapp_1_1crud_1_1registration_1ab93378fa05b214f93587d122761be3eb)`(Session db,int registration_id)`            | 删除注册记录

## Members

#### `public  `[`get_registration`](#namespaceapp_1_1crud_1_1registration_1a16f43f64b5220bd81ff7df2d3fe73b7a)`(Session db,int registration_id)` 

根据ID获取注册记录

Args: db: 数据库会话 registration_id: 注册记录ID

Returns: [Registration](#classapp_1_1database_1_1_registration): 注册记录对象，如果不存在则返回None

#### `public  `[`get_registration_by_user_and_conference`](#namespaceapp_1_1crud_1_1registration_1ab63e8855114d554c10ec29e10cf73f4e)`(Session db,int user_id,int conference_id)` 

根据用户ID和会议ID获取注册记录

Args: db: 数据库会话 user_id: 用户ID conference_id: 会议ID

Returns: [Registration](#classapp_1_1database_1_1_registration): 注册记录对象，如果不存在则返回None

#### `public  `[`get_registrations_by_user`](#namespaceapp_1_1crud_1_1registration_1a9c4071c19b46210a3ff0b48c9c3b30f0)`(Session db,int user_id,int skip,int limit)` 

根据用户ID获取注册记录列表

Args: db: 数据库会话 user_id: 用户ID skip: 跳过的记录数 limit: 返回的最大记录数

Returns: List[[Registration](#classapp_1_1database_1_1_registration)]: 注册记录对象列表

#### `public  `[`get_registrations_by_conference`](#namespaceapp_1_1crud_1_1registration_1adeb0bb7dcdfa79f3aa34d6ac56e6a98c)`(Session db,int conference_id,int skip,int limit)` 

根据会议ID获取注册记录列表

Args: db: 数据库会话 conference_id: 会议ID skip: 跳过的记录数 limit: 返回的最大记录数

Returns: List[[Registration](#classapp_1_1database_1_1_registration)]: 注册记录对象列表

#### `public  `[`create_registration`](#namespaceapp_1_1crud_1_1registration_1a20733d661f9a082b648c0c6d881ebcbd)`(Session db,`[`RegistrationCreate`](#classapp_1_1models_1_1registration_1_1_registration_create)` registration,int user_id)` 

创建新的注册记录

Args: db: 数据库会话 registration: 注册记录创建模型 user_id: 用户ID

Returns: [Registration](#classapp_1_1database_1_1_registration): 创建的注册记录对象

#### `public  `[`delete_registration`](#namespaceapp_1_1crud_1_1registration_1ab93378fa05b214f93587d122761be3eb)`(Session db,int registration_id)` 

删除注册记录

Args: db: 数据库会话 registration_id: 注册记录ID

Returns: [Registration](#classapp_1_1database_1_1_registration): 被删除的注册记录对象，如果不存在则返回None

# namespace `app::crud::user` 

用户数据库操作模块

本模块提供用户相关的数据库CRUD操作函数

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`get_user`](#namespaceapp_1_1crud_1_1user_1ab33183c170d7fc7ddb122d800282ae7f)`(Session db,int user_id)`            | 根据ID获取用户
`public  `[`get_user_by_username`](#namespaceapp_1_1crud_1_1user_1aefaf67ce3b31acf7f09fc8420761b83c)`(Session db,str username)`            | 根据用户名获取用户
`public  `[`get_user_by_email`](#namespaceapp_1_1crud_1_1user_1adcce69d5599eedd7a0a4ebe5bc182213)`(Session db,str email)`            | 根据电子邮箱获取用户
`public  `[`get_users`](#namespaceapp_1_1crud_1_1user_1ab0ca8529244b599738e66a0cf7136e70)`(Session db,int skip,int limit)`            | 获取所有用户
`public  `[`create_user`](#namespaceapp_1_1crud_1_1user_1a77c737f3f48132e1bab1df457d2c84cd)`(Session db,`[`UserCreate`](#classapp_1_1models_1_1user_1_1_user_create)` user)`            | 创建新用户

## Members

#### `public  `[`get_user`](#namespaceapp_1_1crud_1_1user_1ab33183c170d7fc7ddb122d800282ae7f)`(Session db,int user_id)` 

根据ID获取用户

Args: db: 数据库会话 user_id: 用户ID

Returns: [User](#classapp_1_1database_1_1_user): 用户对象，如果不存在则返回None

#### `public  `[`get_user_by_username`](#namespaceapp_1_1crud_1_1user_1aefaf67ce3b31acf7f09fc8420761b83c)`(Session db,str username)` 

根据用户名获取用户

Args: db: 数据库会话 username: 用户名

Returns: [User](#classapp_1_1database_1_1_user): 用户对象，如果不存在则返回None

#### `public  `[`get_user_by_email`](#namespaceapp_1_1crud_1_1user_1adcce69d5599eedd7a0a4ebe5bc182213)`(Session db,str email)` 

根据电子邮箱获取用户

Args: db: 数据库会话 email: 电子邮箱

Returns: [User](#classapp_1_1database_1_1_user): 用户对象，如果不存在则返回None

#### `public  `[`get_users`](#namespaceapp_1_1crud_1_1user_1ab0ca8529244b599738e66a0cf7136e70)`(Session db,int skip,int limit)` 

获取所有用户

Args: db: 数据库会话 skip: 跳过的记录数 limit: 返回的最大记录数

Returns: List[[User](#classapp_1_1database_1_1_user)]: 用户对象列表

#### `public  `[`create_user`](#namespaceapp_1_1crud_1_1user_1a77c737f3f48132e1bab1df457d2c84cd)`(Session db,`[`UserCreate`](#classapp_1_1models_1_1user_1_1_user_create)` user)` 

创建新用户

Args: db: 数据库会话 user: 用户创建模型

Returns: [User](#classapp_1_1database_1_1_user): 创建的用户对象

# namespace `app::database` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`get_db`](#database_8py_1ae6bae1bc6b5767a56b312d1cf37dd1ee)`()`            | 获取数据库会话的依赖函数
`public  `[`create_tables`](#database_8py_1a21f7b7e2142ce0947cbcaa5b27c7ae55)`()`            | 创建数据库表
`class `[`app::database::AgendaItem`](#classapp_1_1database_1_1_agenda_item) | 会议议程项模型
`class `[`app::database::Conference`](#classapp_1_1database_1_1_conference) | 会议数据库模型
`class `[`app::database::Friendship`](#classapp_1_1database_1_1_friendship) | 好友关系模型
`class `[`app::database::FriendshipStatus`](#classapp_1_1database_1_1_friendship_status) | 
`class `[`app::database::Notification`](#classapp_1_1database_1_1_notification) | 通知模型
`class `[`app::database::NotificationType`](#classapp_1_1database_1_1_notification_type) | 
`class `[`app::database::Registration`](#classapp_1_1database_1_1_registration) | 会议注册模型（用户参加会议的记录）
`class `[`app::database::User`](#classapp_1_1database_1_1_user) | 用户数据库模型

## Members

#### `public  `[`get_db`](#database_8py_1ae6bae1bc6b5767a56b312d1cf37dd1ee)`()` 

获取数据库会话的依赖函数

用于FastAPI依赖注入，创建数据库会话并在请求结束时自动关闭 
#### Returns
Generator[数据库会话对象]

#### `public  `[`create_tables`](#database_8py_1a21f7b7e2142ce0947cbcaa5b27c7ae55)`()` 

创建数据库表

使用SQLAlchemy创建所有定义的数据库表

# class `app::database::AgendaItem` 

```
class app::database::AgendaItem
  : public Base
```  

会议议程项模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::database::Conference` 

```
class app::database::Conference
  : public Base
```  

会议数据库模型

存储会议的基本信息，包括标题、描述、时间和地点

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::database::Friendship` 

```
class app::database::Friendship
  : public Base
```  

好友关系模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::database::FriendshipStatus` 

```
class app::database::FriendshipStatus
  : public PyEnum
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::database::Notification` 

```
class app::database::Notification
  : public Base
```  

通知模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::database::NotificationType` 

```
class app::database::NotificationType
  : public PyEnum
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::database::Registration` 

```
class app::database::Registration
  : public Base
```  

会议注册模型（用户参加会议的记录）

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::database::User` 

```
class app::database::User
  : public Base
```  

用户数据库模型

存储用户的基本信息，包括认证信息和权限设置

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `app::dependencies` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`verify_password`](#dependencies_8py_1a40731b72ec9914f74ac90918296ab838)`(plain_password,hashed_password)`            | 验证密码
`public  `[`get_password_hash`](#dependencies_8py_1a6291a2bf804959818901fac8f193f49d)`(password)`            | 生成密码哈希
`public  `[`authenticate_user`](#dependencies_8py_1a87c80760c9848b70d9bf765ea3ed661e)`(Session db,str username,str password)`            | 用户认证
`public  `[`create_access_token`](#dependencies_8py_1ace20b6d68961f9864435e08f9d25d073)`(dict data,Optional expires_delta)`            | 创建访问令牌
`public  `[`get_current_user`](#dependencies_8py_1af12093b8dc702010b147eb4aacd9523e)`(str token,Session db)`            | 获取当前用户
`public  `[`get_current_active_user`](#dependencies_8py_1a8c2684482e270173e2d10aa366a2e8db)`(Request request,Session db)`            | 获取当前活跃用户或重定向到登录页面
`public  `[`get_current_admin_user`](#dependencies_8py_1ab043bf03ce6ed5b3e89a382c98f3c6df)`(Request request,Session db)`            | 获取当前管理员用户或重定向

## Members

#### `public  `[`verify_password`](#dependencies_8py_1a40731b72ec9914f74ac90918296ab838)`(plain_password,hashed_password)` 

验证密码

比较明文密码与哈希密码是否匹配

Args: plain_password: 明文密码 hashed_password: 哈希后的密码

Returns: bool: 密码是否匹配

#### `public  `[`get_password_hash`](#dependencies_8py_1a6291a2bf804959818901fac8f193f49d)`(password)` 

生成密码哈希

对明文密码进行哈希处理

Args: password: 明文密码

Returns: str: 哈希后的密码

#### `public  `[`authenticate_user`](#dependencies_8py_1a87c80760c9848b70d9bf765ea3ed661e)`(Session db,str username,str password)` 

用户认证

验证用户名和密码是否正确

Args: db: 数据库会话 username: 用户名 password: 明文密码

Returns: User|False: 认证成功返回用户对象，失败返回False

#### `public  `[`create_access_token`](#dependencies_8py_1ace20b6d68961f9864435e08f9d25d073)`(dict data,Optional expires_delta)` 

创建访问令牌

生成JWT访问令牌

Args: data: 要编码到令牌中的数据 expires_delta: 令牌过期时间增量，如果为None则使用默认值

Returns: str: 编码后的JWT令牌

#### `public  `[`get_current_user`](#dependencies_8py_1af12093b8dc702010b147eb4aacd9523e)`(str token,Session db)` 

获取当前用户

从JWT令牌中解析并获取当前用户

Args: token: JWT令牌 db: 数据库会话

Returns: [User](#classapp_1_1database_1_1_user): 当前用户对象

Raises: HTTPException: 如果令牌无效或用户不存在

#### `public  `[`get_current_active_user`](#dependencies_8py_1a8c2684482e270173e2d10aa366a2e8db)`(Request request,Session db)` 

获取当前活跃用户或重定向到登录页面

从请求中获取当前用户，如果未登录则重定向到登录页面

Args: request: HTTP请求对象 db: 数据库会话

Returns: User|RedirectResponse: 当前用户对象或重定向响应

#### `public  `[`get_current_admin_user`](#dependencies_8py_1ab043bf03ce6ed5b3e89a382c98f3c6df)`(Request request,Session db)` 

获取当前管理员用户或重定向

从请求中获取当前用户，验证是否为管理员，如果不是则重定向

Args: request: HTTP请求对象 db: 数据库会话

Returns: User|RedirectResponse: 当前管理员用户对象或重定向响应

# namespace `app::init_db` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`init_db`](#init__db_8py_1ad85714b869522050fcc3ed8c9ecf0566)`()`            | 初始化数据库

## Members

#### `public  `[`init_db`](#init__db_8py_1ad85714b869522050fcc3ed8c9ecf0566)`()` 

初始化数据库

创建数据库表并添加默认数据（如管理员账号）

# namespace `app::main` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`home`](#main_8py_1aa4e8d0d7d92ffeccaa0eea530d7bd8e7)`(Request request,Session db)`            | 首页路由处理函数
`public  `[`health_check`](#main_8py_1acf4df756006003ef120d105cc189549f)`()`            | 健康检查接口

## Members

#### `public  `[`home`](#main_8py_1aa4e8d0d7d92ffeccaa0eea530d7bd8e7)`(Request request,Session db)` 

首页路由处理函数

处理首页请求，显示会议列表和用户信息 
#### Parameters
* `request` HTTP请求对象 

* `db` 数据库会话对象 

#### Returns
HTMLResponse 渲染后的首页HTML响应

#### `public  `[`health_check`](#main_8py_1acf4df756006003ef120d105cc189549f)`()` 

健康检查接口

用于监控系统是否正常运行，返回系统状态信息 
#### Returns
dict 包含系统状态和消息的字典

# namespace `app::models::conference` 

会议和议程项相关的数据模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`app::models::conference::AgendaItemBase`](#classapp_1_1models_1_1conference_1_1_agenda_item_base) | 议程项基础模型
`class `[`app::models::conference::AgendaItemCreate`](#classapp_1_1models_1_1conference_1_1_agenda_item_create) | 议程项创建模型
`class `[`app::models::conference::AgendaItemResponse`](#classapp_1_1models_1_1conference_1_1_agenda_item_response) | 议程项响应模型
`class `[`app::models::conference::ConferenceBase`](#classapp_1_1models_1_1conference_1_1_conference_base) | 会议基础模型
`class `[`app::models::conference::ConferenceCreate`](#classapp_1_1models_1_1conference_1_1_conference_create) | 会议创建模型
`class `[`app::models::conference::ConferenceResponse`](#classapp_1_1models_1_1conference_1_1_conference_response) | 会议响应模型
`class `[`app::models::conference::ConferenceUpdate`](#classapp_1_1models_1_1conference_1_1_conference_update) | 会议更新模型

# class `app::models::conference::AgendaItemBase` 

```
class app::models::conference::AgendaItemBase
  : public BaseModel
```  

议程项基础模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::conference::AgendaItemCreate` 

```
class app::models::conference::AgendaItemCreate
  : public app.models.conference.AgendaItemBase
```  

议程项创建模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::conference::AgendaItemResponse` 

```
class app::models::conference::AgendaItemResponse
  : public app.models.conference.AgendaItemBase
```  

议程项响应模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::conference::ConferenceBase` 

```
class app::models::conference::ConferenceBase
  : public BaseModel
```  

会议基础模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::conference::ConferenceCreate` 

```
class app::models::conference::ConferenceCreate
  : public app.models.conference.ConferenceBase
```  

会议创建模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::conference::ConferenceResponse` 

```
class app::models::conference::ConferenceResponse
  : public app.models.conference.ConferenceBase
```  

会议响应模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::conference::ConferenceUpdate` 

```
class app::models::conference::ConferenceUpdate
  : public app.models.conference.ConferenceBase
```  

会议更新模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `app::models::friendship` 

好友关系相关的数据模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`app::models::friendship::FriendResponse`](#classapp_1_1models_1_1friendship_1_1_friend_response) | 好友响应模型，用于返回好友信息
`class `[`app::models::friendship::FriendshipBase`](#classapp_1_1models_1_1friendship_1_1_friendship_base) | 好友关系基础模型
`class `[`app::models::friendship::FriendshipCreate`](#classapp_1_1models_1_1friendship_1_1_friendship_create) | 好友关系创建模型
`class `[`app::models::friendship::FriendshipResponse`](#classapp_1_1models_1_1friendship_1_1_friendship_response) | 好友关系响应模型
`class `[`app::models::friendship::FriendshipUpdate`](#classapp_1_1models_1_1friendship_1_1_friendship_update) | 好友关系更新模型

# class `app::models::friendship::FriendResponse` 

```
class app::models::friendship::FriendResponse
  : public BaseModel
```  

好友响应模型，用于返回好友信息

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::friendship::FriendshipBase` 

```
class app::models::friendship::FriendshipBase
  : public BaseModel
```  

好友关系基础模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::friendship::FriendshipCreate` 

```
class app::models::friendship::FriendshipCreate
  : public app.models.friendship.FriendshipBase
```  

好友关系创建模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::friendship::FriendshipResponse` 

```
class app::models::friendship::FriendshipResponse
  : public app.models.friendship.FriendshipBase
```  

好友关系响应模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::friendship::FriendshipUpdate` 

```
class app::models::friendship::FriendshipUpdate
  : public BaseModel
```  

好友关系更新模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `app::models::notification` 

通知相关的数据模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`app::models::notification::NotificationBase`](#classapp_1_1models_1_1notification_1_1_notification_base) | 通知基础模型
`class `[`app::models::notification::NotificationCreate`](#classapp_1_1models_1_1notification_1_1_notification_create) | 通知创建模型
`class `[`app::models::notification::NotificationResponse`](#classapp_1_1models_1_1notification_1_1_notification_response) | 通知响应模型
`class `[`app::models::notification::NotificationUpdate`](#classapp_1_1models_1_1notification_1_1_notification_update) | 通知更新模型

# class `app::models::notification::NotificationBase` 

```
class app::models::notification::NotificationBase
  : public BaseModel
```  

通知基础模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::notification::NotificationCreate` 

```
class app::models::notification::NotificationCreate
  : public app.models.notification.NotificationBase
```  

通知创建模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::notification::NotificationResponse` 

```
class app::models::notification::NotificationResponse
  : public app.models.notification.NotificationBase
```  

通知响应模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::notification::NotificationUpdate` 

```
class app::models::notification::NotificationUpdate
  : public BaseModel
```  

通知更新模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `app::models::registration` 

会议注册相关的数据模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`app::models::registration::RegistrationBase`](#classapp_1_1models_1_1registration_1_1_registration_base) | 注册基础模型
`class `[`app::models::registration::RegistrationCreate`](#classapp_1_1models_1_1registration_1_1_registration_create) | 注册创建模型
`class `[`app::models::registration::RegistrationResponse`](#classapp_1_1models_1_1registration_1_1_registration_response) | 注册响应模型
`class `[`app::models::registration::UserRegistrationResponse`](#classapp_1_1models_1_1registration_1_1_user_registration_response) | 用户注册响应模型，包含用户和会议信息

# class `app::models::registration::RegistrationBase` 

```
class app::models::registration::RegistrationBase
  : public BaseModel
```  

注册基础模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::registration::RegistrationCreate` 

```
class app::models::registration::RegistrationCreate
  : public app.models.registration.RegistrationBase
```  

注册创建模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::registration::RegistrationResponse` 

```
class app::models::registration::RegistrationResponse
  : public app.models.registration.RegistrationBase
```  

注册响应模型

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::registration::UserRegistrationResponse` 

```
class app::models::registration::UserRegistrationResponse
  : public BaseModel
```  

用户注册响应模型，包含用户和会议信息

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `app::models::user` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`app::models::user::Token`](#classapp_1_1models_1_1user_1_1_token) | 令牌模型
`class `[`app::models::user::TokenData`](#classapp_1_1models_1_1user_1_1_token_data) | 令牌数据模型
`class `[`app::models::user::UserBase`](#classapp_1_1models_1_1user_1_1_user_base) | 用户基础模型
`class `[`app::models::user::UserCreate`](#classapp_1_1models_1_1user_1_1_user_create) | 用户创建模型
`class `[`app::models::user::UserLogin`](#classapp_1_1models_1_1user_1_1_user_login) | 用户登录模型
`class `[`app::models::user::UserResponse`](#classapp_1_1models_1_1user_1_1_user_response) | 用户响应模型

# class `app::models::user::Token` 

```
class app::models::user::Token
  : public BaseModel
```  

令牌模型

用于JWT认证的令牌信息

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::user::TokenData` 

```
class app::models::user::TokenData
  : public BaseModel
```  

令牌数据模型

用于存储令牌中的数据

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::user::UserBase` 

```
class app::models::user::UserBase
  : public BaseModel
```  

用户基础模型

包含用户名和邮箱的基础信息

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::user::UserCreate` 

```
class app::models::user::UserCreate
  : public app.models.user.UserBase
```  

用户创建模型

用于注册新用户，包含密码和管理员权限

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::user::UserLogin` 

```
class app::models::user::UserLogin
  : public BaseModel
```  

用户登录模型

用于用户登录验证

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::user::UserResponse` 

```
class app::models::user::UserResponse
  : public app.models.user.UserBase
```  

用户响应模型

用于返回用户信息，不包含敏感数据

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `app::routers::auth` 

认证相关的路由处理模块

包含用户注册、登录、登出和令牌获取等功能

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`register_page`](#namespaceapp_1_1routers_1_1auth_1ac894e794f149ef8279d31da276125353)`(Request request)`            | 渲染注册页面
`public  `[`register`](#namespaceapp_1_1routers_1_1auth_1a742bca4b190f822d5d48d2417c6ab6a9)`(Request request,str username,str email,str password,str confirm_password,bool is_admin,Session db)`            | 注册新用户
`public  `[`login_page`](#namespaceapp_1_1routers_1_1auth_1a74157d17dda3dbf04c1c6b0abc5f532f)`(Request request)`            | 渲染登录页面
`public  `[`login`](#namespaceapp_1_1routers_1_1auth_1ae70c05cf4568b2b3397ccbd8c565d242)`(Request request,str username,str password,Session db)`            | 用户登录
`public  `[`logout`](#namespaceapp_1_1routers_1_1auth_1aaed036e1d746e7cd6e44aa28ac771d49)`()`            | 用户登出
`public  `[`login_for_access_token`](#namespaceapp_1_1routers_1_1auth_1abae6ff81781ab2037df7034581616820)`(OAuth2PasswordRequestForm form_data,Session db)`            | 获取访问令牌（用于API认证）

## Members

#### `public  `[`register_page`](#namespaceapp_1_1routers_1_1auth_1ac894e794f149ef8279d31da276125353)`(Request request)` 

渲染注册页面

#### `public  `[`register`](#namespaceapp_1_1routers_1_1auth_1a742bca4b190f822d5d48d2417c6ab6a9)`(Request request,str username,str email,str password,str confirm_password,bool is_admin,Session db)` 

注册新用户

#### `public  `[`login_page`](#namespaceapp_1_1routers_1_1auth_1a74157d17dda3dbf04c1c6b0abc5f532f)`(Request request)` 

渲染登录页面

#### `public  `[`login`](#namespaceapp_1_1routers_1_1auth_1ae70c05cf4568b2b3397ccbd8c565d242)`(Request request,str username,str password,Session db)` 

用户登录

#### `public  `[`logout`](#namespaceapp_1_1routers_1_1auth_1aaed036e1d746e7cd6e44aa28ac771d49)`()` 

用户登出

#### `public  `[`login_for_access_token`](#namespaceapp_1_1routers_1_1auth_1abae6ff81781ab2037df7034581616820)`(OAuth2PasswordRequestForm form_data,Session db)` 

获取访问令牌（用于API认证）

# namespace `app::routers::conferences` 

会议相关的路由处理模块

包含会议列表、详情、创建、编辑、删除和议程管理等功能

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`list_conferences`](#namespaceapp_1_1routers_1_1conferences_1a4662b81bd448dff2470ea65049810826)`(Request request,Session db)`            | 显示所有会议列表
`public  `[`create_conference_page`](#namespaceapp_1_1routers_1_1conferences_1af3c6e65e018cf0b26585c8a95dc3268f)`(Request request,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | 渲染创建会议页面
`public  `[`create_conference`](#namespaceapp_1_1routers_1_1conferences_1a51442c457652be1d0e5c57367ea84d6f)`(Request request,str title,str description,str date,str location,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | 创建新会议
`public  `[`admin_conferences`](#namespaceapp_1_1routers_1_1conferences_1ad86297869c180294da4025aa6a4f415d)`(Request request,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | List conferences created by the current admin user.
`public  `[`conference_detail`](#namespaceapp_1_1routers_1_1conferences_1a660abe0e42aaab5340d64360ebcca6d0)`(Request request,int conference_id,Session db)`            | Get a conference by ID.
`public  `[`edit_conference_page`](#namespaceapp_1_1routers_1_1conferences_1a07ec49ad3c6c141a937d4c28085ddc4b)`(Request request,int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | Render the edit conference page.
`public  `[`edit_conference`](#namespaceapp_1_1routers_1_1conferences_1aa61ba1c75992e0557d166ae1980e42ef)`(Request request,int conference_id,str title,str description,str date,str location,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | Edit a conference.
`public  `[`delete_conference`](#namespaceapp_1_1routers_1_1conferences_1a9c4e0c10ba5034c47dca387159bb055c)`(int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | Delete a conference.
`public  `[`add_agenda_item`](#namespaceapp_1_1routers_1_1conferences_1aa8a421bdfd74c0844507cad90d12a533)`(Request request,int conference_id,str start_time,str end_time,str title,str speaker,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | Add an agenda item to a conference.
`public  `[`delete_agenda_item`](#namespaceapp_1_1routers_1_1conferences_1a5499155e445401d8cfe6fd97d6920450)`(int conference_id,int agenda_item_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | Delete an agenda item.

## Members

#### `public  `[`list_conferences`](#namespaceapp_1_1routers_1_1conferences_1a4662b81bd448dff2470ea65049810826)`(Request request,Session db)` 

显示所有会议列表

#### `public  `[`create_conference_page`](#namespaceapp_1_1routers_1_1conferences_1af3c6e65e018cf0b26585c8a95dc3268f)`(Request request,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

渲染创建会议页面

#### `public  `[`create_conference`](#namespaceapp_1_1routers_1_1conferences_1a51442c457652be1d0e5c57367ea84d6f)`(Request request,str title,str description,str date,str location,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

创建新会议

#### `public  `[`admin_conferences`](#namespaceapp_1_1routers_1_1conferences_1ad86297869c180294da4025aa6a4f415d)`(Request request,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

List conferences created by the current admin user.

#### `public  `[`conference_detail`](#namespaceapp_1_1routers_1_1conferences_1a660abe0e42aaab5340d64360ebcca6d0)`(Request request,int conference_id,Session db)` 

Get a conference by ID.

#### `public  `[`edit_conference_page`](#namespaceapp_1_1routers_1_1conferences_1a07ec49ad3c6c141a937d4c28085ddc4b)`(Request request,int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

Render the edit conference page.

#### `public  `[`edit_conference`](#namespaceapp_1_1routers_1_1conferences_1aa61ba1c75992e0557d166ae1980e42ef)`(Request request,int conference_id,str title,str description,str date,str location,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

Edit a conference.

#### `public  `[`delete_conference`](#namespaceapp_1_1routers_1_1conferences_1a9c4e0c10ba5034c47dca387159bb055c)`(int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

Delete a conference.

#### `public  `[`add_agenda_item`](#namespaceapp_1_1routers_1_1conferences_1aa8a421bdfd74c0844507cad90d12a533)`(Request request,int conference_id,str start_time,str end_time,str title,str speaker,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

Add an agenda item to a conference.

#### `public  `[`delete_agenda_item`](#namespaceapp_1_1routers_1_1conferences_1a5499155e445401d8cfe6fd97d6920450)`(int conference_id,int agenda_item_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

Delete an agenda item.

# namespace `app::routers::friends` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`list_friends`](#friends_8py_1a3160d83a66d09af493152bd46e1733ba)`(Request request,Session db)`            | 显示好友列表页面。
`public  `[`add_friend`](#friends_8py_1a19894d69edadea56a32a724477913f65)`(Request request,int friend_id,Session db)`            | 发送好友请求。
`public  `[`accept_friend_request`](#friends_8py_1a0687bf5c6e20d75755252820e3095193)`(Request request,int friendship_id,Session db)`            | 接受好友请求。
`public  `[`reject_friend_request`](#friends_8py_1a259bbaacd8b607a50713fd33963da107)`(Request request,int friendship_id,Session db)`            | 拒绝好友请求。
`public  `[`delete_friend`](#friends_8py_1a25f185cb7eba2fc7a7d568d3ddd895fa)`(Request request,int friend_id,Session db)`            | 删除好友。

## Members

#### `public  `[`list_friends`](#friends_8py_1a3160d83a66d09af493152bd46e1733ba)`(Request request,Session db)` 

显示好友列表页面。

#### `public  `[`add_friend`](#friends_8py_1a19894d69edadea56a32a724477913f65)`(Request request,int friend_id,Session db)` 

发送好友请求。

#### `public  `[`accept_friend_request`](#friends_8py_1a0687bf5c6e20d75755252820e3095193)`(Request request,int friendship_id,Session db)` 

接受好友请求。

#### `public  `[`reject_friend_request`](#friends_8py_1a259bbaacd8b607a50713fd33963da107)`(Request request,int friendship_id,Session db)` 

拒绝好友请求。

#### `public  `[`delete_friend`](#friends_8py_1a25f185cb7eba2fc7a7d568d3ddd895fa)`(Request request,int friend_id,Session db)` 

删除好友。

# namespace `app::routers::my_conferences` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`my_conferences`](#my__conferences_8py_1a287235a8f614df789624812ea187644b)`(Request request,Session db)`            | 显示用户的会议页面，包括参与的会议和创建的会议（如果是管理员）。

## Members

#### `public  `[`my_conferences`](#my__conferences_8py_1a287235a8f614df789624812ea187644b)`(Request request,Session db)` 

显示用户的会议页面，包括参与的会议和创建的会议（如果是管理员）。

# namespace `app::routers::notifications` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`list_notifications`](#notifications_8py_1adce469a5698c94c0c71ce73d775a6560)`(Request request,Session db)`            | 显示通知列表页面。
`public  `[`mark_notification_as_read`](#notifications_8py_1adf955a7f87216168b9141142208bfece)`(Request request,int notification_id,Session db)`            | 将通知标记为已读。
`public  `[`mark_all_notifications_as_read`](#notifications_8py_1addbe10f0e98e16a5a2bce0d458c71a5c)`(Request request,Session db)`            | 将所有通知标记为已读。
`public  `[`delete_notification`](#notifications_8py_1a08e2c2a86df389fa48aa15076cc19fe0)`(Request request,int notification_id,Session db)`            | 删除通知。

## Members

#### `public  `[`list_notifications`](#notifications_8py_1adce469a5698c94c0c71ce73d775a6560)`(Request request,Session db)` 

显示通知列表页面。

#### `public  `[`mark_notification_as_read`](#notifications_8py_1adf955a7f87216168b9141142208bfece)`(Request request,int notification_id,Session db)` 

将通知标记为已读。

#### `public  `[`mark_all_notifications_as_read`](#notifications_8py_1addbe10f0e98e16a5a2bce0d458c71a5c)`(Request request,Session db)` 

将所有通知标记为已读。

#### `public  `[`delete_notification`](#notifications_8py_1a08e2c2a86df389fa48aa15076cc19fe0)`(Request request,int notification_id,Session db)` 

删除通知。

# namespace `app::routers::registrations` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`my_registrations`](#registrations_8py_1aebcbac7d6340a03e227c97e23d729561)`(Request request,Session db)`            | List registrations for the current user.
`public  `[`register_for_conference`](#registrations_8py_1a747713a82795a86ec792bd5cd5c59b4c)`(int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | Register for a conference.
`public  `[`unregister_from_conference`](#registrations_8py_1a036f41e8b163e693659c5d19c216cc91)`(int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)`            | Unregister from a conference.
`public  `[`conference_attendees`](#registrations_8py_1a1d3af50d73643f9ab61d62f20cef44f3)`(Request request,int conference_id,Session db)`            | List attendees for a conference.
`public  `[`invite_friend`](#registrations_8py_1af2f519fbae1d70890ab0b8c1755e46bb)`(Request request,int conference_id,int friend_id,Session db)`            | 邀请好友参加会议。
`public  `[`accept_invitation`](#registrations_8py_1af840ac5725c69c3c15bcaccedb74a40c)`(Request request,int conference_id,bool direct_accept,Session db)`            | 接受会议邀请。

## Members

#### `public  `[`my_registrations`](#registrations_8py_1aebcbac7d6340a03e227c97e23d729561)`(Request request,Session db)` 

List registrations for the current user.

#### `public  `[`register_for_conference`](#registrations_8py_1a747713a82795a86ec792bd5cd5c59b4c)`(int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

Register for a conference.

#### `public  `[`unregister_from_conference`](#registrations_8py_1a036f41e8b163e693659c5d19c216cc91)`(int conference_id,Session db,`[`User`](#classapp_1_1database_1_1_user)` current_user)` 

Unregister from a conference.

#### `public  `[`conference_attendees`](#registrations_8py_1a1d3af50d73643f9ab61d62f20cef44f3)`(Request request,int conference_id,Session db)` 

List attendees for a conference.

#### `public  `[`invite_friend`](#registrations_8py_1af2f519fbae1d70890ab0b8c1755e46bb)`(Request request,int conference_id,int friend_id,Session db)` 

邀请好友参加会议。

#### `public  `[`accept_invitation`](#registrations_8py_1af840ac5725c69c3c15bcaccedb74a40c)`(Request request,int conference_id,bool direct_accept,Session db)` 

接受会议邀请。

# namespace `delete_users` 

删除指定用户的脚本。 运行方式：python -m app.scripts.delete_users

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`delete_users`](#namespacedelete__users_1ab5a59c3333c090903c658c364010953d)`()`            | 删除指定的用户。

## Members

#### `public  `[`delete_users`](#namespacedelete__users_1ab5a59c3333c090903c658c364010953d)`()` 

删除指定的用户。

# namespace `fix_admin_password` 

将admin用户的密码重置为admin123的脚本。 运行方式：python -m app.scripts.fix_admin_password

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`fix_admin_password`](#namespacefix__admin__password_1a51d45c5872b6d52b7027e522c785ede5)`()`            | 将admin用户的密码重置为'admin123'。

## Members

#### `public  `[`fix_admin_password`](#namespacefix__admin__password_1a51d45c5872b6d52b7027e522c785ede5)`()` 

将admin用户的密码重置为'admin123'。

# namespace `generate_demo_data` 

生成示例数据的脚本，包括会议、好友关系和通知。 运行方式：python -m app.scripts.generate_demo_data

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`generate_demo_data`](#namespacegenerate__demo__data_1a5e6f5619d772403ba84dddae238a106f)`()`            | 生成示例数据。
`public  `[`create_demo_conferences`](#namespacegenerate__demo__data_1a229b37410cdac80e6953852f0ac2b804)`(Session db,users)`            | 创建示例会议。
`public  `[`create_demo_friendships`](#namespacegenerate__demo__data_1af2381bad1e8169dd02f56879f57edbb3)`(Session db,users)`            | 创建示例好友关系。
`public  `[`create_demo_registrations`](#namespacegenerate__demo__data_1ae0a02e20448c54c7f56b836228483d06)`(Session db,users,conferences)`            | 创建示例会议注册。
`public  `[`create_demo_notifications`](#namespacegenerate__demo__data_1aceeab2a8fb6f9e95c6ed35020c352243)`(Session db,users,conferences)`            | 创建示例通知。

## Members

#### `public  `[`generate_demo_data`](#namespacegenerate__demo__data_1a5e6f5619d772403ba84dddae238a106f)`()` 

生成示例数据。

#### `public  `[`create_demo_conferences`](#namespacegenerate__demo__data_1a229b37410cdac80e6953852f0ac2b804)`(Session db,users)` 

创建示例会议。

#### `public  `[`create_demo_friendships`](#namespacegenerate__demo__data_1af2381bad1e8169dd02f56879f57edbb3)`(Session db,users)` 

创建示例好友关系。

#### `public  `[`create_demo_registrations`](#namespacegenerate__demo__data_1ae0a02e20448c54c7f56b836228483d06)`(Session db,users,conferences)` 

创建示例会议注册。

#### `public  `[`create_demo_notifications`](#namespacegenerate__demo__data_1aceeab2a8fb6f9e95c6ed35020c352243)`(Session db,users,conferences)` 

创建示例通知。

# namespace `generate_demo_users` 

生成示例用户的脚本。 运行方式：python -m app.scripts.generate_demo_users

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`generate_demo_users`](#namespacegenerate__demo__users_1a3b83c2edc45fd3199c5e0a5c2333b275)`()`            | 生成示例用户。

## Members

#### `public  `[`generate_demo_users`](#namespacegenerate__demo__users_1a3b83c2edc45fd3199c5e0a5c2333b275)`()` 

生成示例用户。

# namespace `generate_invitations` 

生成会议邀请通知的脚本。 运行方式：python -m app.scripts.generate_invitations

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`generate_invitations`](#namespacegenerate__invitations_1aa9bc41f895a19b8a0aa0c9017538fcaf)`()`            | 生成会议邀请通知。

## Members

#### `public  `[`generate_invitations`](#namespacegenerate__invitations_1aa9bc41f895a19b8a0aa0c9017538fcaf)`()` 

生成会议邀请通知。

# namespace `list_admin_users` 

列出所有用户及其管理员状态的脚本。 运行方式：python -m app.scripts.list_admin_users

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`list_admin_users`](#namespacelist__admin__users_1abb39cb0ff4e1399072161b918bb16122)`()`            | 列出所有用户及其管理员状态。

## Members

#### `public  `[`list_admin_users`](#namespacelist__admin__users_1abb39cb0ff4e1399072161b918bb16122)`()` 

列出所有用户及其管理员状态。

# namespace `update_all_passwords` 

更新所有用户密码的脚本。 运行方式：python -m app.scripts.update_all_passwords

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`update_all_passwords`](#namespaceupdate__all__passwords_1a9cc031e7c89c059cc1a07fc3d2eec9ad)`()`            | 将所有用户的密码更新为'1'。

## Members

#### `public  `[`update_all_passwords`](#namespaceupdate__all__passwords_1a9cc031e7c89c059cc1a07fc3d2eec9ad)`()` 

将所有用户的密码更新为'1'。

# class `app::models::conference::AgendaItemResponse::Config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::conference::ConferenceResponse::Config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::friendship::FriendResponse::Config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::friendship::FriendshipResponse::Config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::notification::NotificationResponse::Config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::registration::RegistrationResponse::Config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::registration::UserRegistrationResponse::Config` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `app::models::user::UserResponse::Config` 

用户ID

是否为管理员

创建时间

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

Generated by [Moxygen](https://sourcey.com/moxygen)