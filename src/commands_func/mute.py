#!/usr/bin/env python3

import asyncio
from random import choice


class Mute:
    def __init__(self, **kwargs):
        # no need for memory
        self.muted = []
        self.admins = ["Epos95", "CurryAndMilk"]
        self.GOD_MODE = True  # Kill switch for if it gets annoying

    async def __timeout(self, message, muted_user, timeout=10):
        if self.GOD_MODE and muted_user.name in self.admins:
            snarky_messages = [
                "Oh yea please try again",
                "you thought!",
                "...",
                "Going good?",
                "Error!",
                "woops, looks like you tried to mute a admin, would you like some help with that?",
                "OwO I did a fucky wucky uwu",
            ]

            await message.channel.send(choice(snarky_messages))
            return

        await asyncio.sleep(timeout)

        if self.is_muted(muted_user.id):
            self.muted.remove(muted_user.id)
            await message.channel.send(f"Unmuted user {muted_user.name}!")

    async def mute_user(self, message):
        if self.__get_mentions(message):
            user = self.__get_mentions(message)
            self.muted.append(user.id)

            await message.channel.send(
                f"Successfully muted {user.name} for {self.timeout} seconds!"
            )

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
        if (
            len(message.mentions) > 0
        ):  # and not  "".join() in [user.name for user in message.mentions]:
            return message.mentions[0]
