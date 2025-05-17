<div align="center">
  <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo">
  </a>

## 🤖 NoneBot2 插件：自动同意被过滤好友请求 auto\_accept\_filtered\_requests

  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/yourname/auto_accept_filtered_requests.svg" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.8|3.9|3.10|3.11-blue.svg" alt="python">
  <a href="https://onebot.dev/">
    <img src="https://img.shields.io/badge/OneBot-v11-black?style=social" alt="onebot">
  </a>
</div>

> \[!IMPORTANT]
> **收藏项目**，获取插件更新的第一时间通知！🌟

## 📖 插件简介

`auto_accept_filtered_requests` 是基于 [NoneBot2](https://github.com/nonebot/nonebot2) 开发的插件，用于自动获取并处理平台过滤掉的好友申请请求。

插件会定时向指定的 API 请求被平台过滤的好友申请列表，并自动同意这些请求（可选记录 QQ 至文件中）。

## 🚀 功能特性

* ⏱️ 定时检查被过滤的好友申请
* ✅ 自动同意符合条件的请求
* 📝 可选记录已通过的 QQ 号
* 🔧 完全可配置（通过 `.env.prod`）

## 🔧 环境配置

在 `.env.prod` 文件中添加如下配置项：

| 环境变量名            | 默认值                     | 说明               |
| ---------------- | ----------------------- | ---------------- |
| `API_BASE`       | `http://127.0.0.1:3000` | 请求 API 的地址       |
| `INTERVAL`       | `30`                    | 每次检查的时间间隔（单位：秒）  |
| `COUNT`          | `50`                    | 每次拉取的最大请求数       |
| `LOG_FILE`       | `approved_requests.txt` | （可选）记录已通过好友的文件路径 |
| `ENABLE_LOGGING` | `false`                 | 是否启用记录通过请求的 QQ 号 |

示例 `.env.prod` 文件：

```ini
API_BASE=http://127.0.0.1:3000
INTERVAL=60
COUNT=100
LOG_FILE=approved.txt
ENABLE_LOGGING=true
```

## 💿 安装方式

进入你的 NoneBot2 项目根目录，安装插件代码：

```bash
# 假设你已放置插件到插件目录 plugins/auto_accept_filtered_requests
# 或者通过 git clone 添加插件
```

修改 `pyproject.toml` 中 `[tool.nonebot]` 配置：

```toml
[tool.nonebot]
plugins = ["auto_accept_filtered_requests"]
```

## 🧠 插件机制简介

插件启动后：

1. 加载 `.env.prod` 配置。
2. 注册 `on_startup` 事件，启动自动检查任务。
3. 定时调用 API 拉取被过滤的好友申请。
4. 自动发送同意请求，记录 QQ 到本地文件（可选）。

## 🧪 示例日志输出

```
✅ auto_accept_filtered_requests 插件已启动
🌟 auto_check_loop 已启动
发现请求来自: 张三（QQ: 123456789），flag: abc123，自动同意中...
✅ 已记录 QQ：123456789 到 approved_requests.txt
```

## 📜 License

本项目基于 MIT 协议发布。欢迎自由使用与修改。