from discord.ext import commands
from bot import firebase


class get_sections(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getsections(self, context):
        guild = context.guild
        data = firebase.DB_get('servers/' + str(context.guild.id) + '/createdroles')
        for roleset in data.each():
            category_name = roleset.key()
            roles = roleset[category_name]
        categories = guild.categories



def setup(bot):
    bot.add_cog(get_sections(bot))