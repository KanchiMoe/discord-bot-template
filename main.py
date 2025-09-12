from dotenv import load_dotenv
import logging
import os

from src.discord.bot import BOT

DEFAULT_LOG_LEVEL = os.environ.get("LOG_LEVEL") or logging.DEBUG
logging.getLogger().setLevel(DEFAULT_LOG_LEVEL)
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not DISCORD_BOT_TOKEN:
        raise RuntimeError("DISCORD_BOT_TOKEN is not set or empty.")

    BOT.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    if not os.environ.get("NOT_DOTENV"):
        load_dotenv()
        logging.info("dotenv loaded.")

    main()
