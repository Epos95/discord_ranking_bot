class Ranking:
    def __init__(self, **kwargs):
        self.CHANNEL_RATING = kwargs["channel_rating"]
        self.message = kwargs["message_handle"]
        self.memory = kwargs["memory_handle"]
        pass

    # This will print the current top list of the ranking
    # The fancy stuff is just formating to make it look good
    # Writtten by Epos
    def top_list(self):
        longest_name = max(map(len, self.memory.get_list()))
        response = ("-" * (longest_name + 12)) + "\n"

        for counter, person in enumerate(self.memory.get_list()):
            response += f"| \#{str(counter+1)} {self.memory.get_stat(person)}"

        response += ("-" * (longest_name + 12))
        self.message.channel.send(response)

    def add(self, *args):
        # args= [message]
        pass


