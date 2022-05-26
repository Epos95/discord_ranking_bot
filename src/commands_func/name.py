# Chould think about splittling this function up?
# At least if making it any bigger. It can not be any larger now.
# If splitting the code, make sure to have one function for each thing
class Name:
    def __init__(self, **kwargs):
        self.memory = kwargs["memory_handle"]

    async def name(self, message):
        # This is if there was 1 argument to the command
        if len(message.content.split()) == 2:
            result = self.memory.change_name(
                message.author.id, message.content.split()[1]
            )
            if result == 1:
                response = "Name has been changed!"
            elif result == 0:
                response = "Could not change to the new name"
            else:
                response = "Something else went wrong"

            await message.channel.send(response)
        elif len(message.content.split()) > 2:
            # This is if more then 1 argument given
            response = "You can not have space in name!"
            await message.channel.send(response)
        else:
            # This is to display current name
            name = self.memory.id_name(message.author.id)
            response = f"Your current name is {name}"
            await message.channel.send(response)
