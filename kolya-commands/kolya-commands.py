from discord.ext import commands

class Hug:
        """Family Hug!"""
        def __init__(self, bot):
            self.bot = bot
            
            
            
        @commands.command()
        async def famhug(self):
         await self.bot.say('***FAMLIYA HUG INCOMING!!***:hugging: :heart:')
        
        @commands.command()
        async def member(self):
         await self.bot.say("Alright kid, you're a Familya member now. https://gph.is/2w6UiTV")
            
            
def setup(bot):
    n = Hug(bot)
    bot.add_cog(n)
