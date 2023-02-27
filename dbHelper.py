import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()



# Query certain colummns
cursor.execute("SELECT band, date FROM events WHERE date='2023-10-24'")
rows = cursor.fetchall()
print(rows)

#Inser new rows
new_rows =[('Cats City', 'Savage cats rock', '2024-10-29'),
           ('Dogs City', 'Savage fighters methal', '2025-10-29')]

cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_rows)
connection.commit()


def query_all(table_name):
    # Query all data
    cursor.execute(f"select * from {table_name}")
    return cursor.fetchall()


def query_with_condition(table_name, condition):
    # Query all data
    cursor.execute(f"select * from {table_name} WHERE {condition}")
    return cursor.fetchall()


def insert_sigle(table_name, row):
    cursor.execute(f"INSERT INTO {table_name} VALUES (?,?,?)", row)
    connection.commit()
    return 0


def insert_many_rows(table_name, rows):
    cursor.executemany(f"INSERT INTO {table_name} VALUES (?,?,?)", rows)
    connection.commit()
    return 0