from memory import Memory
import mysql.connector
import utils


class Name:
    def __init__(self, **kwargs):
        self.memory: Memory = kwargs["memory_handle"]

    async def name(self, message):
        # This is if there was 1 argument to the command
        if len(message.content.split()) == 2:
            new_name = utils.fix_str(message.content.split()[1])
            # TODO: implement propper error handling to catch specific faults
            try:
                self.memory.add_alias(message.author.id, new_name)
            except:
                pass

            result = self.memory.change_name(
                message.author.id, message.content.split()[1]
            )
            if result:
                response = "Name has been changed!"
            else:
                response = "Name could not be changed!"

            await message.channel.send(response)

        elif len(message.content.split()) > 2:
            # This is if more then 1 argument given
            response = "You can not have space in name!"
            await message.channel.send(response)
        else:
            # This is to display current name
            name = self.memory.id_to_name(message.author.id)
            response = f"Your current name is {name}"
            await message.channel.send(response)
