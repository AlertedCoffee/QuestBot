import sqlite3 as sql


def create_table() -> None:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
       user_id INT PRIMARY KEY,
       user_name TEXT,
       quest_stations TEXT,
       question_opened bit,
       score INT);
       """)
    connection.commit()

    connection.close()


def drop_table():
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute("""drop TABLE IF EXISTS users
           """)
    connection.commit()
    connection.close()


def add_user(user_id: int, user_name: str) -> None:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"""insert into users
    values('{user_id}', '{user_name}', '', 0, 0)""")
    connection.commit()
    connection.close()


def get_user_list() -> []:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM users;")
    result = cursor.fetchall()
    connection.close()
    return result


def drop_user(user_id: int) -> None:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"delete from users"
                   f" where user_id = '{user_id}';")

    connection.commit()
    connection.close()


def get_quest_stations_string(user_id: int) -> str:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT quest_stations FROM users where user_id = '{user_id}';")
    string_result = cursor.fetchall()
    connection.close()

    try:
        return string_result[0][0]
    except:
        return ''


def get_quest_stations(user_id: int) -> []:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT quest_stations FROM users where user_id = '{user_id}';")
    string_result = cursor.fetchall()
    connection.close()

    try:
        return str(string_result[0][0]).split('&')
    except:
        return []


def save_quest_station(user_id: int, station: int) -> None:
    stations = get_quest_stations_string(user_id) + str(station) + '&'

    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"""Update users
                   set quest_stations = '{stations}'
                   where user_id = '{user_id}';""")

    connection.commit()
    connection.close()


def get_station_status(user_id: int) -> bool:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT question_opened FROM users where user_id = '{user_id}';")
    string_result = cursor.fetchall()
    result = string_result[0][0]

    connection.close()

    if result == 0:
        return False
    else:
        return True


def open_station(user_id: int) -> None:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"""Update users
                   set question_opened = 1
                   where user_id = '{user_id}';""")

    connection.commit()
    connection.close()


def close_station(user_id: int) -> None:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"Update users"
                   f" set question_opened = 0"
                   f" where user_id = '{user_id}';")

    connection.commit()
    connection.close()


def get_score(user_id: int) -> int:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT score FROM users where user_id = '{user_id}';")
    string_result = cursor.fetchall()
    result = string_result[0][0]

    connection.close()
    return result


def add_score(user_id: int) -> None:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    score = int(get_score(user_id)) + 1

    cursor.execute(f"Update users"
                   f" set score = {score}"
                   f" where user_id = '{user_id}';")

    connection.commit()
    connection.close()


def create_user(user_id: int, user_name: str, question_stations: str, score: int) -> None:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"""insert into users
            values('{user_id}', '{user_name}', '{question_stations}', {score})""")
    connection.commit()
    connection.close()


def user_exist(user_id: int) -> bool:
    connection = sql.connect('userbase.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM users where user_id = {user_id};")
    result = cursor.fetchall()
    connection.close()

    if len(result) != 0:
        return True
    else:
        return False
