import disnake
from disnake.ext import commands

class FunCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command()
  async def fun_command(self, inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message("This command is very fun")


def setup(bot):
  bot.add_cog(FunCommands(bot))
