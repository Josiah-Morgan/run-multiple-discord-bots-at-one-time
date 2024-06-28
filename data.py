import os
import traceback

import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot('1', intents=intents, activity=disnake.Game(name="bots"))

for filename in os.listdir("main_bot_cog"):
    if filename.endswith('.py'):
        bot.load_extension(f'main_bot_cog.{filename[:-3]}')
        print(filename + ' Loaded')


@bot.slash_command()
@commands.is_owner()
async def load(inter, cogname: str, folder = 'cogs'):
    """
    Loads a cog
    Parameters
    ----------
    cogname: The cog to load
    """
    try:
      bot.load_extension(f"{folder}.{cogname}")
    except Exception as e:
      await inter.response.send_message(
        f"```py\n{traceback.format_exc()}\n```\n\n\n, {e}")
    else:
      await inter.response.send_message(
        f":gear: Successfully Loaded **{cogname}** Module!") 

@bot.slash_command()
@commands.is_owner()
async def unload(inter, cogname: str, folder = 'cogs'):
    """
    Unloads a cog
    Parameters
    ----------
    cogname: The cog to unload
    """
    try:
      bot.unload_extension(f"{folder}.{cogname}")
    except Exception as e:
      await inter.response.send_message(
        f"```py\n{traceback.format_exc()}\n```\n\n\n, {e}")
    else:
      await inter.response.send_message(
        f":gear: Successfully Unloaded **{cogname}** Module!")

@bot.slash_command()
@commands.is_owner()
async def reload(inter, cogname: str, folder = 'cogs'):
    """
    Loads and unloads a cog
    Parameters
    ----------
    cogname: The cog to reload
    """
    try:
      bot.unload_extension(f"{folder}.{cogname}")
      bot.load_extension(f"{folder}.{cogname}")
    except Exception as e:
      await inter.response.send_message(
        f"```py\n{traceback.format_exc()}\n```\n\n\n, {e}")
    else:
      await inter.response.send_message(
        f":gear: Successfully Reloaded the **{cogname}** module!")

bot.run("<bot_token>")
