import mysql.connector
import json
from dotenv import load_dotenv
import os


load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("SQL_USER"),
    user=os.getenv("SQL_USER"),
    port=os.getenv("SQL_USER"),
    password=os.getenv("SQL_USER"),
    database="klinternet_bot",
)

mycursor = mydb.cursor()

with open("stats.json", "r") as fh:
    oldMemory = json.load(fh)

# Create all users
for id, name in oldMemory["names"].items():
    rating = oldMemory["top"][id]
    sent_messages = oldMemory["messageCount"][id]
    sqlQuery = f"INSERT INTO User (Id, Name, Message_count, Rating) VALUES ('{id}', '{name}', {sent_messages}, {rating})"
    print(sqlQuery)  # exec this
    mycursor.execute(sqlQuery)

# Create all alias
for alias, id in oldMemory["alias"].items():
    sqlQuery = f"INSERT INTO Alias (Name, user_id) VALUES ('{alias}', {id})"
    print(sqlQuery)  # exec this
    mycursor.execute(sqlQuery)

# Create all cites
for index, cite in oldMemory["citation"].items():
    sqlQuery = f"INSERT INTO Cite (Sent_from, Content) VALUES ({cite[0]}, '{cite[1]}')"
    print(sqlQuery)  # exec this
    try:
        mycursor.execute(sqlQuery)
    except:
        print("last query did not pass")

# create all votes
for vote in oldMemory["voting_history"]:
    sqlQuery = f"INSERT INTO Vote (Sent_from, Sent_to, Content, Points) VALUES ({vote['sender']}, {vote['reciever']}, '{vote['reason']}', {1 if vote['vote'] == 'Up' else -1})"
    print(sqlQuery)  # exec this
    mycursor.execute(sqlQuery)

mydb.commit()
mydb.close()


"""
CREATE TABLE `User` (
  `Id` Char(18),
  `Name` Char(150),
  `Message_count` Int,
  `Rating` Int,
  PRIMARY KEY (`Id`)
);

CREATE TABLE `Message` (
  `Id` Int NOT NULL AUTO_INCREMENT,
  `Content` Text,
  `Timestamp` datetime,
  `Sent_from` Char(18),
  PRIMARY KEY (`Id`),
  FOREIGN KEY (`Sent_from`) REFERENCES `User`(`Id`)
);

CREATE TABLE `Cite` (
  `Id` Int NOT NULL AUTO_INCREMENT,
  `Sent_from` Char(18),
  `Content` Text,
  `Timestamp` datetime,
  PRIMARY KEY (`Id`),
  FOREIGN KEY (`Sent_from`) REFERENCES `User`(`Id`)
);

CREATE TABLE `Vote` (
  `Id` Int NOT NULL AUTO_INCREMENT,
  `Sent_from` Char(18),
  `Sent_to` Char(18),
  `Content` Text,
  `Points` tinyint,
  PRIMARY KEY (`Id`),
  FOREIGN KEY (`Sent_to`) REFERENCES `User`(`Id`),
  FOREIGN KEY (`Sent_from`) REFERENCES `User`(`Id`)
);

CREATE TABLE `Alias` (
  `Name` Char(150),
  `User_id` Char(18),
  PRIMARY KEY (`Name`),
  FOREIGN KEY (`User_id`) REFERENCES `User`(`Id`)
);

"""
