class Stats:
    def __init__(self, **kwargs):
        self.memory = kwargs["memory_handle"]

    async def stats(self, message):

        # This will only print the stats
        if ' ' not in message.content:
            longest_name = max(map(len, self.memory.get_message_list()))
            response = ("-" * (longest_name + 12)) + "\n"
            response += f'| Messages sent:\n'
            response += ("-" * (longest_name + 12)) + "\n"

            for counter, person in enumerate(self.memory.get_message_list()):
                if person == "":
                    response += f"| \#{str(counter+1)} {self.memory.get_message_count(person)}"

            response += "-" * (longest_name + 12)
            await message.channel.send(response)
        
        # This will print the stats for a individual
        else:
            await message.channel.send("Sorry not implemented, try at next release")

