import asyncio
from discord.channel import CategoryChannel
from discord.ext import commands
import discord
from discord.utils import get
import random
from bot import firebase


class create_channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # args 1 = number of channels to create
    # args 2 = category name
    @commands.command(name="createcategory",
                      description="<number of channels to add> <category name in quotes>: adds the category and amount of text and voice channels to that category")
    async def createcategory(self, context, number_of_channels, section_name):
        guild = context.guild
        # Create role-assign channel
        channels = guild.text_channels
        found = False
        for chnl in channels:
            if chnl.name == "role-assign":
                found = True
                break
        if not found:
            await guild.create_text_channel("role-assign")
            await context.send("role-assign channel created")

        try:
            category = ""
            # checks to see if a user is not an admin and tries to run the command, stop
            if not context.message.author.guild_permissions.administrator:
                await context.message.add_reaction('❌')
                await context.send("You cannot use this command, you are not an admin")
                return

            # checks to see if the category has already been created, if so set value to True
            list_of_cats = guild.categories
            valid = False
            for j in list_of_cats:
                if section_name.lower() == j.name.lower():
                    valid = True
                    category = j

            # creates the category if it does not exist. if it does exist, move on
            if valid == False:
                category = await guild.create_category_channel(section_name.lower())

            channel_number = int(number_of_channels)

            # creates the category name
            category_name = discord.utils.get(
                context.guild.categories, name=section_name.lower())

            data = firebase.DB_get(
                'servers/' + str(context.guild.id))
            try:
                created_roles = data.val()['createdroles'][category_name.name]
            except Exception:
                created_roles = []
            # if the channels are not created but the category is, adds them to the category
            change = False
            for i in range(channel_number):
                if i < 25:
                    category_channels = category.channels

                    if discord.utils.get(category_channels, name=str(i+1)) is None:
                        change = True
                        createdrole = await guild.create_role(name=f'{section_name.lower()} {i + 1}')
                        created_roles.append(createdrole.name)
                        await asyncio.sleep(0.1)
                        specific_role = discord.utils.get(
                            guild.roles, name=f'{section_name.lower()} {i+1}')
                        overwrites = {
                            guild.default_role: discord.PermissionOverwrite(read_messages=False),
                            specific_role: discord.PermissionOverwrite(
                                read_messages=True)
                        }

                        # stops here, \/\/ breaks
                        await guild.create_text_channel(f'{i+1}', overwrites=overwrites, category=category_name)
                        await asyncio.sleep(0.1)
                        await guild.create_voice_channel(f'{i+1}', overwrites=overwrites, category=category_name)
                        await asyncio.sleep(0.1)

            if change:
                guild = context.guild
                # Get all class channels
                data = firebase.DB_get(
                    'servers/' + str(context.guild.id))
                try:
                    print(data.val()['createdroles'])
                except KeyError:
                    created_roles = []
                msg = "**Use the %join \"(name)\" (section#) to get the role. Ex: %join \"Math\" 4**\n"
                for key in data.val()['createdroles'].keys():
                    msg = msg + key + ' :::: '
                    count = 0
                    for roles in data.val()['createdroles'][key]:
                        count = count + 1
                    msg = msg + 'Groups 1-' + str(count) + '\n'
                # Send message to role-assign channel
                channels = guild.text_channels
                for chnl in channels:
                    if chnl.name == "role-assign":
                        await chnl.send(msg)
                        break

            list_to_dict = {}
            for j in range(len(created_roles)):
                list_to_dict[j] = created_roles[j]
            firebase.DB_set(list_to_dict,
                            'servers/' + str(context.guild.id) + '/createdroles/' + str(category_name.name))
            await context.message.add_reaction('✅')

        except ValueError:
            await context.message.add_reaction('❌')
            await context.send("the second argument needs to be an integer!")


def setup(bot):
    bot.add_cog(create_channel(bot))
