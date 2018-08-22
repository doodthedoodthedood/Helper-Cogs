from discort.ext import commands

class Calculator:
        """Adds, subtracts, multiplies, and divides your numbers"""
        async def __init__(self, bot):
            self.bot = bot
        
        
        
        @commands.group(pass_context=True, no_pm=True)
        async def calculator(self, cxt)
         if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            
        @calculator.command(no_pm=True)
        async def add(self, num1, num2):
            self.bot.say('Adding Numbers...')
            final = num1 + num2
            self.bot.say(final + ' is the answer you are looking for.')
            
            
        @calculator.command(no_pm=True)
        async def subtract(self, num1, num2):
            self.bot.say('Subtracting Numbers...')
            final = num1 - num2
            self.bot.say(final + ' is the answer you are looking for.')
            
            
        @calculator.command(no_pm=True)
        async def multiply(self, num1, num2):
            self.bot.say('Multipliying Numbers...')
            final = num1 x num2
            self.bot.say(final + ' is the answer you are looking for.')
            
        @calculator.command(no_pm=True)
        async def divide(self, num1, num2):
            self.bot.say('Dividing Numbers...')
            final = num1 / num2
            self.bot.say(final + ' is the answer you are looking for.')
            
            
    def setup(bot):
        n = Repeat(bot)
        bot.add_cog(n)
