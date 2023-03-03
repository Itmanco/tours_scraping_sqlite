import sqlite3


class DbHelper:
    def __init__(self, database_path):
        # Establish a connection and a cursor
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()


    def query_all(self, table_name):
        # Query all data
        try:
            self.cursor.execute(f"select * from {table_name}")
            return self.cursor.fetchall()
        except sqlite3.OperationalError:
            return "no such table"


    def event_in_table(self, row):
        band, city, date = row
        self.cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            return True
        else:
            return False

    def create_table(self, table_name, columns):
        first_cicle = True
        script = f"CREATE TABLE '{table_name}' ("
        for item in columns:
            if first_cicle:
                script = script + f"'{item[0]}' TEXT"
                first_cicle = False
            elif item[1] == "str":
                script = script + f",'{item[0]}' TEXT"
            elif item[1] == "int":
                script = script + f",'{item[0]}' INTEGER"
        script = script+")"
        self.cursor.execute(script)
        self.connection.commit()



    def query_with_condition(self, table_name, condition):
        # Query all data
        self.cursor.execute(f"select * from {table_name} WHERE {condition}")
        return self.cursor.fetchall()


    def insert_sigle(self, table_name, row):

        script = f"INSERT INTO {table_name} VALUES ("
        first_Time = True
        for item in row:
            if first_Time:
                first_Time = False
                script = script + f"'{item}'"
            else:
                script = script + f",'{item}'"
        script = script+")"
        self.cursor.execute(script)
        self.connection.commit()
        return 0


    def insert_many_rows(self, table_name, rows):
        self.cursor.executemany(f"INSERT INTO {table_name} VALUES (?,?,?)", rows)
        self.connection.commit()
        return 0