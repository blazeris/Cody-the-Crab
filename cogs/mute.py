from discord.ext import commands
import discord
from bot import firebase

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description = "Prevents non admin role from sending messages")
    async def hidetext(self, context):
        guild = context.guild
        roles = guild.roles
        for i in roles:
            if not i.permissions.administrator:
                permissions = i.permissions
                permissions.update(send_messages = False)
                try:
                    await i.edit(permissions = permissions)
                except Exception:
                    print("Nope")
        await context.send("Locked text channels")

    @commands.command(description = "Allows non admin role to send messages")
    async def revealtext(self, context):
        guild = context.guild
        roles = guild.roles
        for i in roles:
            if not i.permissions.administrator:
                permissions = i.permissions
                permissions.update(send_messages = True)
                try:
                    await i.edit(permissions = permissions)
                except Exception:
                    print("Nope")
        await context.send("Unlocked text channels")

    @commands.command(description = "Prevents non admin roles from entering voice channels")
    async def hidevoice(self, context):
        guild = context.guild
        roles = guild.roles
        for i in roles:
            if not i.permissions.administrator:
                permissions = i.permissions
                permissions.update(connect = False)
                try:
                    await i.edit(permissions = permissions)
                except Exception:
                    print("Nope")
        await context.send("Locked voice channels")

    @commands.command(description = "Allows non admin roles to enter voice channels")
    async def revealvoice(self, context):
        guild = context.guild
        roles = guild.roles
        for i in roles:
            if not i.permissions.administrator:
                permissions = i.permissions
                permissions.update(connect = True)
                try:
                    await i.edit(permissions = permissions)
                except Exception:
                    print("Nope")
        await context.send("Unlocked voice channels")


def setup(bot):
    bot.add_cog(Mute(bot))