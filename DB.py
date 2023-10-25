import sqlite3 as sql
import os


def start_db():
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
       user_id INT PRIMARY KEY,
       user_name TEXT,
       quest_stations TEXT,
       score INT);
       """)
    connection.commit()

    connection.commit()
    connection.close()


def add_user(user_id: int, user_name: str):
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"""insert into users
    values('{user_id}', '{user_name}', '', 0)""")
    connection.commit()
    connection.close()


def get_quest_stations(user_id: int):
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT quest_stations FROM users where user_id = '{user_id}';")
    string_result = cursor.fetchall()

    try:
        result = string_result[0][0]
    except:
        result = ''
    connection.close()
    return result


def save_quest_station(user_id: int, station: int):
    stations = get_quest_stations(user_id) + '&' + str(station)

    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"Update users"
                   f" set quest_stations = '{stations}'"
                   f" where user_id = '{user_id}';")

    connection.commit()
    connection.close()


def get_score(user_id: int):
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT score FROM users where user_id = '{user_id}';")
    string_result = cursor.fetchall()
    result = string_result[0][0]

    connection.close()
    return result


def add_score(user_id: int):
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    score = int(get_score(user_id)) + 1

    cursor.execute(f"Update users"
                   f" set score = {score}"
                   f" where user_id = '{user_id}';")

    connection.commit()
    connection.close()


def get_user_list():
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM users;")
    result = cursor.fetchall()
    connection.close()
    return result


def drop_user(user_id: int):
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"delete from users"
                   f" where user_id = '{user_id}';")

    connection.commit()
    connection.close()


def create_user(user_id: int, user_name: str, question_stations: str, score: int):
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"""insert into users
            values('{user_id}', '{user_name}', '{question_stations}', {score})""")
    connection.commit()
    connection.close()


def user_exist(user_id: int):
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM users where user_id = {user_id};")
    result = cursor.fetchall()
    connection.close()

    if len(result) != 0:
        return True
    else:
        return False
