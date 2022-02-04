from itertools import count
import memory

import os

import discord
from dotenv import load_dotenv

# This is just config stuff: Token, what server to write to, what channel to use for io
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = "general"

# Creating a obj for the memory and stuff
top_list = memory.Stats()

# This is the handle to the discord api
client = discord.Client()

# If something happens on discord
@client.event
# If this something is a message
async def on_message(message):
    # This is just so the bot does not answer itself and become a loop
    if message.author == client.user:
        return

    # If !stats is written, it will print all the points for each person. The other stuff is for formating
    if message.content == "!stats":
        response = "-----------------------\n"
        counter = 1
        for person in top_list.get_list():
            response += "| " +"\#" + str(counter) + " " + top_list.get_stat(person)
            counter += 1
        response += "-----------------------"
        await message.channel.send(response)
    
    # This is supposed to be the part where you can add and subtract points from each other
    # This does not work so good, the problem is that the name will not always be capitalized
    elif message.content != None and str(client.get_channel(message.channel.id)) == CHANNEL:
        # If rating is - the subtract function will run
        if message.content[0] == "-":
            # if there is a cap between - and name
            if message.content[1] == " ":
                top_list.subtract(str(message.content.split()[1]))
            else:
                top_list.subtract(str(message.content.split()[0][1:]))
            
            response = "updated"
        # If rating is + the add function will run
        elif message.content[0] == "+":
            if message.content[1] == " ":
                top_list.add(str(message.content.split()[1]))
            else:
                top_list.add(str(message.content[1:]))

            response = "updated"
        try:
            # This is the message that will be sent if the command was recognized
            await message.channel.send(response)
        except:
            # If not recognized message
            pass

client.run(TOKEN)
