##
# @file run.py
# @brief 应用程序启动脚本
# @details 使用uvicorn启动FastAPI应用程序的入口脚本
# @author Meeting System Team
# @date 2024
# @version 1.0
##

import uvicorn

##
# @brief 主函数
# @details 启动FastAPI应用程序，配置主机、端口和重载模式
##
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8010, reload=True)
