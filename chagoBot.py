import discord
from discord.ext import commands
import random
import asyncio
from PIL import Image
import os, time
from myToken import getToken

# get PATH
cwd = os.getcwd()

# Bot settings
client = commands.Bot(command_prefix = '.', help_command=None)
myToken = getToken()

@client.event
async def on_ready():
	print('Funciono :D')

@client.command()
async def chago(ctx, numI = None):

	# Validación argumento nulo
	if numI is None:
		numI = 1

	# Excepción para strings
	try:
		numI = int(numI)
	except Exception as e:

		foto = numI.lower()

		if foto == 'independiente':
			imageName = "4.jpg"
		elif foto == 'mamado':
			imageName = "3.jpg"
		elif foto == 'xxx':
			imageName = "7.jpg"
		elif foto == 'goku':
			imageName = "138266441_1496074330590252_989026040913170683_n.png"
		elif foto == 'cafe':
			imageName = "6.jpg"
		elif foto == 'puto':
			await ctx.send('Lo que se ve no se pregunta')
			
		else :
			await ctx.send('No encontre la foto mi lord')



		imagesDir = cwd + '\\imagenes\\' + imageName
		imagen = Image.open(imagesDir)

		# Save the image
		imagen.save(imageName)

		# Display the image
		await ctx.send(file = discord.File(imageName))

		# Delete image
		# time.sleep(1)
		os.remove(imageName)

		return

	# Validación numeros grandes o negativos
	if (numI > 5) or (numI <= 0):
		await ctx.send('No mames')
		return



	for _ in range(numI):

		# list of images
		contenido = os.listdir(cwd + '\\imagenes')

		# Random number
		aleatorio = random.randint(1,len(contenido))

		# get the image name
		imageName = contenido[aleatorio - 1]
		imagesDir = cwd + '\\imagenes\\' + imageName
		imagen = Image.open(imagesDir)

		# Save the image
		imagen.save(imageName)

		# Display the image
		await ctx.send(file = discord.File(imageName))

		# Delete image
		# time.sleep(1)
		os.remove(contenido[aleatorio - 1])


# Chago game
@client.command()
async def chagame(ctx):

	# list of images
	contenido = os.listdir(cwd + '\\chagame')

	# Random number
	aleatorio = random.randint(1,len(contenido))

	# get the image name
	imageName = contenido[aleatorio - 1]
	imagesDir = cwd + '\\chagame\\' + imageName
	imagen = Image.open(imagesDir)

	# Save the image
	imagen.save(imageName)

	# Display the image
	await ctx.send(file = discord.File(imageName))

	# Delete image
	# time.sleep(1)
	os.remove(contenido[aleatorio - 1])


# Help command
@client.command(pass_context = True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.dark_gold()
	)

	embed.set_author(name='Help')
	embed.add_field(name='.chagame', value='Carta random del juego de Shhhhhhaguitooo')
	embed.add_field(name='.chago', value='1 Imagen random del Dios Chago')
	embed.add_field(name='.chago <numero>', value='Varias imagenes random del Dios Chago (numero entre 1 y 5)')
	embed.add_field(name='.chago <palabra>', value='Imagen especifica del Dios Chago')
	embed.add_field(name='Palabras para imagenes de chago', value='independiente\nmamado\nxxx\ngoku\ncafe\nputo')

	await ctx.send(embed=embed)

# Close the bot
@client.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def close(ctx):
	await ctx.send('Adios we\nSi me quieres activar de nuevo hablale a Roberto')
	await client.close()
	print("Bot Closed")  # This is optional, but it is there to tell you.

client.run(myToken)
