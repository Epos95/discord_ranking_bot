import os
import memory

import discord
import datetime
import commands_func
# Had this for the intent
#from discord.ext import commands
from dotenv import load_dotenv

# This is just config stuff: Token, what server to write to, what channel to use for io
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
CHANNEL_RATING = "rating"


# Creating a obj for the memory and stuff
memory_handle = memory.Stats()

# This is the handle to the discord api
client = discord.Client()

# Just packed together so it is easy to send as kwarg
kwarg_send = {"channel_rating": CHANNEL_RATING, "memory_handle":memory_handle}

ranking_handle = commands_func.Ranking(**kwarg_send)
citation_handle = commands_func.Citation(**kwarg_send)


# This will store different commands and stuff
commands = {
    "-": ranking_handle.sub,
    "+": ranking_handle.add,
    "!name": top_list.change_name,
    "!ranking": ranking_handle.ranking,
    "!cite": citation_handle.cite
} 

# If something happens on discord
@client.event
# If this something is a message
async def on_message(message):
    # This is just so the bot does not answer itself and become a loop
    if message.author == client.user:
        return

    # Print author
    #print(message.author.id)

    # Just making sure that the bot only uses one server on discord
    if str(message.guild) == GUILD:
        # Once methods are rewritten a bit the commands structure can be even more generic in such a way that:

        if message.content.split()[0] in commands:
                await commands[message.content.split()[0]](message)




        # To see if its a reply of a previous message
        #print(message.reference)            

        """
         elif message.content.split()[0] == "!alias":
            print("alias")
        
        elif message.content.split()[0] == "!name":
            if commands[message.content.split()[0]](str(message.author.id), message.content.split()[1]):
                response = f"Your new name is {message.content.split()[1]}"
            else:
                response = f"{message.content.split()[1]} is not avalible"

            await message.channel.send(response)
        
        elif message.content.split()[0] == "!ping":
            # This does not work, because of timezones
            time_sent = int(message.created_at.strftime("%y%m%d%H%M%S%f")) // 100
            time_now = int(datetime.datetime.now().strftime("%y%m%d%H%M%S%f"))//100
            print(f"{(time_now-time_sent)} ")
            print(f"now {time_now} before {time_sent}")
        

    else:
        pass

        #print(f"Message sent in {message.guild}")
    """
client.run(TOKEN)