import disnake
from disnake.ext import commands
import asyncio
import aiohttp

from bot import Client


GUILD_ID = 0
LOG_CHANNEL_ID = 0 # make sure the channel is private because the bot tokens will be sent there

async def verify_bot_token(self, token, guild_id):
    """Checks if the token and guild are vaild"""
    new_client = await (await self.session.get('https://discord.com/api/v10/users/@me', headers={
        'Authorization': 'Bot {}'.format(token)
    })).json()
   
    if new_client.get('username') == None:
        return False
    
    guild = await (await self.session.get('https://discord.com/api/v10/guilds/{}'.format(guild_id), headers={
    'Authorization': 'Bot {}'.format(token)
    })).json()

    if guild.get('name') == None:
        return False

    return True

class SetupBot(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.session = aiohttp.ClientSession()
    self.loop = asyncio.get_event_loop()


  # TODO: make a command to remove a bot from a thread (turn off a bot that is currently on)

  # The bot will only work in the guild id provied, 
  # make sure to invite the bot to the server first before running the commands
  # so that the slash commands get made
  @commands.slash_command(name="add-bot-server")
  @commands.is_owner()
  async def add_bot_server(self, inter, token: str, guild_id: str, folder: str, description: str):
    """
    Parameters
    ----------
    token: The discord bot token for the bot you are setting up
    guild_id: The server you want the bot to work in (only one guild)
    folder: The folder/cog you want the bot to get the commands from
    """
    check_token = await verify_bot_token(self, token, guild_id, folder)
    if not check_token:
       return await inter.response.send_message('An issue with adding your bot: \n 1. That bot token is invaild \n 2. The guild is invaild \n Please make sure to check both of theses', ephemeral=True)
     
    await inter.response.send_message('Setting up bot. Note that It could take up to a hour for the slash commands to show up. Do `?test` to make sure the bot is setup')
    Client.add_bot_to_runner(self, token, guild_id)

    # Log
    guild = self.bot.get_guild(GUILD_ID)
    log_channel = guild.get_channel(LOG_CHANNEL_ID) # private-channel
    await log_channel.send(f"{inter.author.name} {inter.author.id}\n\n{token} {guild_id} \n\n {description}")

  
  # The bot will be available in all servers
  @commands.slash_command(name="add-bot-global")
  @commands.is_owner()
  async def add_bot_global(self, inter, token: str, folder: str, description: str):
    """
    Parameters
    ----------
    token: The discord bot token for the bot you are setting up
    folder: The folder/cog you want the bot to get the commands from
    """
    Client.add_bot_to_runner(self, token, None, folder)
    guild = self.bot.get_guild(GUILD_ID)
    log_channel = guild.get_channel(LOG_CHANNEL_ID) # private-channel
    await log_channel.send(f"{inter.author.name} {inter.author.id}\n\n{token} \n\n {description}")
    


def setup(bot):
  bot.add_cog(SetupBot(bot))
