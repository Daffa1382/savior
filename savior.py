import discord
from discord.ext import commands
import asyncio

TOKEN = 'NjY4MzE4MzI5MTM5NzU3MDU3.XixJxw.PRnIej9dr2WSQtOqbjssllfsgSM'


client = commands.Bot(command_prefix = 's!'


@client.event()
async def on_ready():
    print('login as savior')


@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong:Pong!')

client.run(TOKEN)
