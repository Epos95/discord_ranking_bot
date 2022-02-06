import memory
import os

import discord
# Had this for the intent
#from discord.ext import commands
from dotenv import load_dotenv

# This is just config stuff: Token, what server to write to, what channel to use for io
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
CHANNEL = "rating"


# Creating a obj for the memory and stuff
top_list = memory.Stats()

# This is for seeing all members on server, but it does not work
#intents = discord.Intents()
#intents.all()
#bot = commands.Bot(command_prefix='.',intents=intents)

# This is the handle to the discord api
client = discord.Client()


# Prints the points of each person.
async def ranking(m): 
    longest_name = max(map(len, top_list.get_list()))
    response = ("-" * (longest_name + 12)) + "\n"

    for counter, person in enumerate(top_list.get_list()):
        response += f"| \#{str(counter+1)} {top_list.get_stat(person)}"

    response += ("-" * (longest_name + 12))
    await m.channel.send(response)

# This will store different commands and stuff
commands = {
    "-": top_list.subtract,
    "+": top_list.add,
    "!ranking": ranking
} 


# If something happens on discord
@client.event
# If this something is a message
async def on_message(message):
    print(message.author.id)

    """
    if message.author.id == "170604046388953089":
        print("YES")
    """

    # This is just so the bot does not answer itself and become a loop
    if message.author == client.user:
        return

    if str(message.guild) == GUILD: # Remove "or 1" if running for real
        # Once methods are rewritten a bit the commands structure can be even more generic in such a way that:
        #
        # if message.content.split()[0] in commands:
        #     commands[message.content.split()[0]](message)
        #
        # The args can be made generic by letting the functions in commands use **kwargs and *args or wahtever

        # If !ranking is written, it will print all the points for each person. The other stuff is for formating
        if message.content.split()[0] == "!ranking":
            # Call the command (Which we know exists) with the correct args
            await commands[message.content.split()[0]](message)

        elif message.content.split()[0] == "!alias":
            print("alias")

        # This is when giving or taking rating-points from persons
        elif message.content != None and str(client.get_channel(message.channel.id)) == CHANNEL:
            new_message = message.content
            # When rating someone the call will be done from here
            if new_message[0] == "-" or new_message[0] == "+":
                name = "" # This is the string that will hold the name of the person being voted on
                self_rating = False # Flag for if person votes on themselves
                # if there is a gap between -/+ and name
                if new_message[1] == " ":
                    name = str(new_message.split()[1])
                    # Stopping people from voting for themselves
                    if top_list.alias_id(name) == str(message.author.id):
                        self_rating = True
                    else:
                        pos = top_list.get_pos(name)
                        commands[new_message[0]](name)
                        pos2 = top_list.get_pos(name)
                else:
                    name = str(new_message.split()[0][1:]) 
                    # Stopping people from voting for themselves
                    if top_list.alias_id(name) == str(message.author.id):
                        self_rating = True
                    else:
                        pos = top_list.get_pos(name)
                        commands[new_message[0]](name)
                        pos2 = top_list.get_pos(name)
                if self_rating:
                    response = "You are not allowed to vote on yourself"
                else:
                    if pos != pos2: 
                        response = f"{name} was moved {pos-pos2} steps to place #{top_list.get_pos(name)}"
                    else:
                        response = f"{name} is still on place #{top_list.get_pos(name)}"
            try:
                # This is the message that will be sent if the command was recognized
                await message.channel.send(response)
            except:
                # If not recognized message
                pass
    else:
        print(message.guild)

client.run(TOKEN)