from discord.ext import commands


class Repeat:
        """Repeats your text"""
        
        def __init__(self, bot):
                self.bot = bot
        
        @commands.command(no_pm=True)
        async def sayagain(self, *, text):
            """Copies You"""
            await self.bot.say(text)
        
        
def setup(bot):
    n = Repeat(bot)
    bot.add_cog(n)
        
