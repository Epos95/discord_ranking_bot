# TODO

## First
* Alias from discord
* Connect list with people in the server, so people in the server is automatically in the list or atleast that people can be voted on from beeing in the server
* Alias_id should return discord nickname if there is no alias

### Bettingsystem for who will be the next one to downvote you
This idea will build up a coin system that will give money depending on what kind of bets you do. Different bets could be:
* Next person who will vote you up/down
* The closest person to write at a given time
* Coin tossing
* etc
Depending on the bet the person could be able to win money, with different amount depending on how hard of a bet it is. The coins will later be usable for buing different roles and stuff like that.

### Adding cite function
This could be done with just saving cite in the json and then printing random quotes every week or something. Or it could be done with the implementation said + the option to vote from 1-10 how good the quote is and then having a tier-list for the highest score. One way to implement it would be with reacting on the quote with a number 1-10 or something similar.


### Making the bot generical
The bot does not support adding new persons automatically, this should be a feature that is added. Optimal would be that people are added when someone votes on them. But there is some problem with how to know what the id of the person is etc. So this needs some thinking.

One idé would be that if a person is not registered the bot asks for a @ mention of the person or something in that direction.

### Propper error returns
The project should always have right type of errors. TypeErrors and other stuff should be raised. This is implemented sometimes, but not always.

### Case sensitiviness
Make the program not beeing case sensitive for commands. This would be a good thing.

### Unit tests
Start testing functions with unit tests. This for making sure the program is running without problems

## A little later
### Saving history
The bot does save all the history of rakning and soon cites as well. But this is all saved in ram as for now, this is because the whole json file is read in to a class. This should not be the case. The history should be saved in a file that will just be looped through when searching for something. This will let the program grow as well as the history without slowing down the computer running the script.

### Rewriting the memory structure
This is mentioned before in the "Structure of project" but the memory part needs to be written in a more modular way. This will be implemented together with the solution for the "saving history" as it is good to rewrite it when making stuff more efficient.

## Some more ideas
* (Adding birthday function?)
* (Adding urlzoom?)
* Counting messages sent on the server
* Welcome new people
* Make ping work


## Much later
* Music bot