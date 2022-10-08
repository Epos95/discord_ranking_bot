# set shell := ["cmd.exe", "/c"] 

# This will fix the code (black python)
setup:
    sudo docker build -t discord-bot .
    sudo docker run -d --name bot -it discord-bot

# Run the bot
restart:
    sudo docker restart bot

stop:
    sudo docker stop bot
    sudo docker cp bot:/discord_ranking_bot/stats.json .

reset:
    sudo docker cp bot:/discord_ranking_bot/stats.json .
    sudo docker stop bot
    sudo docker rm bot 
    sudo docker image rm discord-bot -f
    sudo docker build -t discord-bot .
    sudo docker run -d --name bot -it discord-bot

remove:
    sudo docker stop bot
    sudo docker rm bot 
    sudo docker image rm discord-bot -f
