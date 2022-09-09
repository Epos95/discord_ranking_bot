# Discord ranking bot
Simple bot for discord. It can be used for ranking and citing.

## Commands:
```
!ranking - Stats will print the toplist in order and display the points for the person
+ [name] ([reason]) - Will give a score to a person
- [name] ([reason]) - Will remove a score from a person
!name [nickname] - Sets new nickname, and also adds it as a alias
!cite when replaying to a message will add the message as a citation
!cite alone will print a random message that was cited before
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
