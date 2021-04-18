import discord
from discord.ext import commands
from discord.utils import get

class delete_channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="deletecategory", description="<name of category> : deletes the category, role and all channels within that category")
    async def deletecategory(self, context, name):
        guild = context.guild
        category = ""
        try:
            # checks to see if a user is not an admin and tries to run the command, stop
            if not context.message.author.guild_permissions.administrator:
                await context.send("You cannot use this command, you are not an admin")
                return
            
            # checks to see if the category has already been created, if so set the category to i
            list_of_cats = guild.categories
            for i in list_of_cats:
                if name == i.name.lower():
                    category = i
                    
            # if the category does not exist, leave the command
            if category == "":
                await context.send("That category does not exist!")
                return
            
            # gets the specifc role for the category
            role = discord.utils.get(context.message.guild.roles, name=name)

            # a list of channels that are under the category
            channels = category.channels

            # deletes the channels in the category, the category and the role for that category
            for channel in channels:
                await channel.delete()
            await category.delete()
            await role.delete()

            await context.message.add_reaction('👍')

        except ValueError:
            await context.send("There seems to be an error!")

def setup(bot):
    bot.add_cog(delete_channel(bot))
    