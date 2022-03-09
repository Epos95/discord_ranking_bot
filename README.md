# Discord ranking bot
Simple bot made for ranking players with commands ish

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
