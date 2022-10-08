FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN git clone https://github.com/Leohemmingsson/discord_ranking_bot.git
WORKDIR /discord_ranking_bot/src/

COPY .env ../

COPY stats.json ../

CMD git pull && python main.py