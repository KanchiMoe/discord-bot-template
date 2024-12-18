import discord
from discord.ext import commands
from discord import app_commands
import logging

# Global bot reference
bot: commands.Bot = None

# !!foo command
@commands.command(name="foo")
async def foo(ctx):
    await ctx.send("You triggered the !!foo command!")
    print("!!foo command executed")

# /bar command
@app_commands.command(name="bar", description="Triggers the bar command")
async def bar(interaction: discord.Interaction):
    await interaction.response.send_message("You triggered the /bar command!")
    print("/bar slash command executed")

# Setup function
async def setup(bot_instance: commands.Bot):
    global bot
    bot = bot_instance

    # Register !!foo command
    logging.debug("Registering command: !!foo")
    bot.add_command(foo)

    # Register /bar slash command
    logging.debug("Registering slash command: /bar")
    bot.tree.add_command(bar)

    logging.info("Commands registered")
