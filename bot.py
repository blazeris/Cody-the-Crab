import discord
import os
import firebase_connect as fb
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='%')
firebase = fb.FirebaseConnection()


@client.event
async def on_ready():
    print('Connected')


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
