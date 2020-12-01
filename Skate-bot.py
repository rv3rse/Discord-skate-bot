import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import random
import time

with open("Skate-bot-settings.json", "r") as f:
	my_dict = json.load(f)

intents = discord.Intents.default()
intents.members = True

#Sets the bots command prefix and also states what channel it will be active in.

bot = commands.Bot(command_prefix = my_dict['command_prefix'], intents=intents)
channel = bot.get_channel("781631030972514335")

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

a_grinds = ['nose grind', 'willy grind', 'feeble grind', 'crooked grind', '50-50 grind', 'tail slide', 'board slide', 'bs blunt slide',
'fs blunt slide', 'nose slide', 'nose blunt slide']

b_manuals = ['manual', 'nose manual']
a_manuals = ['manual', 'nose manual', 'manual revert']

@bot.command()
async def grinds(ctx):
	await ctx.send(random.choice(a_grinds))

@bot.command()
async def manuals(ctx):
	await ctx.send(random.choice(a_manuals + b_manuals))

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
	beginner_line = random.choice(beginnerTricks) + ' ~ ' + random.choice(a_grinds)
	beginner_line2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

	await ctx.send(random.choice([beginner_line, beginner_line2]))

@bot.command()
async def intermediateline(ctx):
	intermediate_line = random.choice(intermediateTricks) + ' ~ ' + random.choice(a_manuals)
	intermediate_line2 = random.choice(intermediateTricks) + ' ~ ' + random.choice(a_grinds)

	await ctx.send(random.choice([intermediate_line, intermediate_line2]))

@bot.command()
async def advancedline(ctx):
	advanced_line = random.choice(advancedTricks) + ' ~ ' + random.choice(a_manuals)
	advanced_line2 = random.choice(advancedTricks) + ' ~ ' + random.choice(a_grinds)

	await ctx.send(random.choice([advanced_line, advanced_line2]))

@bot.command()
async def ping(ctx):

	await ctx.send(f'pong! {round(bot.latency * 1000)}ms')

# Spot of the week (SOTW)

@bot.command()
async def SOTW(ctx):

	await ctx.send("\tSpot of the week: Easy Day High School!", file=discord.File("EasyDay.png"))

# Game of skate


@bot.command()
async def skate(ctx):

	beginner_line = random.choice(beginnerTricks) + ' ~ ' + random.choice(a_grinds)
	beginner_line2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

	beginnerskate = random.choice([beginner_line, beginner_line2])

	await ctx.send("Welcome to the game of skate with a twist!")
	time.sleep(3)
	await ctx.send("\nWhat is your name: ")
	time.sleep(3)

	response = await bot.wait_for('message')
	name = str(response.content)

	await ctx.send(f"\nWelcome to the game {name}!")
	time.sleep(3)
	await ctx.send("\nWhich difficulty would you like: \n - beginner \n - intermediate \n - advanced")
	time.sleep(3)

	choice = await bot.wait_for('message')
	difficulty = str(choice.content)


	if difficulty == 'beginner':

		await ctx.send(f"Here is your first trick, try not to fail: {beginnerskate}")
		time.sleep(3)
		await ctx.send('Did you complete the trick first try: ')

		response2 = await bot.wait_for('message')
		answer = str(response2.content)

		if answer == 'yes':

			beginner_line = random.choice(beginnerTricks) + ' ~ ' + random.choice(a_grinds)
			beginner_line2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

			beginnerskate2 = random.choice([beginner_line, beginner_line2])

			await ctx.send('Well done! Your points: 1!')
			time.sleep(3)
			await ctx.send(f'Here\'s another trick: {beginnerskate2}')
			time.sleep(3)
			await ctx.send('Did you complete the trick: ')

			response3 = await bot.wait_for('message')
			answer2 = str(response3.content)

			if answer2 == 'yes':

				beginner_line = random.choice(beginnerTricks) + ' ~ ' + random.choice(a_grinds)
				beginner_line2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

				beginnerskate3 = random.choice([beginner_line, beginner_line2])

				await ctx.send('Well done! Your points: 2!')
				time.sleep(3)
				await ctx.send(f'Here\'s another trick: {beginnerskate3}')
				time.sleep(3)
				await ctx.send('Did you complete the trick: ')

				response4 = await bot.wait_for('message')
				answer3 = str(response4.content)

				if answer3 == 'yes':

					beginner_line = random.choice(beginnerTricks) + ' ~ ' + random.choice(a_grinds)
					beginner_line2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

					beginnerskate4 = random.choice([beginner_line, beginner_line2])

					await ctx.send('Well done! Your points: 3!')
					time.sleep(3)
					await ctx.send(f'Here\'s another trick: {beginnerskate4}')
					time.sleep(3)
					await ctx.send('Did you complete the trick: ')

					response5 = await bot.wait_for('message')
					answer4 = str(response5.content)

					if answer4 == 'yes':

						await ctx.send('Well done! Your total points: ')
						time.sleep(3)
						await ctx.send(f'You win, {name}!')






# This shows the team roster

@bot.command()
async def roster(ctx):
	await ctx.send(
		"""
**Wülfpack Team Roster:**

**__Managers:__** Jake, Hans.

**__Editors:__** Landon, Josh.

**__Social media managers:__** Austin, Breon.

**__Scouts:__** Brandon, Austin, Breon.

**__Pro skaters:__** Jake, Austin, Breon, Landon, Josh, Hans, Brandon, Adam, Kasai, Kyle, Niko, Daryien and Ryan.

Feel free to contact any of us with any questions or queries.
		""")

# This is the command that shows all the available commands the bot currently has and how to call them.

@bot.command()
async def commandhelp(ctx):
	await ctx.send(
"""
**Hello! You can use commands by using ".examplecommand".**

These are the current commands the bot has:

**__Tricks__**:

\t.beginner - This gives you a random beginner trick. E.g: kickflip.

\t.intermediate - This gives you a random intermediate trick. E.g: Variel flip.

\t.advanced - This gives you a random advanced trick. E.g: Double hardflip.

\t.grinds - This gives you a random grind. E.g: Crooked grind.

\t.manuals - This gives you a random manual. E.g: Nose manual.

**__lines__**:

\t.beginnerline - This gives a random beginner line. E.g: Kickflip ~ Nose manual.

\t.intermediateline - This gives a random intermediate line. E.g: Hardflip ~ Crooked grind.

\t.advancedline - This gives a random advanced line. E.g: Forward kickflip ~ Manual revert.

**__Roster:__**

\t.roster - This shows everyone on the leadership team.

**___Spot of the week:__**

\t.SOTW - This shows the spot of the week challenge.

**__Ping__**:

\t.ping - This shows the ping from the bot to the server in milliseconds.
""")

bot.run(my_dict['bot-token'])