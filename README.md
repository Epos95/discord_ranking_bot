# discord_ranking_bot
Simple bot made for ranking players with commands ish

## Commands
* !ranking
stats will print the toplist in order and display the points for the person
* \+ [name] ([reason])

will give a score to a person
* \- [name] ([reason])

will remove a score from a person

## Things that needs to be added manually:
* .env 

The .env file needs to be added manually with structure:
```
DISCORD_TOKEN=[Actual token]
GUILD=[Server name]
```
* stats.json

The stats.json needs to be added with a simple structure. First time you can run the function setup in memory, not sure if it will work tho :))
