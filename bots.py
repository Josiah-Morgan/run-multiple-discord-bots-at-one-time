import asyncio
import json
import os

import disnake
from disnake.ext import commands


class Client:
    def add_bot_to_runner(self, token, guild_id = None, cog_folder = '<default_folder>'):
        # test_guilds is to make it where only one server can use the bot's commands
        if not guild_id:
            test_guilds = None
        else:
            test_guilds = [int(guild_id)]
        bot = commands.Bot('?', intents=disnake.Intents.all(), test_guilds=test_guilds)

        for file in os.listdir(f'{cog_folder}'):
            if file.endswith('.py'):
                bot.load_extension(f'{cog_folder}.{file[:-3]}')

        asyncio.run_coroutine_threadsafe(bot.start(token), self.loop)
