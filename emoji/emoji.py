from discord.ext import commands

class Emoji:
        
        
        @commands.group(pass_context=True, no_pm=True)
        async def emoji(self, ctx):
         if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            
        @emoji.command(no_pm=True)
        async def convert(self, emoji):
            """Converts text into an emoji"""
            await self.bot.say(":{}:").format(emoji)
            
        @emoji.command(no_pm=True)
        async def list(self, ctx):
            self.bot.say(emojis)
            
            

