import utils
from memory import Memory


class Ranking:
    def __init__(self, **kwargs):
        self.CHANNEL_RATING = kwargs["channel_rating"]
        self.memory: Memory = kwargs["memory_handle"]

    # This will print the current top list of the ranking
    # The fancy stuff is just formating to make it look good
    # Writtten by Epos95
    async def ranking(self, message):
        rating_order = self.memory.get_rating_order()
        longest_name = max(map(len, [e[1] for e in rating_order]))
        response = ("-" * (longest_name + 12)) + "\n"
        response += f"| Voting:\n"
        response += ("-" * (longest_name + 12)) + "\n"

        for counter, person in enumerate([e[1] for e in rating_order]):
            #                #position         |person|     points
            response += f"| \#{str(counter+1)} {person} {[x[3] for x in rating_order if x[1] == person][0]}\n"

        response += "-" * (longest_name + 12)
        await message.channel.send(response)

    # This will check to make sure the vote is "good enough"
    async def __is_good_vote(self, message):
        if str(message.channel) != self.CHANNEL_RATING:
            # response = "Wrong channel for command"
            # await message.channel.send(response)
            return 0

        vote_info = utils.get_vote(message, self.memory)

        reciver_id = self.memory.alias_to_id(vote_info["name"])

        # Can not vote on yourself
        if reciver_id == vote_info["author_id"]:
            response = "You are not allowed to vote on yourself"
            await message.channel.send(response)
            return 0

        return 1  # If not returned by now it is a allowed vote

    # This will get the position of a user
    def __position(self, user_id):
        all_users = self.memory.get_rating_order()
        for index, user in enumerate(all_users):
            if user_id == user[0]:
                return index + 1

    # General function for the flow how to handle a vote
    async def __vote(self, message, points):
        # TODO: Set real error handling with tracing to the actual fault and accurate messages
        try:
            if not await self.__is_good_vote(message):
                # Will just return if conditions not met
                return -1

            vote_info = utils.get_vote(message, self.memory)
            reciver_id = self.memory.alias_to_id(vote_info["name"])
            ranking_before_vote = self.__position(reciver_id)

            # This is the "adding part"
            self.memory.voting_points(reciver_id, points)

            # Saving stuff to memory
            self.memory.add_vote(
                sender=vote_info["author_id"],
                reciver=reciver_id,
                reason=vote_info["reason"],
                vote=points,
            )
            ranking_after_vote = self.__position(reciver_id)

            # This just tells the stats after a vote
            if ranking_before_vote != ranking_after_vote:
                response = f"{vote_info['name']} was moved {ranking_before_vote-ranking_after_vote} steps to place #{ranking_after_vote}"
            else:
                response = (
                    f"{vote_info['name']} is still on place #{ranking_after_vote}"
                )

            await message.channel.send(response)
        except:
            await message.channel.send("Something went wrong, check the spelling")

    # This function is called when giving someone +
    async def add(self, message):
        return await self.__vote(message, 1)

    # This function is called when giving someone -
    async def sub(self, message):
        return await self.__vote(message, -1)
