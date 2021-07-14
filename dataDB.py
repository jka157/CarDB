import sqlite3

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY, name TEXT, hp INTEGER, tq INTEGER, price INTEGER);"
INSERT_CAR = "INSERT INTO cars (name, hp, tq, price) VALUES (?, ?, ?, ?);"
GET_ALL_CARS = "SELECT * FROM cars;"
GET_CARS_BY_NAME = "SELECT * FROM cars WHERE name = ?;"
GET_MOST_EXPENSIVE_CAR = "SELECT * FROM cars ORDER BY price LIMIT 1;"
DELETE_CAR = "DELETE FROM cars WHERE name = ?;"

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE)

def add_car(connection, name, hp, tq, price):
    with connection:
        connection.execute(INSERT_CAR, (name, hp, tq, price))

def get_all_cars(connection):
    with connection:
        return connection.execute(GET_ALL_CARS).fetchall()

def get_cars_by_name(connection, name):
    with connection:
        return connection.execute(GET_CARS_BY_NAME, (name,)).fetchall()

def get_most_expensive_car(connection, name):
    with connection:
        return connection.execute(GET_MOST_EXPENSIVE_CAR, (name,)).fetchone()

def delete_car(connection, name):
    with connection:
        connection.execute(DELETE_CAR, (name, ))




