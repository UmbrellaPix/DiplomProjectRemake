import sqlite3

class sql:
    def __init__(self):
        self._conn_db = sqlite3.connect(r'database.db', check_same_thread=False)
        self._cur_db = self._conn_db.cursor()
        self._db_init()

    # Инициализация таблиц базы данных
    def _db_init(self):
        # Таблица логинов
        self._cur_db.execute(f"""CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        login TEXT,
        password_id INTEGER,
        permission INTEGER,
        first_name TEXT,
        last_name TEXT,
        patronymic TEXT,
        department TEXT,
        post TEXT,
        is_delete INTEGER
        )""")
        self._conn_db.commit()

        # Таблица сессии
        self._cur_db.execute(f"""CREATE TABLE IF NOT EXISTS sessions(
        id INTEGER,
        session_uuid TEXT,
        login_id INTEGER,
        time_deactivation INTEGER,
        is_delete INTEGER
        )""")
        self._conn_db.commit()

        # Таблица паролей
        self._cur_db.execute(f"""CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER,
        password TEXT,
        is_delete INTEGER
        )""")
        self._conn_db.commit()

        # Таблица файлов
        self._cur_db.execute(f"""CREATE TABLE IF NOT EXISTS files(
        id INTEGER,
        name TEXT,
        file BLOB,
        is_delete INTEGER
        )""")
        self._conn_db.commit()

        # Таблица задач
        self._cur_db.execute(f"""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER,
        name TEXT,
        executor INTEGER,
        deadline  TEXT,
        description TEXT,
        files TEXT,
        author_id INTEGER,
        status INTEGER,
        is_delete INTEGER
        )""")
        self._conn_db.commit()

    def _input_handler_create(self, values = {}):
        columns_name = ""
        values_list = []
        count_rows_sql = ""

        for column_name, value in values.items():
            columns_name += "'" + column_name + "', "
            count_rows_sql += "?, "
            values_list.append(value)

        columns_name = columns_name.strip(", ")
        count_rows_sql = count_rows_sql.strip(", ")

        return columns_name, count_rows_sql, values_list
    

    def _input_handler_update(self, values):
        columns_and_values = ""

        for column_name, value in values.items():
            columns_and_values += "'" + column_name + f"' = '{value}', "

        columns_and_values = columns_and_values.strip(", ")

        return  columns_and_values


    def create(self, table, values):
        columns_name, count_rows_sql, values_arr = self._input_handler_create(values)
        self._cur_db.execute(f"INSERT INTO {table} ({columns_name}) VALUES({count_rows_sql})", values_arr)
        self._conn_db.commit()


    def delete(self, table, id):
        self._cur_db.execute(f"UPDATE {table} SET is_delete = 1 WHERE id = '{id}'")
        self._conn_db.commit()


    def update(self, table, id, values):
        self._cur_db.execute(f"UPDATE {table} SET is_delete = 1 WHERE id = '{id}'")
        self._conn_db.commit()

    def search():
        pass

    def all():
        pass

sql_ = sql()
request_table = {
    "id":0, 
    "password":"1234"
    }
sql_.create("passwords", request_table)


