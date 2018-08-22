from discord.ext import commands

class Hug:
        """Family Hug!"""
        def __init__(self, bot):
            self.bot = bot
            
            
            
        @commands.command()
        async def hug(self, *, random=''):
            self.bot.say('***FAMLIYA HUG INCOMING!!***:hugging: :heart:')
            
            
def setup(bot):
    n = Hug(bot)
    bot.add_cog(n)
