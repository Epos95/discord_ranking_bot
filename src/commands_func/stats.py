class Stats:
    def __init__(self, **kwargs):
        self.memory = kwargs["memory_handle"]

    async def stats(self, message):

        exit()
        if ' ' not in message.content:
            longest_name = max(map(len, self.memory.get_list()))
            response = ("-" * (longest_name + 12)) + "\n"

            for counter, person in enumerate(self.memory.get_list()):
                response += f"| \#{str(counter+1)} {self.memory.get_stat(person)}"

            response += "-" * (longest_name + 12)
            await message.channel.send(response)
            print("stats")
        else:
            print("specific stats")

