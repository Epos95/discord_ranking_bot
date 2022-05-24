import asyncio
import utils
class Ranking:
    def __init__(self, **kwargs):
        self.CHANNEL_RATING = kwargs["channel_rating"]
        self.memory = kwargs["memory_handle"]
        pass

    # This will print the current top list of the ranking
    # The fancy stuff is just formating to make it look good
    # Writtten by Epos95
    def top_list(self, message):
        longest_name = max(map(len, self.memory.get_list()))
        response = ("-" * (longest_name + 12)) + "\n"

        for counter, person in enumerate(self.memory.get_list()):
            response += f"| \#{str(counter+1)} {self.memory.get_stat(person)}"

        response += ("-" * (longest_name + 12))
        message.channel.send(response)
    
    # This will check to make sure the vote is "good enough"
    async def __is_good_vote(self, message):
        if str(message.channel) != self.CHANNEL_RATING:
            response = "Wrong channel for command"
            await self.__send_message(response, message)
            #await message.channel.send(response)
            return -1

        vote_info = utils.get_vote(message)

        # Can not vote on yourself
        if self.memory.alias_id(vote_info["name"]) == vote_info["author_id"]:
            response = "You are not allowed to vote on yourself"
            await message.channel.send(response)
            return -1
        
        # Can only vote on existing people
        if self.memory.alias_id(vote_info["name"]) == "Jane Doe":
            response = f"{vote_info['name']} is not registered as a person"
            await message.channel.send(response)
            return -1
        
        return 1 # If not returned by now it is a allowed vote

    async def __send_message(self, response, message):
            await message.channel.send(response)


    # This function is called when giving someone +
    async def add(self, message):
        # AHHHHH PROBLEM, need to run the check BEFORE it continues. BUT I need await for sending the message, not fun.
        # Solutions?
        # Make a function for sending the message, only that function will be async
        # Return the statement that needs to be sent OR the OK-go signal
        # Run the function, twice. Once for the yes or no. Once for sending the accurate message
        # OR gitgod :/
        if not await self.__is_good_vote(message):
            return -1
        

        vote_info = utils.get_vote(message)
        ranking_before_vote = self.memory.get_pos(vote_info["name"])
        # This is the "adding part"
        self.memory.add(vote_info["name"])
        # Saving stuff to memory
        self.memory.history(vote_info["author_id"], self.memory.alias_id(vote_info["name"]), vote_info["reason"], message.content[0])
        ranking_after_vore = self.memory.get_pos(vote_info["name"])

        # This just tells the stats after a vote
        if ranking_before_vote != ranking_after_vore:
            response = f"{vote_info['name']} was moved {ranking_before_vote-ranking_after_vore} steps to place #{self.memory.get_pos(vote_info['name'])}"
        else:
            response = f"{vote_info['name']} is still on place #{self.memory.get_pos(vote_info['name'])}"
        
        await message.channel.send(response)

    # This function is called when giving someone -
    def sub(self, message):
        if not self.__is_good_vote(message):
            return -1

        vote_info = utils.get_vote(message)
        ranking_before_vote = self.memory.get_pos(vote_info["name"])
        # This is the "subtracting part"
        self.memory.subtract(vote_info["name"])
        # Saving stuff to memory
        self.memory.history(vote_info["author_id"], self.memory.alias_id(vote_info["name"]), vote_info["reason"], message.content[0])
        ranking_after_vore = self.memory.get_pos(vote_info["name"])

        # This just tells the stats after a vote
        if ranking_before_vote != ranking_after_vore:
            response = f"{vote_info['name']} was moved {ranking_before_vote-ranking_after_vore} steps to place #{self.memory.get_pos['name']}"
        else:
            response = f"{vote_info['name']} is still on place #{self.memory.get_pos(vote_info['name'])}"
        
        message.channel.send(response)
