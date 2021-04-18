from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("TEAKSJDTHJKDAFHKJ")
    

    @commands.command(name = 'ping', description = 'When ping, the bot will PONG')
    async def ping(self, context):
        await context.send("PONG")

    @commands.command(name = 'pingg', description = 'When ping, the bot will PONG')
    async def pingg(self, context):
        await context.send("PONGG")

    @commands.command(name = 'pinggg', description = 'When ping, the bot will PONG')
    async def pinggg(self, context):
        await context.send("PONGGG")

    @commands.command(name = 'pingggg', description = 'When ping, the bot will PONG')
    async def pingggg(self, context):
        await context.send("PONGGGG")

    @commands.command(name = 'pinggggg', description = 'When ping, the bot will PONG')
    async def pinggggg(self, context):
        await context.send("PONGGGGGgggggggggggggggggggggggggggggggg")

    @commands.command(name = 'pingggggg', description = 'When ping, the bot will PONG')
    async def pingggggg(self, context):
        await context.send("PONGGGGGgggggggggggggggg")

    @commands.command(name = 'pinggggggg', description = 'When ping, the bot will PONG')
    async def pinggggggg(self, context):
        await context.send("PONGGGGGgggggggggggggggg")

    @commands.command(name = 'pingggggggg', description = 'When ping, the bot will PONG')
    async def pingggggggg(self, context):
        await context.send("PONGGGGGgggggggg")
def setup(bot):
    bot.add_cog(Test(bot))
    print("in setup")
    