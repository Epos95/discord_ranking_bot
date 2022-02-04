import memory

import os

import discord
from dotenv import load_dotenv

# This is just config stuff: Token, what server to write to, what channel to use for io
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "Klinternet"
CHANNEL = "rating"


# Creating a obj for the memory and stuff
top_list = memory.Stats()

commands = {"-": top_list.subtract, "+": top_list.add} # This will store different commands and stuff

# This is the handle to the discord api
client = discord.Client()



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

    # If !stats is written, it will print all the points for each person. The other stuff is for formating
    if message.content == "!ranking":
        response = "-----------------------\n"
        counter = 1
        for person in top_list.get_list():
            response += f"| \# {str(counter)} {top_list.get_stat(person)}"
            counter += 1
        response += "-----------------------"
        await message.channel.send(response)
    
    elif message.content.split()[0] == "!alias":
        print("alias")

    # This is when giving or taking rating-points from persons
    elif message.content != None and str(client.get_channel(message.channel.id)) == CHANNEL:
        new_message = message.content
        # When rating someone the call will be done from here
        if new_message[0] == "-" or new_message[0] == "+":
            # if there is a gap between -/+ and name
            name = ""
            if new_message[1] == " ":
                name = str(new_message.split()[1])
                pos = top_list.get_pos(name)
                commands[new_message[0]](name)
                pos2 = top_list.get_pos(name)
            else:
                name = str(new_message.split()[0][1:]) 
                pos = top_list.get_pos(name)
                commands[new_message[0]](name)
                pos2 = top_list.get_pos(name)
            if pos != pos2: 
                response = f"{name} was moved {pos-pos2} steps to place #{top_list.get_pos(name)}"
            else:
                response = f"{name} is still on place {top_list.get_pos(name)}"
        try:
            # This is the message that will be sent if the command was recognized
            await message.channel.send(response)
        except:
            # If not recognized message
            pass

client.run(TOKEN)