import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import DMChannel
import json
import random

with open("Skate-bot-settings.json", "r") as f:
	my_dict = json.load(f)

#Sets the bots command prefix and also states what channel it will be active in.

bot = commands.Bot(command_prefix = my_dict['command_prefix'])
#channel = bot.get_channel(my_dict['channel_id'])

#Notifies you that the bot is ready in the terminal.

@bot.event
async def on_ready():
	print("Skate bot is ready!")

#List of skate tricks for the "Game of skate"

beginnerTricks = ['kickflip', 'heelflip', 'fs 180', 'bs 180', 'fs shuv-it', 'bs shuv-it']

intermediateTricks = ['hardflip', 'variel flip', 'variel heel', 'tre flip', '360 shuv-it', 'lazer flip', 'nollie kickflip',
'nollie heelflip', 'nollie tre', 'inward heelflip',]

advancedTricks = ['forward kickflip', 'forward heelflip', 'nollie hardflip', 'nollie 360 hardflip', 'nollie variel flip', 'double flip',
'double heelflip', 'double variel heel', 'double variel flip', '360 hardflip']

grinds = ['nose grind', 'willy grind', 'feeble grind', 'crooked grind', '50-50 grind', 'tail slide', 'board slide', 'bs blunt slide',
'fs blunt slide', 'nose slide', 'nose blunt slide']

b_manuals = ['manual', 'nose manual']
a_manuals = ['manual', 'nose manual', 'manual revert']

@bot.command()
async def beginner(ctx):
	await ctx.send(random.choice(beginnerTricks))

@bot.command()
async def intermediate(ctx):
	await ctx.send(random.choice(intermediateTricks))

@bot.command()
async def advanced(ctx):
	await ctx.send(random.choice(advancedTricks))

@bot.command()
async def beginnerline(ctx):
	beginner_line = random.choice(beginnerTricks) + ' ~ ' + random.choice(grinds)
	beginner_line2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

	await ctx.send(random.choice([beginner_line, beginner_line2]))

@bot.command()
async def intermediateline(ctx):
	intermediate_line = random.choice(intermediateTricks) + ' ~ ' + random.choice(a_manuals)
	intermediate_line2 = random.choice(intermediateTricks) + ' ~ ' + random.choice(grinds)

	await ctx.send(random.choice([intermediate_line, intermediate_line2]))

@bot.command()
async def advancedline(ctx):
	advanced_line = random.choice(advancedTricks) + ' ~ ' + random.choice(a_manuals)
	advanced_line2 = random.choice(advancedTricks) + ' ~ ' + random.choice(grinds)

	await ctx.send(random.choice([advanced_line, advanced_line2]))

#This is the command that shows all the available commands the bot currently has and how to call them.

@bot.command()
async def commandhelp(ctx):
	await ctx.send(
"""
```
Hello! You can use commands by using ".examplecommand".

These are the current commands the bot has:

Just tricks:

.beginner - This gives you a random beginner trick. E.g: kickflip.

.intermediate - This gives you a random intermediate trick. E.g: Variel flip.

.advanced - This gives you a random advanced trick. E.g: Double hardflip.

lines:

.beginnerline - This gives a random beginner line. E.g: Kickflip ~ Nose manual.

.intermediateline - This gives a random intermediate line. E.g: Hardflip ~ Crooked grind.

.advancedline - This gives a random advanced line. E.g: Forward kickflip ~ Manual revert.
``` 
""")

bot.run(my_dict['bot-token'])