import discord
from discord import embeds
from discord.errors import DiscordException
from discord.ext import commands
import random
import discord


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    rpg_message = ""

    @commands.command()
    async def rps(self, context):

        rpg_embed = discord.Embed(title='Rock Paper Scissors',
                                  description="choose your weapon")
        rpg_embed.set_image(url="https://i.imgur.com/EiN0hgE.png")

        message = await context.send(embed=rpg_embed)
        await message.add_reaction("✌️")
        await message.add_reaction("✊")
        await message.add_reaction("✋")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # ✌️ = 1, ✊ = 2, ✋ = 3
        if reaction.emoji != '✌️' and reaction.emoji != '✊' and reaction.emoji != '✋':
            return

        num = random.randrange(1, 3)

        if user.bot:
            return

        rpg_embed = discord.Embed(title='Rock Paper Scissors',
                                  description="choose your weapon")
        rpg_embed.set_image(url="https://i.imgur.com/EiN0hgE.png")

        sign = ""
        if num == 1:
            sign = "✌️"
        if num == 2:
            sign = "✊"
        if num == 3:
            sign = "✋"

        if reaction.emoji == '✌️':
            rpg_embed.add_field(name="RESULTS", value=f'(You) ✌️ vs {sign}')
            await reaction.message.edit(embed=rpg_embed)
            if num == 1:
                await reaction.message.channel.send("😑😑TIE😑😑")
            if num == 2:
                await reaction.message.channel.send("💀💀 YOU LOSE 💀💀")
                await reaction.message.channel.send("How did you lose? Clams don't have hands!")
            if num == 3:
                await reaction.message.channel.send("🥳🥳 YOU WIN 🥳🥳")

        if reaction.emoji == '✊':
            rpg_embed.add_field(name="RESULTS", value=f'(You) ✊ vs {sign}')
            await reaction.message.edit(embed=rpg_embed)
            if num == 1:
                await reaction.message.channel.send("🥳🥳 YOU WIN 🥳🥳")
            if num == 2:
                await reaction.message.channel.send("😑😑 TIE 😑😑")
            if num == 3:
                await reaction.message.channel.send("💀💀 YOU LOSE 💀💀")
                await reaction.message.channel.send("How did you lose? Clams don't have hands!")

        if reaction.emoji == "✋":
            rpg_embed.add_field(name="RESULTS", value=f'(You) ✋ vs {sign}')
            await reaction.message.edit(embed=rpg_embed)
            if num == 1:
                await reaction.message.channel.send("💀💀 YOU LOSE 💀💀")
                await reaction.message.channel.send("How did you lose? Clams don't have hands!")
            if num == 2:
                await reaction.message.channel.send("🥳🥳 YOU WIN 🥳🥳")
            if num == 3:
                await reaction.message.channel.send("😑😑TIE😑😑")

        if len(reaction.message.embeds) > 0:
            for embed in reaction.message.embeds:
                if embed.title == 'Rock Paper Scissors':
                    await reaction.message.clear_reactions()
                    return


def setup(bot):
    bot.add_cog(Test(bot))
