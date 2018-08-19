import discord
from discord.ext import commands

class fun:
    """A cog that does fun stuff"""

    def __init__(self, bot):
        self.bot = bot

   @commands.command(no_pm=True)
    async def repeat(self, *, text):
        """Copies your words"""
        await self.bot.say(text)

def setup(bot):
    bot.add_cog(fun(bot))
