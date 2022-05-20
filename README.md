# Discord ranking bot
Simple bot for discord. As for now it has a ranking feature. There will soon be a feature for citing messages and stuff like that

## Commands:
* !ranking-  stats will print the toplist in order and display the points for the person
* \+ [name] ([reason]) - will give a score to a person
* \- [name] ([reason]) - Will remove a score from a person
* !name [nickname] - Sets new nickname for the ranking


## Things that needs to be added manually:
* .env 

The .env file needs to be added manually with structure:
```
DISCORD_TOKEN=[Actual token]
GUILD=[Server name]
```
* stats.json

The stats.json needs to be added with a simple structure. Hehe ;) 

## Future structure of project:
The structure of the whole project needs to be updated. This means that there can not be a main that makes all the computing and stuff.
Plan:
**Main** This should just initialize stuff, and also read what command is used. Then it should call the apropriate function. This is also where there is a check so the bot writes in the right "guild" (server), but not stuff like what channel etc.

**Fucntions** This is a file that does not exsist. This should might even be a module, that has a fucnction for every type of command. 

**Memory** This file should *STRICTLY* save stuff to the json file. This includes all type of modifying as setters and stuff, but also getting information (getters)

**Utils** This is meant for smaller functions that will be used often. Example is when making stuff caseinsensitive, styling of text etc.


## Changes when making this a bigger bot
### Saving history
The bot does save all the history of rakning and soon cites as well. But this is all saved in ram as for now, this is because the whole json file is read in to a class. This should not be the case. The history should be saved in a file that will just be looped through when searching for something. This will let the program grow as well as the history without slowing down the computer running the script.

### Making the bot generical
The bot does not support adding new persons automatically, this should be a feature that is added.

### Propper error returns
The program does not give right error codes, this is not added at all. This should either be added by returning a certain value indicating what error it is, or by propper error handeling in python