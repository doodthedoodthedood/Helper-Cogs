from discord.ext import commands
from redbot.core import commands
from discord.ext import emoji
import json
class Emoji:
        
        
        @commands.group(pass_context=True, no_pm=True)
        async def emoji(self, ctx):
                """emoji stuff"""
            
        @emoji.command(no_pm=True)
        async def convert(self, ctx, emoji):
            """Converts text into an emoji"""
            with open('emojis.json') as emojis:
                if emoji in emojis:
                    await ctx.send(":" + emoji + ":")
                else:
                    await ctx.send('That is not a valid emoji')
            
        @emoji.command(no_pm=True)
        async def list(self, ctx):
           await ctx.send(Emoji.emojis)
            
            

