import os
import memory

import discord
from commands_func import Ranking, Citation, Name, Stats, History, Mute

# Had this for the intent
from dotenv import load_dotenv

# This is just config stuff: Token, what server to write to, what channel to use for io
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("GUILD")
CHANNEL_RATING = "rating"


# Creating a obj for the memory and stuff
memory_handle = memory.Memory()

# This is the handle to the discord api
client = discord.Client(intents=discord.Intents.all())

# Just packed together so it is easy to send as kwarg
kwarg_send = {"channel_rating": CHANNEL_RATING, "memory_handle": memory_handle}

# All class declarations for the commands package
ranking_handle = Ranking(**kwarg_send)
citation_handle = Citation(**kwarg_send)
name_handle = Name(**kwarg_send)
history_handle = History(**kwarg_send)
mute_handle = Mute(**kwarg_send)
stats_handle = Stats(**kwarg_send)


# This will store different commands and stuff
commands = {
    "-": ranking_handle.sub,
    "+": ranking_handle.add,
    "!name": name_handle.name,
    "!ranking": ranking_handle.ranking,
    "!cite": citation_handle.cite,
    "!votes_by": history_handle.cast_by_user,
    "!votes_on": history_handle.cast_on_user,
    "!mute" : mute_handle.mute_user,
    "!unmute" : mute_handle.unmute_user,
    "!stats": stats_handle.stats,
}


# If something happens on discord
@client.event
# If this something is a message
async def on_message(message):
    #print(message.author.id)
    # This is just so the bot does not answer itself and become a loop
    if message.author == client.user:
        return

    if str(message.guild) == GUILD:
        if mute_handle.is_muted(message.author.id):
            print(f"removed message from muted user: {message.author.name}")
            # delete message
            await message.delete()
            return

        # Here it should be a counter for messages sent on the server.

        # If there is a image, this will throw a error
        # list index out of range
        memory_handle.messageSend(message)

        # If the command is made with arg
        if ' ' in message.content and message.content.split()[0] in commands:
            await commands[message.content.split()[0]](message)
        
        # If the command does not have any args
        elif message.content in commands:
            await commands[message.content](message)


client.run(TOKEN)
