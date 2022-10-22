# set shell := ["cmd.exe", "/c"] 

defualt:
    @just --list

# For the first time running the bot
setup:
    @sudo docker build -t discord-bot .
    @sudo docker run -p 3306:3306-d --name bot -it discord-bot 

# Run or restart the bot
restart:
    @sudo docker restart bot

# Turn off the bot
stop:
    @sudo docker stop bot
    @sudo docker cp bot:/discord_ranking_bot/stats.json .

# Full reinstallation of docker, OBS bot need to be running
reset:
    @sudo docker cp bot:/discord_ranking_bot/stats.json .
    @sudo docker stop bot
    @sudo docker rm bot 
    @sudo docker image rm discord-bot -f
    @sudo docker build -t discord-bot .
    @sudo docker run -d --name bot -it discord-bot

# Remove the container and image
remove:
    @sudo docker stop bot
    @sudo docker rm bot 
    @sudo docker image rm discord-bot -f
