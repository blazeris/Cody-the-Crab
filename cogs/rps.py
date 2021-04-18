from discord.ext import commands
import random


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, context, args1):
        num = random.randrange(1,3)
        #✌️ = 1, ✊ = 2, ✋ = 3
        sign = ""
        if num == 1:
            sign = "✌️"
        if num == 2:
            sign = "✊"
        if num == 3:
            sign = "✋"
        await context.send(args1 + " vs " + sign)
        if args1 == "✌️":
            if num == 1:
                await context.send("Tie")
            if num == 2:
                await context.send("I win")
            if num == 3:
                await context.send("You win")
        if args1 == "✊":
            if num == 1:
                await context.send("You win")
            if num == 2:
                await context.send("Tie")
            if num == 3:
                await context.send("I win")
        if args1 == "✋":
            if num == 1:
                await context.send("I win")
            if num == 2:
                await context.send("You win")
            if num == 3:
                await context.send("Tie")


def setup(bot):
    bot.add_cog(Test(bot))