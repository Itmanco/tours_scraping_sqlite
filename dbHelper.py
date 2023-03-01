import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()


def query_all(table_name):
    # Query all data
    try:
        cursor.execute(f"select * from {table_name}")
        return cursor.fetchall()
    except sqlite3.OperationalError:
        return "no such table"


def event_in_table(row):
    band, city, date = row
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def create_table(table_name, columns):
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
    cursor.execute(script)
    connection.commit()



def query_with_condition(table_name, condition):
    # Query all data
    cursor.execute(f"select * from {table_name} WHERE {condition}")
    return cursor.fetchall()


def insert_sigle(table_name, row):

    script = f"INSERT INTO {table_name} VALUES ("
    first_Time = True
    for item in row:
        if first_Time:
            first_Time = False
            script = script + f"'{item}'"
        else:
            script = script + f",'{item}'"
    script = script+")"
    cursor.execute(script)
    connection.commit()
    return 0


def insert_many_rows(table_name, rows):
    cursor.executemany(f"INSERT INTO {table_name} VALUES (?,?,?)", rows)
    connection.commit()
    return 0