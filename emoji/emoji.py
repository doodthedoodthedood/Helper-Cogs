from discord.ext import commands
from redbot.core import commands

class Emoji:
        
        
        @commands.group(pass_context=True, no_pm=True)
        async def emoji(self, ctx):
         if ctx.invoked_subcommand is None:
            await ctx.send_cmd_help(ctx)
            
        @emoji.command(no_pm=True)
        async def convert(self, emoji):
            """Converts text into an emoji"""
            await ctx.send(":{}:").format(emoji)
            
        @emoji.command(no_pm=True)
        async def list(self, ctx):
           await ctx.send(emojis)
            
            

