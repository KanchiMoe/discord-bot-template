import discord
from discord.ext import commands
from discord import app_commands
import src.bot_client as bot_client

BOT = bot_client.BOT

# /ping
@app_commands.command(name="ping", description="Ping")
async def ping_slash(interaction: discord.Interaction):
    await interaction.response.send_message(":stopwatch: | pong!")


async def setup(bot_instance: commands.Bot):
    bot = bot_instance
    bot.tree.add_command(ping_slash)
