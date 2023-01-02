import os
import memory

import discord
from commands_func import *

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
mute_handle = Mute(**kwarg_send, timeout=10)
stats_handle = Stats(**kwarg_send)
help_handle = Help(**kwarg_send)


# This will store different commands and stuff
commands = {
    "-": ranking_handle.sub,
    "+": ranking_handle.add,
    "!name": name_handle.name,
    "!ranking": ranking_handle.ranking,
    "!cite": citation_handle.cite,
    "!votes_by": history_handle.cast_by_user,
    "!votes_on": history_handle.cast_on_user,
    "!mute": mute_handle.mute_user,
    "!unmute": mute_handle.unmute_user,
    "!stats": stats_handle.stats,
    "!help": help_handle.run,
}

# Should detect when a member changes its status.
@client.event
async def on_member_update(user_before, user_after):
    user_alias = memory_handle.id_to_name(user_after.id)

    # Needs some data structure keeping track of the time a specific user last went online
    # (this data structure could be done using the database, adding the last time the user went from offline to online in the database would give some time bugs if the bot went down for a longer period of time however)
    # Then when getting an update from online to anything else we can delta now with that saved datetime
    # This will give us how long they were online for and can thus be added to the users global score

    print(f"{user_alias} changed their status!")

# If something happens on discord
@client.event
# If this something is a message
async def on_message(message):
    # print(message.author.id)
    # This is just so the bot does not answer itself and become a loop
    if message.author == client.user:
        return

    if str(message.guild) == GUILD:
        if mute_handle.is_muted(message.author.id):
            print(f"removed message from muted user: {message.author.name}")
            # delete message
            await message.delete()
            return

        # Counting messages sent by users
        memory_handle.sent_messages_points(user_id=str(message.author.id), points=1)

        # If the command is made with arg
        if " " in message.content and message.content.split()[0] in commands:
            await commands[message.content.split()[0]](message)

        # If the command does not have any args
        elif message.content in commands:
            await commands[message.content](message)


client.run(TOKEN)
