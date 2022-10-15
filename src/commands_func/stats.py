from memory import Memory


class Stats:
    def __init__(self, **kwargs):
        self.memory: Memory = kwargs["memory_handle"]

    async def stats(self, message):

        # This will only print the stats
        if " " not in message.content:
            stat_order = self.memory.get_message_order()

            longest_name = max(map(len, [e[1] for e in stat_order]))
            response = ("-" * (longest_name + 12)) + "\n"
            response += f"| Messages sent:\n"
            response += ("-" * (longest_name + 12)) + "\n"

            for counter, person in enumerate([e[1] for e in stat_order]):
                #                  #pos            |person|  sent messages
                response += f"| \#{str(counter+1)} {person} {[x[2] for x in stat_order if x[1] == person][0]}\n"

            response += "-" * (longest_name + 12)
            await message.channel.send(response)

        # This will print the stats for a individual
        else:
            await message.channel.send("Sorry not implemented, try at next release")
