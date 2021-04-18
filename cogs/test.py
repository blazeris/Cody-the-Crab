from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("TEAKSJDTHJKDAFHKJ")

    @commands.command()
    async def ping(self, context):
        print("in ping")
        await context.send("PONG")


def setup(bot):
    bot.add_cog(Test(bot))
    print("test loaded")
