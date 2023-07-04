"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
from builtins import *

# Параметры подключения к базе данных PostgreSQL
host = 'localhost'
port = '5432'
database = 'north'
user = 'postgres'
password = 'Matvey1234567890'

# Подключение к базе данных
connection = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
cursor = connection.cursor()


# Функция для заполнения таблицы данными из CSV-файла
def fill_table_from_csv(table_name, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовок
        for row in reader:
            query = f"INSERT INTO {table_name} VALUES ({', '.join('%s' for _ in row)})"
            cursor.execute(query, row)
            connection.commit()


# Заполнение таблицы employees данными из employees_data.csv
fill_table_from_csv('employees', 'employees_data.csv')

# Заполнение таблицы customers данными из customers_data.csv
fill_table_from_csv('customers', 'customers_data.csv')

# Заполнение таблицы orders данными из orders_data.csv
fill_table_from_csv('orders', 'orders_data.csv')

# Закрытие соединения с базой данных
cursor.close()
connection.close()
