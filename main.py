import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Lista de saludos
saludos = [
    "¡Hola!", 
    "¡Qué tal!", 
    "¡Saludos!", 
    "¡Hola, hola!", 
    "¡Buen día!",
    "¡Hey!",
    "¡Qué onda!"
]

@bot.event
async def on_ready():
    print(f'{bot.user} se ha conectado a Discord!')

@bot.command(name='hola')
async def hola(ctx):
    saludo_aleatorio = random.choice(saludos)
    await ctx.send(f'{saludo_aleatorio} {ctx.author.name}')
