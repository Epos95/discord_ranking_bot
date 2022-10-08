FROM python:3.10


RUN git clone https://github.com/Leohemmingsson/discord_ranking_bot.git
WORKDIR /discord_ranking_bot/src/

RUN pip install -r ../requirements.txt

COPY .env ../

COPY stats.json ../

CMD git pull && python main.py