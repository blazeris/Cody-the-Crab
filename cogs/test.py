from discord.ext import commands

description = ("!ping will make the bot respond with PONG")

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("TEAKSJDTHJKDAFHKJ")
    

    @commands.command(name = 'ping', description = 'When ping, the bot will PONG')
    async def ping(self, context):
        await context.send("PONG")



def setup(bot):
    bot.add_cog(Test(bot))
    print("in setup")
    