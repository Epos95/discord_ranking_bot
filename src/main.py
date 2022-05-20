import os
import memory

import discord
import datetime
# Had this for the intent
#from discord.ext import commands
from dotenv import load_dotenv

# This is just config stuff: Token, what server to write to, what channel to use for io
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
CHANNEL_RATING = "rating"


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
    "!ranking": ranking,
    "!name": top_list.change_name,
    "history": top_list.history,
    "!cite": top_list.save_cite
} 


# If something happens on discord
@client.event
# If this something is a message
async def on_message(message):
    # Print author
    #print(message.author.id)

    """
    if message.author.id == "170604046388953089":
        print("YES")
    """

    # This is just so the bot does not answer itself and become a loop
    if message.author == client.user:
        return

    if str(message.guild) == GUILD:
        # Once methods are rewritten a bit the commands structure can be even more generic in such a way that:
        #
        # if message.content.split()[0] in commands:
        #     commands[message.content.split()[0]](message)
        #
        # The args can be made generic by letting the functions in commands use **kwargs and *args or wahtever

        # If !ranking is written, it will print all the points for each person. The other stuff is for formating

        # To see if its a reply of a previous message
        #print(message.reference)            

        if message.content.split()[0] == "!ranking":
            if str(message.channel) == CHANNEL_RATING:
                print("Running the ranking script")
                # Call the command (Which we know exists) with the correct args
                await commands[message.content.split()[0]](message)
            else:
                print("Command sent in wrong channel")
                # This might should tell the person where it is possible to say some commands?

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


        elif message.content.split()[0] == "!cite":
            # This will cite a sent message
            if message.reference == None:
               return 
            else:
                #print(message.reference)
                async for old_message in message.channel.history(limit=100):
                    if old_message.id == message.reference.message_id:
                        top_list.save_cite(old_message.author.id, old_message.content, old_message.id)

        # New giving or taking rating-points
        elif (message.content[0] == "+" or message.content[0] == "-") and str(message.channel) == CHANNEL_RATING:
            content = message.content
            name = ""
            reason = ""
            is_reason = False
            character_not_name = [' ', '+', '-']
            # This for-loop will take out name and reason in variables form content (message.content)
            for i in content:
                if i == '(' or is_reason:
                    if i != '(' and i != ')':
                        reason += i
                    is_reason = True
                elif i not in character_not_name:
                    name += i
            
            # Making sure it is not allowed to vote for oneself
            if top_list.alias_id(name) == str(message.author.id):
                response = "You are not allowed to vote on yourself"
            
            # This part could be switched out with iterating over all server members + alias
            elif top_list.alias_id(name) == "Jane Doe": 
                response = f"{name} is not registered as a person"

            # If everything works as it should
            else:
                print(f"sender {top_list.alias_id(name)} reciever {str(message.author.id)}")
                pos1 = top_list.get_pos(name)
                commands[message.content[0]](top_list.alias_id(name))
                commands["history"](sender=str(message.author.id), reciever=top_list.alias_id(name), reason=reason, vote=message.content[0])
                pos2 = top_list.get_pos(name)

                if pos1 != pos2: 
                    response = f"{name} was moved {pos1-pos2} steps to place #{top_list.get_pos(name)}"
                else:
                    response = f"{name} is still on place #{top_list.get_pos(name)}"


            await message.channel.send(response)
    else:
        print(f"Message sent in {message.guild}")

client.run(TOKEN)