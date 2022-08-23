class History:
    def __init__(self, **kwargs) -> None:
        self.memory = kwargs["memory_handle"]

    def __get_votes_by(self, username):
        id = self.memory.alias_id(username)
        json = self.memory.get_memory()["voting_history"]

        messages = []
        for thing in json:
            if thing["sender"] == username:
                messages.append(thing)

        s = [f"voting history for {self.memory.id_name(username)}:"]
        for message in messages:
            if message["reason"]:
                m = f"for \"{message['reason']}\" "
            else:
                m = f""
            s.append(
                f" * {message['vote']} vote {m}from {self.memory.id_name(message['sender'])} cast on {self.memory.id_name(message['reciever'])}"
            )

        return s

    def __get_votes_on(self, username):
        id = self.memory.alias_id(username)
        json = self.memory.get_memory()["voting_history"]

        messages = []
        for thing in json:
            if thing["reciever"] == username:
                messages.append(thing)

        s = [f"voting history on {self.memory.id_name(username)}:"]
        for message in messages:
            if message["reason"]:
                m = f"for \"{message['reason']}\" "
            else:
                m = f""
            s.append(
                f" * {message['vote']} vote {m}on {self.memory.id_name(message['reciever'])} cast by {self.memory.id_name(message['sender'])}"
            )

        return s

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

        user_alias = self.memory.alias_id(user)
        if user_alias == "Jane Doe":
            await message.channel.send(f"Couldnt find username: {user}")
            return

        if n:
            votes = "\n".join(self.__get_votes_by(user_alias)[: 1 + int(n)])
        else:
            votes = "\n".join(self.__get_votes_by(user_alias))

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

        user_alias = self.memory.alias_id(user)
        if user_alias == "Jane Doe":
            await message.channel.send(f"Couldnt find username: {user}")
            return
        if n:
            votes = "\n".join(self.__get_votes_on(user_alias)[: 1 + int(n)])
        else:
            votes = "\n".join(self.__get_votes_on(user_alias))

        await message.channel.send(votes)
