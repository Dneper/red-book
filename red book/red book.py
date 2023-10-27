import discord
from discord.ext import commands
#import os, random

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default() )

@bot.event
async def on_ready():
    print('Я работаю')

@bot.command()
async def tulen(ctx):
    with open('images/tulen.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send('https://redbookrf.ru/kaspijskij-tyulen')

@bot.command()
async def poloz(ctx):
    with open('images/poloz.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send('https://redbookrf.ru/yaponskiy-poloz-elaphe-japonica')

@bot.command()
async def aist(ctx):
    with open('images/aist.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send('https://redbookrf.ru/chernyy-aist-ciconia-nigra')

@bot.command()
async def krab(ctx):
    with open('images/krab.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send('https://redbookrf.ru/yaponskiy-krab-charybdis-japonica')

@bot.command()
async def shmel(ctx):
    with open('images/shmel.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send('https://redbookrf.ru/shmel-otshelnik-bombus-anachoreta')

@bot.command()
async def kruzeshtern(ctx):
    with open('images/kruzeshtern.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send('https://redbookrf.ru/cherenok-kruzenshterna-solen-krusensterni')

bot.run('MTE1OTg3OTg3NzExODQwMjU3Mg.Gmus-1.HX5kw4bxhaE4l3udTejq6UNpnsENu_Nzba0c4Q')