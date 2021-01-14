import discord
from discord.utils import get
from discord.ext import commands
import nacl.utils

client = discord.Client()
bot = commands.Bot(command_prefix='')

marker = 0

@bot.event
async def on_ready():
    print('Connected!')
    #print('Username: {0.name}\nID: {0.id}'.format(client.user))


@bot.command()
async def join(ctx):
    print("ok")
    x = ctx.author.voice.channel
    print(x)
    await x.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(key)