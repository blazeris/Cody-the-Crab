from discord.ext import commands
import discord
class create_channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    # args 1 = number of channels to create
    # args 2 = category name
    async def addchannel(self, context, args1, name):
        guild = context.guild
        
        
        try:
            channel_number = int(args1)

            # creates the category name and the channel name
            
            await guild.create_category_channel(name)
            await guild.create_role(name=name)
            category_name = discord.utils.get(context.guild.categories, name=name)
            for i in range(channel_number):
                await guild.create_text_channel(f'{i + 1}', category=category_name)
                await guild.create_voice_channel(f'{i + 1}', category=category_name)
            
        except ValueError:
            await context.send("the second arguement needs to be an integer!")
            
        


def setup(bot):
    bot.add_cog(create_channel(bot))
    