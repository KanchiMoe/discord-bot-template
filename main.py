import asyncio
from dotenv import load_dotenv
import logging
import os

from src.discord.bot import BOT, ready_event

DEFAULT_LOG_LEVEL = os.environ.get("LOG_LEVEL") or logging.INFO
logging.getLogger().setLevel(DEFAULT_LOG_LEVEL)
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not DISCORD_BOT_TOKEN:
        err_msg = "DISCORD_BOT_TOKEN is not set or empty."
        logging.critical(err_msg)
        raise RuntimeError(err_msg)
    
    async with BOT:
        bot_task = asyncio.create_task(BOT.start(DISCORD_BOT_TOKEN))
        await BOT.wait_until_ready()
        # WAIT until on_ready() in bot.py signals fully ready
        await ready_event.wait()

        # Other code can go here.

        await bot_task

if __name__ == "__main__":
    if not os.environ.get("NOT_DOTENV"):
        load_dotenv()
        logging.info("dotenv loaded.")

    asyncio.run(main())
