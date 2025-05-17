import asyncio
import httpx
import os
from dotenv import load_dotenv

from nonebot import get_driver, logger

# 加载 .env.prod 配置
load_dotenv(dotenv_path=".env.prod")

driver = get_driver()

@driver.on_startup
async def _():
    logger.info("✅ auto_accept_filtered_requests 插件已启动")
    asyncio.create_task(auto_check_loop())

# 从环境变量读取配置
API_BASE = os.getenv("API_BASE", "http://127.0.0.1:3000")
INTERVAL = int(os.getenv("INTERVAL", "30"))
LOG_FILE = os.getenv("LOG_FILE", "approved_requests.txt")
COUNT = int(os.getenv("COUNT", "50"))
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "false").lower() == "true"

def log_approved_qq(qq: str):
    if not ENABLE_LOGGING:
        return
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{qq}\n")
        logger.info(f"✅ 已记录 QQ：{qq} 到 {LOG_FILE}")
    except Exception as e:
        logger.error(f"写入文件失败：{e}")

async def fetch_filtered_requests(count: int = COUNT):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                f"{API_BASE}/get_doubt_friends_add_request",
                json={"count": count},
                timeout=5
            )
        logger.debug(f"HTTP 请求返回: {res.status_code} {res.text}")
        res.raise_for_status()
        data = res.json()
        if data.get("status") != "ok":
            logger.warning("获取被过滤好友请求失败")
            return []
        return data.get("data", [])
    except Exception as e:
        logger.error(f"获取被过滤好友请求时出错: {e}")
        return []

async def approve_request(flag: str, qq: str):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                f"{API_BASE}/set_doubt_friends_add_request",
                json={"flag": flag, "approve": True},
                timeout=5
            )
        res.raise_for_status()
        logger.info(f"已同意被过滤好友请求 flag={flag}，QQ={qq}")
        log_approved_qq(qq)
    except Exception as e:
        logger.error(f"处理被过滤好友请求失败（flag={flag}，QQ={qq}）: {e}")

async def auto_check_loop():
    logger.warning("🌟 auto_check_loop 已启动")
    await asyncio.sleep(6)
    while True:
        logger.info("开始自动检查被过滤的好友请求...")
        requests = await fetch_filtered_requests()
        if not requests:
            logger.info("暂无被过滤的好友请求。")
        for req in requests:
            flag = req.get("flag")
            nick = req.get("nick", "未知昵称")
            qq = str(req.get("user_id", "未知QQ"))
            logger.info(f"发现请求来自: {nick}（QQ: {qq}），flag: {flag}，自动同意中...")
            await approve_request(flag, qq)
        await asyncio.sleep(INTERVAL)
