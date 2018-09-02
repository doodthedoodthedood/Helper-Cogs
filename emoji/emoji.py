from discord.ext import commands
from redbot.core import commands

class Emoji:
        
        
        @commands.group(pass_context=True, no_pm=True)
        async def emoji(self, ctx):
                """emoji stuff"""
            
        @emoji.command(no_pm=True)
        async def convert(self, ctx, emoji):
            """Converts text into an emoji"""
            await ctx.send(":{emoji}:")
            
        @emoji.command(no_pm=True)
        async def list(self, ctx):
           await ctx.send(emojis)
            
            

