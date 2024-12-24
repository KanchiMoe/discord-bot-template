import discord
from discord.ext import commands
import logging

intents = discord.Intents.default() # default intents
intents.guilds = True
intents.message_content = True  # Enable message content intent
intents.members = True # Enable server member intent (for member join/leave events)
intents.presences = True # Enable presence intent (for status changes like online/offline)
intents.messages = True
BOT = commands.Bot(command_prefix="!!", intents=intents, help_command=None)

async def tree_sync():
    await BOT.tree.sync()
    logging.debug("Slash commands synced")
