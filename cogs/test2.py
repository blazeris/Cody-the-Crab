from discord.ext import commands

description = ("!ping will make the bot respond with PONG")

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("TEAKSJDTHJKDAFHKJ")
    

    @commands.command(name = 'pinggggggggg', description = 'When ping, the bot will PONG')
    async def pinggggggggg(self, context):
        await context.send("PONG")

    @commands.command(name = 'pingggggggggg', description = 'When ping, the bot will PONG')
    async def pingggggggggg(self, context):
        await context.send("PONGG")

    @commands.command(name = 'pinggggggggggg', description = 'When ping, the bot will PONG')
    async def pinggggggggggg(self, context):
        await context.send("PONGGG")

    @commands.command(name = 'pingggggggggggg', description = 'When ping, the bot will PONG')
    async def pingggggggggggg(self, context):
        await context.send("PONGGGG")

    @commands.command(name = 'pinggggggggggggg', description = 'When ping, the bot will PONG')
    async def pinggggggggggggg(self, context):
        await context.send("PONGGGGGgggggggggggggggggggggggggggggggg")

    @commands.command(name = 'pingggggggggggggg', description = 'When ping, the bot will PONG')
    async def pingggggggggggggg(self, context):
        await context.send("PONGGGGGgggggggggggggggg")

    @commands.command(name = 'pinggggggggggggggg', description = 'When ping, the bot will PONG')
    async def pinggggggggggggggg(self, context):
        await context.send("PONGGGGGgggggggggggggggg")

    @commands.command(name = 'pingggggggggggggggg', description = 'When ping, the bot will PONG')
    async def pingggggggggggggggg(self, context):
        await context.send("PONGGGGGgggggggg")
def setup(bot):
    bot.add_cog(Test(bot))
    print("in setup")
    