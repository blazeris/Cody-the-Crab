from discord.ext import commands
from bot import firebase


class get_sections(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description = "Gets all the class sections/roles and messages the 'role-assign' channel")
    async def getsections(self, context):
        guild = context.guild
        #Get all class channels
        data = firebase.DB_get(
            'servers/' + str(context.guild.id))
        try:
            print(data.val()['createdroles'])
        except KeyError:
            created_roles = []
        msg = "**Use the %join (name) (section#) to get the role. Ex: %joinsection Math 4**\n"
        for key in data.val()['createdroles'].keys():
            msg = msg + key + ' :::: '
            count = 0
            for roles in data.val()['createdroles'][key]:
                count = count + 1
            msg = msg + 'Groups 1-' + str(count) + '\n'
        #Send message to role-assign channel
        channels = guild.text_channels
        for chnl in channels:
            if chnl.name == "role-assign":
                await chnl.send(msg)
                break
        await context.send('Roles sent to "role-assign" channel')



def setup(bot):
    bot.add_cog(get_sections(bot))