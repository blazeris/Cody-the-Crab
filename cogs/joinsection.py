from discord.ext import commands
import discord
from bot import firebase


class JoinSection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Joins a specific section\'s group')
    async def join(self, context, section_name, group_number):
        member = context.message.author
        role_name = str(section_name) + ' ' + str(group_number)
        roles = []
        data = firebase.DB_get('servers/' + str(context.guild.id))
        for key in data.val()['createdroles'].keys():
            for db_role in data.val()['createdroles'][key]:
                roles.append(db_role)
        server_role = discord.utils.get(context.guild.roles, name=role_name)
        if role_name in roles and server_role is not None:
            await member.add_roles(server_role)
            await context.message.add_reaction('✅')
        else:
            await context.message.add_reaction('❌')
            await context.channel.send('Invalid section and group number! Do %join <section name in quotes> <group number>')


def setup(bot):
    bot.add_cog(JoinSection(bot))
