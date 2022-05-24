class Name:
    def __init__(self):
        pass

    
    async def name(self, message):
        try:
            if message.content.split()[1] != # author name:
                await self.__change_name(message)
            else:
                # Person tries to change name to their own name
                response = f"\"{message.content.split()[1]}\" is already your name"
                await message.channel.send(response)
        except:
            # This means there was no more than the command
            # That means that we should print the name of the author
            response = ("authorname")

    async def __change_name(self, message):
        pass

    async def __send_name(self, message):
        pass

    async def alias(self, message):
        pass