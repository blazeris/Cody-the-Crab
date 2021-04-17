import discord
import math
import re
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('1')

    @commands.command()
    async def help(self, context, cog = "1"):
                
        em = discord.Embed(title = "Help Pages!")
        
        em.set_thumbnail(url="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fab2ce1a7-3074-410e-84ac-d44e78ae88cb%2FByte_the_Shark.png?table=block&id=f76f6edc-694f-497f-a793-716dcfc1e340&width=600&userId=&cache=v2")
        
        cogs = [c for c in self.bot.cogs.keys()]

        totalPages = math.ceil(len(cogs)/4)

        cog = int(cog)

        if cog >totalPages or cog < 1:
            await context.send(f"Invalid page number: '{cog}', please pick from {totalPages} ")
            return 

        neededCogs = []
        for i in range(4):
            x = i + (int(cog)-1)*4
            try:
                neededCogs.append(cogs[x])
            except IndexError:
                pass
        for cog in neededCogs:
            commandList = "" 
            for command in self.bot.get_cog(cog).walk_commands():
                if command.hidden:
                    continue
                elif command.parent != None:
                    continue

                commandList += f"**{command.name}** - *{command.description}*"
            commandList +="\n"
            em.add_field(name=cog, value=commandList, inline=False)

        await context.send(embed = em)
        


def setup(bot):
    bot.add_cog(Test(bot))