import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from bot import firebase


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
                await context.message.add_reaction('❌')
                await context.send("You cannot use this command, you are not an admin")
                return

            # checks to see if the category has already been created, if so set the category to i
            list_of_cats = guild.categories
            for i in list_of_cats:
                if name.lower() == i.name.lower():
                    category = i

            # if the category does not exist, leave the command
            if category == "":
                await context.message.add_reaction('❌')
                await context.send("That category does not exist!")
                return

            text_channels = category.text_channels

            # while len(c)
            # deletes the channels in the category, the category and the role for that category
            i = 1
            while len(text_channels) > 0:
                text_channels = category.text_channels
                vc_channels = category.voice_channels

                await text_channels[0].delete()
                await asyncio.sleep(0.1)
                await vc_channels[0].delete()
                await asyncio.sleep(0.1)

                text_channels = category.text_channels
                vc_channels = category.voice_channels

                role = discord.utils.get(
                    context.message.guild.roles, name=f'{name.lower()} {i}')
                await role.delete()
                await asyncio.sleep(0.1)
                i += 1

            firebase.DB_remove('servers/' + str(context.guild.id) +
                               '/createdroles/' + str(category.name))
            await category.delete()
            await context.message.add_reaction('✅')

        except ValueError:
            await context.message.add_reaction('❌')
            await context.send("There seems to be an error!")


def setup(bot):
    bot.add_cog(delete_channel(bot))
