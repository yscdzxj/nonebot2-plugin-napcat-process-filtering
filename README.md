<div align="center">
  <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo">
  </a>

  <h2>✨ NoneBot2 插件：自动同意 QQ 被过滤的好友请求 ✨</h2>

  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/yscdzxj/nonebot2_qq_napcat_process_filtering.svg" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.8|3.9|3.10|3.11-blue.svg" alt="python">
  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/NoneBot2-v2.0.0-green.svg" alt="NoneBot2">
  </a>
  <a href="https://napneko.com/">
    <img src="https://img.shields.io/badge/NapCat-NTQQ-orange.svg" alt="NapCat">
  </a>
</div>

> [!IMPORTANT]
> **收藏项目**，你将从 GitHub 上无延迟地接收所有发布通知～⭐️

> 基于 NapCat 的 `<获取被过滤好友请求 API>` 实现的自动同意被过滤好友请求的 NoneBot2 插件。

---

## 📖 介绍

本插件旨在自动处理 NapCat 中被过滤的好友请求，减少手动操作，提高效率。

### ✨ 特性

* 自动轮询 NapCat 提供的被过滤好友请求接口
* 自动同意符合条件的好友请求
* 可选记录已同意的 QQ 号
* 可配置轮询间隔和请求数量

## 💿 安装

### 依赖环境

* Python 3.8 及以上版本
* NoneBot2
* NapCat（必须开启 HTTP 服务端口127.0.0.1:3000）

### 安装插件

1. 确保已安装 `httpx` 驱动：

   ```bash
   nb driver install httpx
   ```
2. 在使用前请先安装 nonebot-plugin-apscheduler 插件至项目环境中，可参考获取商店插件来了解并选择安装插件的方式。如：
在项目目录下执行以下命令：

   ```bash
   nb plugin install nonebot-plugin-apscheduler
   ```
3. 克隆本仓库或将插件代码放入 NoneBot2 项目的插件目录。

## ⚙️ 配置

在项目目录下 `.env.prod` 文件添加以下配置：

```env
# NapCat HTTP 服务地址
API_BASE=http://127.0.0.1:3000

# 轮询间隔（秒）
INTERVAL=3600

# 每次获取的请求数量
COUNT=1

# 是否启用日志记录（true/false）(会自动填充在项目目录)
ENABLE_LOGGING=true

# 日志文件名字
LOG_FILE=approved_requests.txt
```

## 🚀 使用

插件将在 NoneBot2 启动时自动运行，并开始轮询 NapCat 的被过滤好友请求接口。

### 示例日志输出

```

auto_accept_filtered_requests 插件已启动
auto_check_loop 已启动
开始自动检查被过滤的好友请求...
发现请求来自: 用户昵称（QQ: 123456789），flag: abcdefg，自动同意中...
已同意被过滤好友请求 flag=abcdefg，QQ=123456789
已记录 QQ：123456789 到 approved_requests.txt
```



## 🧩 插件原理

插件通过 NapCat 提供的 HTTP 接口获取被过滤的好友请求列表，并自动发送同意请求。

### 主要接口

* `/set_doubt_friends_add_request`：获取被过滤好友请求

详细接口文档请参考(https://napcat.apifox.cn/289565516e0)。

## 🛠️ 开发者说明

插件核心逻辑位于 `__inti__.py` 文件中，主要包括以下函数：

* `fetch_filtered_requests`：获取被过滤的好友请求
* `approve_request`：同意指定的好友请求
* `auto_check_loop`：定时轮询并处理请求

如需自定义处理逻辑，可根据需求修改上述函数。

## 🤝 致谢

* [NapCat]https://napneko.github.io/：现代化的基于 NTQQ 的 Bot 协议端实现
* [NoneBot2](https://github.com/nonebot/nonebot2)：跨平台的 Python 异步机器人框架