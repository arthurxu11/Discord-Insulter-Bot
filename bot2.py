# Discord Bot
# Arthur Xu
# March 11th, 2020
# Simple discord bot that can send childish insults towards whoever the user desires.

import discord
import random
from discord.ext import commands

insults = [" hasn't even started his side projects yet smh", " dropped a dookie in his pants", " has ligma", " got blocked by Maggie", " wants to go into Computer Engineering", " got caught lacking", " sucks at Halo"]

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!insult'):
        if str(message.author) == "Specific Usertag":
            await message.channel.send("Shut up")
            return
        x = message.content
        insult = random.choice(insults)
        await message.channel.send(x[7:] + insult)

client.run('Your bot token here')
