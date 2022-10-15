# imports from lib
from dotenv import load_dotenv
from unittest import result
import datetime
import mysql.connector
import os


class Memory:
    def __init__(self) -> None:
        load_dotenv()

        self.__SQL_USER = os.getenv("SQL_USER")
        self.__SQL_PASS = os.getenv("SQL_PASS")
        self.__SQL_PORT = os.getenv("SQL_PORT")
        self.__SQL_HOST = os.getenv("SQL_HOST")

    def __get_sql_handle(self):
        mydb = mysql.connector.connect(
            host=self.__SQL_HOST,
            user=self.__SQL_USER,
            port=self.__SQL_PORT,
            password=self.__SQL_PASS,
            database="test",
        )
        return mydb

    # General function to change a number of an existing row
    def __change_points(self, table, column, user_id, points=1):
        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        # To prevent sql-injection usage of %s
        sql = f"SELECT * FROM User WHERE Id=%s"
        values = (user_id,)
        mycursor.execute(sql, values)

        # If defined increment, else skip
        if mycursor.fetchone():
            sql = f"UPDATE {table} SET {column} = {column} + %s WHERE Id=%s"
            values = (
                points,
                user_id,
            )

            mycursor.execute(sql, values)
            mydb.commit()
            mydb.close()
            return 1
        mydb.close()
        return 0

    def sent_messages_points(self, user_id: str, points: int = 1):
        return self.__change_points(
            table="User", column="Message_count", user_id=user_id, points=points
        )

    def voting_points(self, user_id: str, points: int = 1):
        return self.__change_points(
            table="User", column="Rating", user_id=user_id, points=points
        )

    # General function to get the order of a table sorted by specified column
    def __get_order(self, table, column):
        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        sql = f"SELECT * FROM {table} ORDER BY {column} DESC"
        mycursor.execute(sql)
        return_list = mycursor.fetchall()
        mydb.close()
        return return_list

    def get_rating_order(self):
        return self.__get_order(table="User", column="Rating")

    def get_message_order(self):
        return self.__get_order(table="User", column="Message_count")

    def get_user_info(self, user_id: str):
        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        # To prevent sql-injection usage of %s
        sql = f"SELECT * FROM User WHERE Id=%s"
        values = (user_id,)
        mycursor.execute(sql, values)

        # If defined increment, else skip
        if user := mycursor.fetchone():
            mydb.close()
            return user

        mydb.close()
        return 0

    # General function to add a new instance of a specified table
    def __add_value(self, table: str, **kwargs):
        """
        Kwargs need to define table and have atleast one kwarg
        """
        # Too few arguments
        if len(kwargs) < 1 or table == None:
            return 0

        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        sql = f"INSERT INTO {table} ({', '.join(kwargs.keys())}) VALUES ({', '.join(['%s']*len(kwargs))})"

        mycursor.execute(sql, list(kwargs.values()))

        mydb.commit()
        mydb.close()
        return 1

    def add_vote(self, sender: str, reciver: str, reason: str, vote: int):
        param = {
            "Sent_from": sender,
            "Sent_to": reciver,
            "Content": reason,
            "Points": vote,
        }

        return self.__add_value(table="Vote", **param)

    def add_alias(self, user_id: str, new_alias: str):
        param = {
            "User_id": user_id,
            "Name": new_alias,
        }

        return self.__add_value(table="Alias", **param)

    def add_cite(self, user_id: str, cited_message: str, timestamp: datetime.datetime):
        param = {
            "Sent_from": user_id,
            "Content": cited_message,
            "Timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }

        return self.__add_value(table="Cite", **param)

    def add_user(self, user_id: str, name: str):
        param = {
            "Id": user_id,
            "Name": name,
            "Message_count": 0,
            "Rating": 0,
        }

        return self.__add_value(table="User", **param)

    def id_to_name(self, user_id):
        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        # To prevent sql-injection usage of %s
        sql = "SELECT * FROM User WHERE Id=%s"
        values = (user_id,)
        mycursor.execute(sql, values)

        # If defined increment, else skip
        if x := mycursor.fetchone():
            mydb.close()
            return x[1]

        mydb.close()
        return 0

    def alias_to_id(self, alias) -> str:
        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        # To prevent sql-injection usage of %s
        sql = "SELECT * FROM Alias WHERE Name=%s"
        values = (alias,)
        mycursor.execute(sql, values)

        # If defined increment, else skip
        if x := mycursor.fetchone():
            mydb.close()
            return x[1]

        mydb.close()
        return 0  # This means no found

    def change_name(self, user_id, new_name) -> int:
        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        # To prevent sql-injection usage of %s
        sql = "SELECT * FROM User WHERE Id=%s"
        values = (user_id,)
        mycursor.execute(sql, values)

        # If defined person found
        # FIXME: Does not work yet
        if mycursor.fetchone():
            sql = "SELECT * FROM Alias WHERE Name=%s AND User_id=%s"
            values = (
                new_name,
                user_id,
            )
            mycursor.execute(sql, values)

            if mycursor.fetchone():
                sql = f"UPDATE User SET Name = %s WHERE Id=%s"
                values = (
                    new_name,
                    user_id,
                )

                mycursor.execute(sql, values)
                mydb.commit()
                mydb.close()
                return 1
            else:
                # This means that the alias belongs to someone else or is not defined
                pass

        mydb.close()
        return 0

    def __get_random(self, table: str, n) -> list[tuple]:
        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        # To prevent sql-injection usage of %s
        sql = f"SELECT * FROM {table} ORDER BY RAND() LIMIT %s"
        values = (n,)
        mycursor.execute(sql, values)

        values = mycursor.fetchall()
        mydb.close()
        return values

    def get_ranom_cite(self, n=1) -> list[tuple]:
        return self.__get_random("Cite", n)

    def __get_vote_spec(self, sent_from=None, sent_to=None) -> list[tuple]:
        if not sent_from and not sent_to:
            return 0

        mydb = self.__get_sql_handle()
        mycursor = mydb.cursor()

        # To prevent sql-injection usage of %s
        if sent_from:
            sql = f"SELECT * FROM Vote WHERE Sent_from = %s"
            values = (sent_from,)
        elif sent_to:
            sql = f"SELECT * FROM Vote WHERE Sent_to= %s"
            values = (sent_to,)

        mycursor.execute(sql, values)

        values = mycursor.fetchall()

        mydb.close()
        return values

    def get_vote_from(self, id) -> list[tuple]:
        return self.__get_vote_spec(sent_from=id)

    def get_vote_on(self, id) -> list[tuple]:
        return self.__get_vote_spec(sent_to=id)


# If starting this file as main
if __name__ == "__main__":
    test = Memory()
    # test.setup()
    # print(test.alias_id("hej"))
    # test.history("From", "To", "Reasoning", "-")
    # test.voting_points("170604046388953089", 1)
    print(test.alias_to_id("d"))


# SQL e.errno
# e.errno  |  e.sqlstate  |        meaning

# 1062          23000       duplicate PK
# 1452          23000       FK contraint fail
