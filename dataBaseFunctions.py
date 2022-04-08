import sqlite3

def get_id_users():
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_crypto_users = """SELECT * from usersIds"""
        cursor.execute(sqlite_crypto_users)
        print("Чтение строк")
        records = cursor.fetchall()
        print("Вывод каждой строки \n")
        # for row in records:
        #     print("ID:", row[0])
        #     print("API_KEY:", row[0])
        #     print("API_SECRET:", row[1])
        #     print("QUANTITY:", row[2])
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")\

def add_user_id(data):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_crypto_users = """INSERT INTO usersIds
                              (NAME)
                              VALUES (?);"""
        data_tuple = tuple(data)
        cursor.execute(sqlite_crypto_users, data_tuple)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу data_info")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        return 'Ошибка БД'
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            return 'Успешно'

def InsertFTXApi(FTX_API_KEY, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update usersIds set FTX_API_KEY = ? where NAME = ?"""
        data = (FTX_API_KEY, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertFTXSecretApi(FTX_SECRET_KEY, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update usersIds set FTX_SECRET_KEY = ? where NAME = ?"""
        data = (FTX_SECRET_KEY, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertBinanceApi(BINANCE_API_KEY, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update usersIds set BINANCE_API_KEY = ? where NAME = ?"""
        data = (BINANCE_API_KEY, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertBinanceSecretApi(BINANCE_SECRET_KEY, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update usersIds set BINANCE_SECRET_KEY = ? where NAME = ?"""
        data = (BINANCE_SECRET_KEY, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertFTXSUBSCHET(SUBSCHET, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update usersIds set SUBSCHET = ? where NAME = ?"""
        data = (SUBSCHET, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def getAllUserInfo(name):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from usersIds where NAME = ?"""
        data = (name)
        cursor.execute(sqlite_select_query, (data,))
        print("Чтение строк")
        records = cursor.fetchall()
        print("Вывод каждой строки \n")
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def add_user_id_current_position(data):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_crypto_users = """INSERT INTO currentPostion
                              (NAME)
                              VALUES (?);"""
        data_tuple = tuple(data)
        cursor.execute(sqlite_crypto_users, data_tuple)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу data_info")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        return 'Ошибка БД'
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            return 'Успешно'


def InsertFirstPositionSide(side, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update currentPostion set FIRST_POSITION_SIDE = ? where NAME = ?"""
        data = (side, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertFirstPositionPair(pair, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update currentPostion set FIRST_POSITION_PAIR = ? where NAME = ?"""
        data = (pair, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertFirstPositionSize(size, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update currentPostion set FIRST_POSITION_SIZE = ? where NAME = ?"""
        data = (size, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertSecondPositionSide(side, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update currentPostion set SECOND_POSITION_SIDE = ? where NAME = ?"""
        data = (side, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertSecondPositionPair(pair, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update currentPostion set SECOND_POSITION_PAIR = ? where NAME = ?"""
        data = (pair, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertSecondPositionSize(size, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update currentPostion set SECOND_POSITION_SIZE = ? where NAME = ?"""
        data = (size, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# def InsertSECONDPosition(side,pair,size, NAME):
#     try:
#         sqlite_connection = sqlite3.connect('data_info.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sql_update_query = """INSERT INTO currentPostion  (SECOND_POSITION_SIDE ,SECOND_POSITION_SIZE , SECOND_POSITION_PAIR)
#                                VALUES (?, ?, ?) where NAME = ?;"""
#         data = (side, size, pair, NAME)
#         cursor.execute(sql_update_query, data)
#         sqlite_connection.commit()
#         print("Запись успешно обновлена")
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")


def InsertFirstExchange(Exchange, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update currentPostion set FIRST_POSITION_EXCHANGE = ? where NAME = ?"""
        data = (Exchange, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def InsertSecondExchange(Exchange, NAME):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update currentPostion set SECOND_POSITION_EXCHANGE = ? where NAME = ?"""
        data = (Exchange, NAME)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def delete_positions(name):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """DELETE from currentPostion where NAME = ?"""
        cursor.execute(sql_update_query,(name,))
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def getAllPositionInfo(name):
    try:
        sqlite_connection = sqlite3.connect('data_info.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from currentPostion where NAME = ?"""
        data = (name)
        cursor.execute(sqlite_select_query, (data,))
        print("Чтение строк")
        records = cursor.fetchall()
        print("Вывод каждой строки \n")
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")