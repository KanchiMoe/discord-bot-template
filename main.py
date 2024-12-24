import os
import logging
from dotenv import load_dotenv
from discord.ext import commands
import src.bot_client as bot_client
from src.bot_commands import setup

load_dotenv()

DEFAULT_LOG_LEVEL = os.environ.get("LOG_LEVEL") or logging.INFO
logging.getLogger().setLevel(DEFAULT_LOG_LEVEL)
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if DISCORD_BOT_TOKEN is None:
    logging.critical("DISCORD_BOT_TOKEN is empty. Can not continue.")
    raise RuntimeError

BOT = bot_client.BOT

@BOT.event
async def on_ready():
    logging.info(f"Logged in as {BOT.user} ({BOT.user.id})")
    await bot_client.tree_sync()
    logging.info("Bot ready.")

@BOT.event
async def on_connect():
    await setup(BOT)

# Run the bot with the token
if __name__ == "__main__":
    BOT.run(DISCORD_BOT_TOKEN)
