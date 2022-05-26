# Discord ranking bot
Simple bot for discord. As for now it has a ranking feature. There will soon be a feature for citing messages and stuff like that

## Commands:
```
!ranking - Stats will print the toplist in order and display the points for the person
+ [name] ([reason]) - Will give a score to a person
- [name] ([reason]) - Will remove a score from a person
!name [nickname] - Sets new nickname, and also adds it as a alias
```

### Future features
* Handeling aliases (by beeing able to add and remove aliases)
* Allowing new persons to be added without needing to manually add them
* Counting sent messages on the server, to know who is sending most messages. Something similar to the ranking system that is in place now.
* Sending schedule from timeEdit to discord? This would be fun

## Things that needs to be added manually:
* .env 

The .env file needs to be added manually with structure:
```
DISCORD_TOKEN=[Actual token]
GUILD=[Server name]
```
* stats.json

## Usage of project:
This project has a just file. You can read more about that [here](https://github.com/casey/just). The project is kept pretty by [black python](https://github.com/psf/black) which also is included in the just file.

## Structure of project
The project is structured in OOP with a heavily usage of packages/modules. Where every command is a separate part of the command package. This is just to make it easy to navigate between different commands and also to be able to change things without making everything dependent on each other. 

This type of module based code is something that will be imnplemented for the memory part as well soon. 

The main file is used for checking that messages are sent in the right channel and also acts as a "switch" for what command is used etc.

## Changes that needs to be done
### Saving history
The bot does save all the history of rakning and soon cites as well. But this is all saved in ram as for now, this is because the whole json file is read in to a class. This should not be the case. The history should be saved in a file that will just be looped through when searching for something. This will let the program grow as well as the history without slowing down the computer running the script.

### Rewriting the memory structure
This is mentioned before in the "Structure of project" but the memory part needs to be written in a more modular way. This will be implemented together with the solution for the "saving history" as it is good to rewrite it when making stuff more efficient.

### Making the bot generical
The bot does not support adding new persons automatically, this should be a feature that is added. Optimal would be that people are added when someone votes on them. But there is some problem with how to know what the id of the person is etc. So this needs some thinking.

One idé would be that if a person is not registered the bot asks for a @ mention of the person or something in that direction.

### Propper error returns
The program does not give right error codes, this is not added at all. This should either be added by returning a certain value indicating what error it is, or by propper error handeling in python. And also thinking about if problems should be sent in the test channel or not? Maybe have it send in DMs otherwise.

### Case sensitiviness
Make the program not beeing case sensitive for commands. This would be a good thing.