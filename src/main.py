import os
import memory

import discord
from commands_func import Ranking, Citation, Name

# Had this for the intent
from dotenv import load_dotenv

# This is just config stuff: Token, what server to write to, what channel to use for io
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("GUILD")
CHANNEL_RATING = "rating"


# Creating a obj for the memory and stuff
memory_handle = memory.Stats()

# This is the handle to the discord api
client = discord.Client()

# Just packed together so it is easy to send as kwarg
kwarg_send = {"channel_rating": CHANNEL_RATING, "memory_handle": memory_handle}

# All class declarations for the commands package
ranking_handle = Ranking(**kwarg_send)
citation_handle = Citation(**kwarg_send)
name_handle = Name(**kwarg_send)


# This will store different commands and stuff
commands = {
    "-": ranking_handle.sub,
    "+": ranking_handle.add,
    "!name": name_handle.name,
    "!ranking": ranking_handle.ranking,
    "!cite": citation_handle.cite,
}

# If something happens on discord
@client.event
# If this something is a message
async def on_message(message):
    # This is just so the bot does not answer itself and become a loop
    if message.author == client.user:
        return

    if str(message.guild) == GUILD:

        # Here it should be a counter for messages sent on the server.

        # If there is a image, this will throw a error
        # list index out of range
        if message.content.split()[0] in commands:
            await commands[message.content.split()[0]](message)


client.run(TOKEN)
