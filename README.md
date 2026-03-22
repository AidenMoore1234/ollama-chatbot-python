# ollama-chatbot-python
> Python + Ollama 本地离线聊天机器人 | 求职技术展示项目

## 📌 项目介绍
使用 Python 调用本地 Ollama 大模型实现命令行聊天机器人，无需联网即可对话，展示 Python 基础、API 调用、异常处理等工程能力。

## ✨ 核心功能
- 本地离线聊天（依赖 Ollama 服务）
- 支持输入「再见」退出对话
- 完善的异常处理（避免程序崩溃）

## 🛠 技术栈
- Python 3.x
- Ollama（本地大模型）
- requests 库（HTTP 请求）

## 🚀 运行步骤
1. 安装依赖：`pip install -r requirements.txt`
2. 安装 Ollama：https://ollama.com/
3. 拉取轻量模型：`ollama pull qwen3:4b`
4. 启动 Ollama 服务（默认端口 11434）
5. 运行机器人：`python chatbot.py`

## 📁 项目结构
ollama-chatbot-python/
├── chatbot.py # 主程序（聊天核心逻辑）
├── requirements.txt # 依赖清单
└── README.md # 项目说明


## 📝 求职说明
本项目为 AI 应用方向学习作品，代码结构清晰、注释规范，可直接运行，展示基础工程能力与 AI 技术应用思路。

## 👨‍💻 作者
GitHub：AidenMoore1234
