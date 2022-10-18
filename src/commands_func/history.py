from memory import Memory


class History:
    def __init__(self, **kwargs) -> None:
        self.memory: Memory = kwargs["memory_handle"]

    def __get_votes_by(self, user_id):
        messages = self.memory.get_vote_from(user_id)

        returnList = [f"voting history for {self.memory.id_to_name(user_id)}:"]
        for message in messages:
            reason = ""
            if message[3]:
                reason = f'for "{message[3]}" '
            returnList.append(
                f" * {'Up' if message[4] > 0 else 'Down'} vote {reason}from {self.memory.id_to_name(message[2])} cast on {self.memory.id_to_name(message[1])}"
            )

        return returnList

    def __get_votes_on(self, user_id):
        messages = self.memory.get_vote_on(user_id)

        returnList = [f"voting history on {self.memory.id_to_name(user_id)}:"]
        for message in messages:
            reason = ""
            if message[3]:
                reason = f'for "{message[3]}" '
            returnList.append(
                f" * {'Up' if message[4] > 0 else 'Down'} vote {reason}on {self.memory.id_to_name(message[2])} cast by {self.memory.id_to_name(message[1])}"
            )

        return returnList

    async def cast_by_user(self, message):
        content = message.content.split(" ")

        n = None
        if len(content) > 2:
            # !votes_by epos95 7
            user = content[1]
            n = content[2]
        if len(content) > 1:
            # !votes_by epos95
            user = content[1]
        else:
            # Not enough args
            await message.channel.send("Not enough args!")
            pass

        user_id = self.memory.alias_to_id(user)
        if user_id == 0:
            await message.channel.send(f"Couldnt find username: {user}")
            return

        if n:
            votes = "\n".join(self.__get_votes_by(user_id)[: 1 + int(n)])
        else:
            votes = "\n".join(self.__get_votes_by(user_id))

        await message.channel.send(votes)

    async def cast_on_user(self, message):
        content = message.content.split(" ")

        n = None
        if len(content) > 2:
            # !votes_on epos95 7
            user = content[1]
            n = content[2]
        if len(content) > 1:
            # !votes_on epos95
            user = content[1]
        else:
            # Not enough args
            await message.channel.send("Not enough args!")
            pass

        user_id = self.memory.alias_to_id(user)
        if user_id == 0:
            await message.channel.send(f"Couldnt find username: {user}")
            return
        if n:
            votes = "\n".join(self.__get_votes_on(user_id)[: 1 + int(n)])
        else:
            votes = "\n".join(self.__get_votes_on(user_id))

        await message.channel.send(votes)
