class History:
	def __init__(self, **kwargs) -> None:
		self.memory = kwargs["memory_handle"]

	def __get_votes_by(self, username):
		json = self.memory.__memory
		
		messages = []
		for message in json: 
			if message["sender"] in username:
				messages.append(message)

		s = f"voting history for {username}:\n"
		for message in messages:
			s += f" * \"{message['reason']}\" on {message['reciever']}"
		
		return messages

	def __get_votes_on(self, username):
		json = self.memory.__memory
		
		messages = []
		for message in json: 
			if message["reciever"] in username:
				messages.append(message)

		s = f"voting history for {username}:\n"
		for message in messages:
			s += f" * \"{message['reason']}\" from {message['sender']}"
		
		return messages

	async def cast_by_user(self, message):
		message = message.split(" ")

		n = None
		if len(message) > 2:
			# !votes_by epos95 7
			user = message[1]
			n = message[2]
		if len(message) > 1:
			# !votes_on epos95 
			user = message[1]
		else:
			# Not enough args
			await message.channel.send("Not enough args!")
			pass

		user_alias = self.memory.alias_id(user)
		if user_alias == "Jane Doe":
			await message.channel.send(f"Couldnt find username: {user}")
			return 

		if n:
			votes = self.__get_votes_on(user_alias)[:n]
		else:
			votes = self.__get_votes_on(user_alias)

		await message.channel.send(votes)

	async def cast_on_user(self, message):
		message = message.split(" ")

		n = None
		if len(message) > 2:
			# !votes_by epos95 7
			user = message[1]
			n = message[2]
		if len(message) > 1:
			# !votes_on epos95 
			user = message[1]
		else:
			# Not enough args
			await message.channel.send("Not enough args!")
			pass

		user_alias = self.memory.alias_id(user)
		if user_alias == "Jane Doe":
			await message.channel.send(f"Couldnt find username: {user}")
			return 

		if n:
			votes = self.__get_votes_by(user_alias)[:n]
		else:
			votes = self.__get_votes_by(user_alias)