import discord
from discord.ext import commands
import logging

intents = discord.Intents.default() # default intents
intents.guilds          = True # Events related to servers, such as on_guild_join or on_guild_update
intents.message_content = True # Access to the content of messages (needed to read messages)
intents.members         = True # Events and data related to server members (e.g., member join/leave, fetching member list)
intents.presences       = True # Updates about user presence (e.g., online, offline, idle, do not disturb)
intents.messages        = True # Message-related events like on_message, on_message_edit, on_message_delete

# Bot instance
BOT = commands.Bot(command_prefix="/", intents=intents, help_command=None)

async def bot_add_slashcommands(bot: commands.Bot):
    logging.debug("Registering commands...")
    from src.discord.misc_commands import ping_slash
    bot.tree.add_command(ping_slash)

async def tree_sync():
    logging.debug("Syncing commands with Discord...")
    try:
        # global sync
        await BOT.tree.sync()
        logging.info(f"Slash commands (global) synced")
    except Exception as e:
        logging.error(f"{e}")

@BOT.event
async def on_connect():
    logging.info("Connection to Discord established")

@BOT.event
async def on_ready():
    logging.info(f"Logged in as '{BOT.user}' ({BOT.user.id})")
    await bot_add_slashcommands(BOT)
    await tree_sync()
    logging.info("Bot ready")
