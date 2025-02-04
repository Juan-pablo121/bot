import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')   
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def clave(ctx ,count_pass=10):
    await ctx.send(gen_pass(count_pass))
@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())
@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())        
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def decir(ctx, palabra=''):
    await ctx.send(palabra)


bot.run("Escribe aqui tu token")



