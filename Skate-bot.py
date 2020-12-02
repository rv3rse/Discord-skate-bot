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

bot = commands.Bot(command_prefix = my_dict['command-prefix'], intents=intents)
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

	await ctx.send("Welcome to S-K-A-T-E!")

	time.sleep(2)

	async def difficulty():

		await ctx.send('\nWhich difficulty would you like to play: \n - beginner \n - intermediate \n - advanced')

		while True:

			respone1 = await bot.wait_for('message')
			answer1 = str(respone1.content)

			if answer1 == 'beginner':

				await beginner()
				break

			elif answer1 == 'intermediate':

				await intermediate()
				break

			elif answer1 == 'advanced':

				await advanced()
				break

			else:

				await ctx.send('Not a valid difficulty.')

				break

	async def beginner():

		score = 0
		beginner_play = True

		while beginner_play:


			beginner_line = random.choice(beginnerTricks) + ' ~ ' + random.choice(a_grinds)
			beginner_line2 = random.choice(beginnerTricks) + ' ~ ' + random.choice(b_manuals)

			beginnerskate = random.choice([beginner_line, beginner_line2])

			await ctx.send(f"\nHere is your trick: {beginnerskate}")

			await ctx.send("\nDid you land the trick: ")

			response = await bot.wait_for('message')
			answer = str(response.content)

			if answer == 'yes':
				score = score + 1

			elif answer == 'no':
				await ctx.send(f'That was a great attempt! Your score is {score}.')
				beginner_play = False

			else:
				await ctx.send('Don\'t understand, exiting game.')
				beginner_play = False


	async def intermediate():

		score = 0
		intermediate_play = True

		while intermediate_play:

			intermediate_line = random.choice(intermediateTricks) + ' ~ ' + random.choice(a_manuals)
			intermediate_line2 = random.choice(intermediateTricks) + ' ~ ' + random.choice(a_grinds)

			intermediateskate = random.choice([intermediate_line, intermediate_line2])

			await ctx.send(f"\nHere is your trick: {intermediateskate}")

			await ctx.send("Did you land the trick: ")

			response2 = await bot.wait_for('message')
			answer2 = str(response2.content)

			if answer2 == 'yes':
				score = score + 1

			elif answer2 == 'no':
				await ctx.send(f"That was a great attempt! Your score is {score}.")
				intermediate_play = False

			else:
				await ctx.send("Don\'t understand, exiting game.")

	async def advanced():

		score = 0
		advanced_play = True

		while advanced_play:

				advanced_line = random.choice(advancedTricks) + ' ~ ' + random.choice(a_manuals)
				advanced_line2 = random.choice(advancedTricks) + ' ~ ' + random.choice(a_grinds)

				advancedskate = random.choice([advanced_line, advanced_line2])

				await ctx.send(f"Here are your tricks: {advancedskate}")

				await ctx.send("Did you land it: ")

				response3 = await bot.wait_for('message')
				answer3 = str(response3.content)

				if answer3 == 'yes':
					score = score + 1

				elif answer3 == 'no':
					await ctx.send(f'That was a great attempt! Your score is {score}.')
					advanced_play = False

				else:
					await ctx.send("Don\'t understand, exiting game.")
					advanced_play = False





	await difficulty()


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

**__S-K-A-T-E Game:__**

\t.skate - This starts the game of S-K-A-T-E, choose your difficulty and try to achieve a high score! Honesty is key.
""")

bot.run(my_dict['bot-token'])