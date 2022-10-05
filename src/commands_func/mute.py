#!/usr/bin/env python3

import asyncio

class Mute:
    def __init__(self, **kwargs):
        # no need for memory
        self.muted = []

		# Default to 10 second timeout
        if kwargs["timeout"]:
            self.timeout = kwargs["timeout"]
        else:
            self.timeout = 10

    async def __timeout(self, message, muted_user):
        await asyncio.sleep(self.timeout)

        if self.is_muted(muted_user.id):
            self.muted.remove(muted_user.id)
            await message.channel.send(f"Unmuted user {muted_user.name}!")

    async def mute_user(self, message):
        if self.__get_mentions(message):
            user = self.__get_mentions(message)
            self.muted.append(user.id)

            await message.channel.send(f"Successfully muted {user.name} for {self.timeout} seconds!")

            # Add a timeout for each mute, as a safe guard
            await asyncio.create_task(self.__timeout(message, user))

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
