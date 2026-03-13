import discord
import os
from discord.ext import commands
from model import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


def mensajeVerficacion(clase, conf):
    if conf < 0.7:
        return f"Prediccion: {clase} ({conf*100:.1f}%) - Lo siento, no estoy seguro de lo que se muestra en la imagen"
    else:
        if clase == "Crochet":
            return f"Prediccion: {clase} ({conf*100:.1f}%) - Estoy seguro de esta prediccion, es un crochet"
        elif clase == "CrochetIA":
            return f"Prediccion: {clase} ({conf*100:.1f}%) - Estoy seguro de esta prediccion, es un crochet hecho por IA"
    


@bot.command()
async def check(ctx):
    try:
        if ctx.message.attachments:
            for image in ctx.message.attachments:
               f_name = image.filename
               f_url = image.url
               nameIMG = f"image_{verificarImage()}.png"
               await image.save(f"images/{nameIMG}")
               mensaje = mensajeVerficacion(*getclass(f'images/{nameIMG}'))
               await ctx.send(mensaje)
        else:
            await ctx.send("No se ha adjuntado ninguna imagen")
    except Exception as e:
        await ctx.send(f"Error: {e}")
    
    
def verificarImage():
    temp = 0
    for filename in os.listdir("images"):
        name = filename.split("_")
        number = int(name[1].split(".")[0])
        if number > temp:
            temp = number

    return temp+1



bot.run("TOKEN")
