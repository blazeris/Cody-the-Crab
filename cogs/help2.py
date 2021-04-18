from typing import Optional

from discord import Embed
from discord.utils import get
from discord.ext.menus import MenuPages, ListPageSource
from discord.ext.commands import Cog
from discord.ext.commands import command


def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []

    for key, value in command.params.items():
        if key not in ("self", "ctx","context", "cmd"):
            params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

    params = " ".join(params)

    return f"`{cmd_and_aliases} {params}`"


class HelpMenu(ListPageSource):
    def __init__(self, ctx, data):
        self.ctx = ctx

        super().__init__(data, per_page=4)

    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)

        embed = Embed(title="Welcome to our Help Menu!",
                      description="Click on the emojis to navigate through the menu!",
                      colour=self.ctx.author.colour)
        embed.set_thumbnail(url= "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fab2ce1a7-3074-410e-84ac-d44e78ae88cb%2FByte_the_Shark.png?table=block&id=f76f6edc-694f-497f-a793-716dcfc1e340&width=600&userId=&cache=v2")
        embed.set_footer(text=f"{offset:,} - {min(len_data-1, offset+self.per_page-1):,} of {len_data-1:,} commands.")


        for name, value in fields:
            if value != '`help `':
                embed.add_field(name=value, value=name, inline=False)
        return embed

    async def format_page(self, menu, entries):
        fields = []


        for entry in entries:
                fields.append((entry.description, syntax(entry)))
        return await self.write_page(menu, fields)
    


class Test(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    async def cmd_help(self, ctx, command):
        embed = Embed(title=f"Help with `{command}`",
                      description=syntax(command),
                      colour=ctx.author.colour)
        embed.add_field(name="Command description", value=command.description)
        await ctx.send(embed=embed)

    @command(name="help", description = "Opens the help menu!")
    async def show_help(self, ctx, cmd: Optional[str]):
        if cmd is None:
            menu = MenuPages(source=HelpMenu(ctx, list(self.bot.commands)),
                             delete_message_after=True,
                             timeout=60.0)
            await menu.start(ctx)

        else:
            if (command := get(self.bot.commands, name=cmd)):
                await self.cmd_help(ctx, command)

            else:
                await ctx.send("That command does not exist.")

    #@Cog.listener()
   # async def on_ready(self):
     #   if not self.bot.ready:
      #      self.bot.cogs_ready.ready_up("help")


def setup(bot):
    bot.add_cog(Test(bot))