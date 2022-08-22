class Citation:
    def __init__(self, **kwargs):
        self.memory = kwargs["memory_handle"]
        pass

    # This is the function that will be called when typing "!cite"
    async def cite(self, message):
        if message.reference == None:
            await self.send_cite(message)
            return 1

        search_limit = 100
        try:
            if int(message.content.split()[1]) > search_limit:
                search_limit = int(message.content.split()[1])
        except:
            pass

        if search_limit > 1000000:
            response = "To high search limit, max limit is 1000000"
            await message.channel.send(response)
            return -1

        async for old_message in message.channel.history(limit=search_limit):
            response = ""
            if old_message.id == message.reference.message_id:
                # Error handling for empty messages or images
                if old_message.content == "":
                    response = "Message is empty or a image. Images can not be cited right now"
                    await message.channel.send(response)
                    return -1

                return_value = self.memory.save_cite(
                    old_message.author.id, old_message.content, old_message.id
                )
                if return_value == 1:
                    response = "Message was cited"
                    break
                elif return_value == -1:
                    response = "There was some problem with citing that message"
                    break

        if response == "":
            response = (
                'Message could not be found, try higher search limit ex) "!cite 10000"'
            )
        await message.channel.send(response)


    # This function will send a random cited message
    async def send_cite(self, message):
        cited_message = self.memory.get_cite()
        response = f'"{cited_message[1]}" ~ {cited_message[0]}'
        await message.channel.send(response)
