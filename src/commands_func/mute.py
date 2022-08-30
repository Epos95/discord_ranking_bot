#!/usr/bin/env python3

class Mute:
    def __init__(self, **kwargs):
        # no need for memory
        self.muted = []

    async def mute_user(self, message):
        print("wow")
        if self.__get_mentions(message):
            user = self.__get_mentions(message)
            self.muted.append(user.id)

            # Add a timeout for each mute, as a safe guard
            await message.channel.send(f"Successfully muted {user.name}!")

        else:
            await message.channel.send(f"Failed to mute...")

    async def unmute_user(self, message):
        if self.__get_mentions(message):
            user = self.__get_mentions(message)
            self.muted.remove(user.id)
            await message.channel.send(f"Successfully unmuted {user.name}!")

        else:
            await message.channel.send(f"Failed to mute...")

    def is_muted(self, user_id):
        return user_id in self.muted

    def __get_mentions(self, message):
        if len(message.mentions) > 0: # and not  "".join() in [user.name for user in message.mentions]:
            return message.mentions[0]
