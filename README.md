# Discord ranking bot
Simple bot for discord. It can be used for ranking and citing.

## Commands:
```
!help                                 To print all commands
!cite                                 To get a random cited message, when replaying to a message it will save the message
!ranking                              This will print the stats of the rating given from other people
!stats                                This command will tell how many message each person has sent
+<name> (reason)                      Will give a person one point in the ranking system
-<name> (reason)                      Will lower the persons rating by 1
!name <new name>                      This will change the name displayed by the bot
!votes_on <name> <optional amount>    This will print ratings other people placed on mentioned person
!votes_by <name> <optional amount>    This will print rating a person placed on others
!mute <@name>                         Mutes the specified user
!unmute <@name>                       Unmutes the specified user
```

### Future features
* Handeling aliases (by beeing able to add and remove aliases)
* Allowing new persons to be added without needing to manually add them
* Sending schedule from timeEdit to discord? This would be fun
* Send encrypted messages from a dm to a channel. Everyone that is allowed can uncrypt the message to either the channel or in the dms.

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
