class Help:
    def __init__(self, **kwargs) -> None:
        self.memory = kwargs["memory_handle"]

    def setAllCommands(self, commands):
        self.commands = commands

    async def run(self, message):
        if " " not in message.content:
            await self.printAll(message)

    async def printAll(self, message):
        # This is the discription that will be printed
        allCommands = {
            "!help": "To print all commands",
            "!cite": "To get a random cited message, when replaying to a message it will save the message you reply on",
            "!ranking": "This will print the stats of the rating given from other people",
            "!stats": "This command will tell how many message each person has sent",
            "+<name> (reason)": "Will give a person one point in the ranking system",
            "-<name> (reason)": "Will lower the persons rating by 1",
            "!name <new name>": "This will change the name displayed by the bot",
            "!votes_on <name> <optional amount>": "This will print ratings other people placed on mentioned person",
            "!votes_by <name> <optional amount>": "This will print rating a person placed on others",
        }

        response = "```"
        longestCommand = 0
        for command in allCommands.keys():
            if len(command) > longestCommand:
                longestCommand = len(command)

        # This is padding
        longestCommand += 3

        for command, description in allCommands.items():
            # Adding command padding (to allign) and description
            response += f"{command + (' '* (int(longestCommand) - len(command)))} {description}\n"
        response += "```\n"

        print(response)

        await message.channel.send(response)
