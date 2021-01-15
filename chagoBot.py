import discord
from discord.ext import commands
import random
import asyncio
from PIL import Image
from io import BytesIO

client = commands.Bot(command_prefix = '.')
myToken = 'Nzk4MDA1NDE0MDIwOTA3MDM4.X_uudA.Q7PBJqCVYfiUqehtVZ6EdageIN4'

@client.event
async def on_ready():
	print('Funciono :D')

@client.command()
async def chago(ctx):
	aleatorio = random.randint(1,7)
	nombreImagen = str(aleatorio) + ".jpg"
	imagen = Image.open('C:\\Users\\rober\\Desktop\\chagoBot\imagenes\\' + nombreImagen)
	imagen.save("profile.jpg")
	await ctx.send(file = discord.File("profile.jpg"))

client.run(myToken)