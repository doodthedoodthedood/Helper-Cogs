from discord.ext import commands

class Calculator:
        """Adds, subtracts, multiplies, and divides your numbers"""
        def __init__(self, bot):
            self.bot = bot
        
        version = '1.0.0'
        
        @commands.group(pass_context=True, no_pm=True)
        async def calculator(self, ctx):
         if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            
        @calculator.command(no_pm=True)
        async def add(self, num1, num2):
            """Adds 2 Numbers"""
            int(num1)
            int(num2)
            await self.bot.say('Adding Numbers...')
            final = int(num1) + int(num2)
            await self.bot.say(str(final) + ' is the answer you are looking for.')
            
            
        @calculator.command(no_pm=True)
        async def subtract(self, num1, num2):
            """Subtracts 2 Numbers"""
            int(num1)
            int(num2)
            await self.bot.say('Subtracting Numbers...')
            final = int(num1) - int(num2)
            await self.bot.say(str(final) + ' is the answer you are looking for.')
            
            
        @calculator.command(no_pm=True)
        async def multiply(self, num1, num2):
            """Multiplies 2 Numbers"""
            int(num1)
            int(num2)
            await self.bot.say('Multipliying Numbers...')
            final = int(num1) * int(num2)
            await self.bot.say(str(final) + ' is the answer you are looking for.')
            
        @calculator.command(no_pm=True)
        async def divide(self, num1, num2):
            """Divides 2 Numbers"""
            int(num1)
            int(num2)
            await self.bot.say('Dividing Numbers...')
            final = int(num1) / int(num2)
            await self.bot.say(str(final) + ' is the answer you are looking for.')
        
        
        @calculator.command(no_pm=True)
        async def version(self):
            """Shows the version"""
            await self.bot.say('The version is ' + version)
        
                
def setup(bot):
        n = Calculator(bot)
        bot.add_cog(n)
