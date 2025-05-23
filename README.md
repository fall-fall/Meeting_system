# 会议管理系统

基于Python和FastAPI构建的简单会议管理系统。

## 功能特点

- 用户注册和身份验证
- 基于角色的访问控制（管理员和普通用户）
- 会议创建和管理
- 会议议程管理
- 用户会议注册
- 使用Jinja2模板的响应式UI

## 技术栈

- **后端**: Python 3.x + FastAPI
- **数据库**: SQLite 
- **前端**: Jinja2模板 + 自定义CSS
- **认证**: JWT令牌

## 安装说明

1. 克隆仓库
2. 安装依赖:

   ```
   pip install -r requirements.txt
   ```
3. 运行应用程序:

   ```
   python run.py
   ```

   或者
   ```
   uvicorn app.main:app --reload
   ```
4. 打开浏览器并访问 `http://localhost:8000`

## 项目结构

```
meeting/
├── app/
│   ├── main.py                 # FastAPI应用程序入口点
│   ├── config.py               # 配置设置
│   ├── database.py             # 数据库连接和模型
│   ├── dependencies.py         # 依赖注入
│   ├── routers/                # API路由
│   ├── models/                 # Pydantic模型
│   ├── crud/                   # 数据库操作
│   ├── schemas/                # 数据库模式
│   ├── static/                 # 静态文件(CSS, JS)
│   └── templates/              # Jinja2模板
├── requirements.txt            # 项目依赖
├── run.py                      # 运行脚本
└── README.md                   # 项目文档
```

## API文档

应用程序运行后，您可以在以下位置访问API文档:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 默认管理员账户

- 用户名: admin
- 密码: admin123

## 许可证

本项目采用MIT许可证。
