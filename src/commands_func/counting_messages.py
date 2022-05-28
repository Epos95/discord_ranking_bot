# This class needs to be renamed after what the command should be
# The filename should also be changed
# Name suggestion is "stats"

class Counting_messages:
    def __init__(self):
        pass

    def add(self, message):
        author_id = message.author.id

        # Call memory function to add 1 on author_id

        # This should just add +1 for a person per message. But it should also check if the person is just spamming
        # This will be done by running the __is_spam function.
        pass

    def __is_spam(self):
        # This function should check if a person is spamming just to get points.
        # It should check if messages sent is just the same sent after each other.
        # It should check how fast the person is sending the messages. A limit like 10/second or somrthing like that.
        # It should also check what types of messages that is sent. It should filter out messages that is just
        # different characters in each message and stuff like that.
        pass

    def ranking(self, message):
        if len(message.content.split()) == 1:
            self.top_ranking(message)
        else:
            if message.content.split()[1] == "own":
                self.own_ranking(message)
            
        # This is the general function that is called when a person calls for the ranking command
        pass

    def own_ranking(self, message):
        # This will print out the messages a person is sending. Maybe also some fun fact as how long
        # the average message is or something like that
        pass

    def top_ranking(self, message):
        # This will print out how many messages that has been sent person by person. This is a top score thing
        pass