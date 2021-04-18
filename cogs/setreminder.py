from discord.ext import commands, tasks
from bot import firebase
import datetime


class SetReminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.checktime.start()

    @commands.command(description='setreminder <date in MM/DD/YY> <time in 12:34:PM> <message in quotes>')
    async def setreminder(self, context, arg1, arg2, arg3):
        self.message = arg3
        date = arg1.split("/")
        try:
            month = int(date[0])
            day = int(date[1])
            year = int("20" + date[2])
        except IndexError:
            await context.send("Invalid date format, setreminder <date in MM/DD/YY> <time in 12:34:PM> <message in quotes>")
            return
        time = arg2.split(":")
        try:
            hour = int(time[0])
            minute = int(time[1])
            if(time[2].lower() == "pm"):
                hour = hour + 12
        except IndexError:
            await context.send("Invalid time format, setreminder <date in MM/DD/YY> <time in 12:34:PM> <message in quotes>")
            return

        setdatetime = datetime.datetime(
            year, month, day, hour=hour, minute=minute)

        if(setdatetime <= datetime.datetime.now()):
            await context.message.add_reaction('❌')
            await context.send("Hey, that's in the past!")
        else:
            data = {'msg': self.message, 'year': year, 'month': month,
                    'day': day, 'hour': hour, 'minute': minute}
            firebase.DB_set(data, "servers/" +
                            str(context.guild.id) + "/reminders/" + str(context.author.id) + str(datetime.datetime.now().strftime('%f')))
            await context.message.add_reaction('✅')

    @tasks.loop(seconds=30)
    async def checktime(self):
        data = firebase.DB_get(
            "servers")

        if data is None or data.each() is None:
            return

        for set in data.each():
            try:
                for reminderKey in set.val()['reminders'].keys():
                    reminder = set.val()['reminders'][reminderKey]
                    reminder_datetime = datetime.datetime(
                        reminder['year'], reminder['month'], reminder['day'], hour=reminder['hour'], minute=reminder['minute'])
                    message = reminder['msg']
                    time_diff = datetime.datetime.now() - reminder_datetime
                    if time_diff.total_seconds() < 15 and time_diff.total_seconds() >= -15:
                        await self.sendMessage(set.key(), message)
                    if time_diff.total_seconds() > 15:
                        firebase.DB_remove(
                            "servers/" + set.key() + "/reminders/" + reminderKey)
            except Exception:
                pass

    async def sendMessage(self, serverID, msg):
        # guild = await self.bot.fetch_guild(serverID)
        for g in self.bot.guilds:
            if g.id == int(serverID):
                guild = g
        if guild.system_channel:
            await guild.system_channel.send("@here " + msg)


def setup(bot):
    bot.add_cog(SetReminder(bot))
    print("setreminder loaded")
