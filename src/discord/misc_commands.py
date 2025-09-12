import discord
from discord import app_commands
#from src.bot import BOT

#/ping, all servers
@app_commands.command(name="ping", description="Ping")
async def ping_slash(interaction: discord.Interaction):
    await interaction.response.send_message(":stopwatch: | pong!")
