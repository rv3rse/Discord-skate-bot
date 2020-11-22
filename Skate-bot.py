import discord
from discord.ext import commands
from discord.ext import Bot
from discord import DMChannel
import json
import random

with open("Skate-bot-settings", "r") as f:
	my_dict = json.load(f)

#Sets the bots command prefix and also states what channel it will be active in.

bot = commands.Bot(command_prefix = my_dict['command_prefix'])
channel = bot.get_channel(my_dict['channel_id'])

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

@bot.command
async def beginner(ctx):
	await ctx.send(random.choice(beginnerTricks))

@bot.command()
async def intermediate(ctx):
	await ctx.send(random.choice(intermediateTricks))

@bot.command()
async def advanced(ctx):
	await.ctx.send(random.choice(advancedTricks))

@bot.command()
async def beginner-line(ctx):
	beginnerline = random.choice(beginnerTricks) + ' ~ ' + random.choice(grinds)
	beginnerline2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

	await ctx.send(random.choice([beginnerline, beginnerline2]))

@bot.command()
async def intermediate-line(ctx):
	intermediateline = random.choice(intermediate) + ' ~ ' + random.choice(a_manuals)
	intermediateline2 = random.choice(intermediate) + ' ~ ' + random.choice(grinds)

	await ctx.send(random.choice([intermediateline, intermediateline2]))

@bot.command()
async def advanced-line(ctx):
	advancedline = random.choice(advanced) + ' ~ ' + random.choice(a_manuals)
	advancedline2 = random.choice(advanced) + ' ~ ' + random.choice(grinds)

	await ctx.send(random.choice([advancedline, advancedline2]))

#This is the command that shows all the available commands the bot currently has and how to call them.

@bot.command()
async def command-help(ctx):
	await ctx.send(
"""
```
Hello! You can use commands by using ".examplecommand".

These are the current commands the bot has:

Just tricks:

.Beginner - This gives you a random beginner trick. E.g: kickflip.

.Intermediate - This gives you a random intermediate trick. E.g: Variel flip.

.Advanced - This gives you a random advanced trick. E.g: Double hardflip.

lines:

.Beginnerline - This gives a random beginner line. E.g: Kickflip ~ Nose manual.

.Intermediateline - This gives a random intermediate line. E.g: Hardflip ~ Crooked grind.

.Advancedline - This gives a random advanced line. E.g: Forward kickflip ~ Manual revert.
``` 
""")

bot.run(my_dict['bot-token'])