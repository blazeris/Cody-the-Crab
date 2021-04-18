from discord.channel import CategoryChannel
from discord.ext import commands
import discord
from discord.utils import get
import random

class create_channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    # args 1 = number of channels to create
    # args 2 = category name
    @commands.command(name="createcategory", 
    description="<number of channels to add> <category name> : adds the category and amount of text and voice channels to that category")
    async def createcategory(self, context, args1, args2):
        guild = context.guild
        try:
            # checks to see if a user is not an admin and tries to run the command, stop
            if not context.message.author.guild_permissions.administrator:
                await context.send("You cannot use this command, you are not an admin")
                return
            
            # checks to see if the category has already been created, if so stop the command
            list_of_cats = guild.categories
            for i in list_of_cats:
                if args2.lower() == i.name.lower():
                    await context.send("That category has already been created")
                    return
            
            
            # creates the role and the channel for the given name
            channel_number = int(args1)
            await guild.create_category_channel(args2.lower())
            await guild.create_role(name=args2.lower())



            # gets the name of the category the user is trying to create
            category_name = discord.utils.get(context.guild.categories, name=args2.lower())
            specific_role = get(guild.roles, name = args2.lower())
            # overwrites certain permissions, making those with a certain role only be able to look at the category
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                specific_role: discord.PermissionOverwrite(read_messages=True)
            }

            for i in range(channel_number):
                await guild.create_text_channel(f'{args2.lower()} {i + 1}',overwrites = overwrites, category=category_name)
                await guild.create_voice_channel(f'{args2.lower()} {i + 1}', overwrites = overwrites, category=category_name)
            await context.message.add_reaction('👍')
        
        except ValueError:
            await context.send("the second argument needs to be an integer!")
    
def setup(bot):
    bot.add_cog(create_channel(bot))
    