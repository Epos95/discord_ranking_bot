#set shell := ["cmd.exe", "/c"] # Comment this if not using windows 

# This will fix the code (black python)
setup:
    sudo docker build -t discord-bot .
    sudo docker run -d --name bot -it discord-bot

# Run the bot
restart:
    sudo docker restart bot

stop:
    sudo docker stop bot

reset:
    sudo docker stop bot
    sudo docker rm bot 
    sudo docker image rm discord-bot -f
    sudo docker build -t discord-bot .
    sudo docker run -d --name bot -it discord-bot

remove:
    sudo docker stop bot
    sudo docker rm bot 
    sudo docker image rm discord-bot -f
