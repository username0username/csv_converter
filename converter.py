import csv
import sqlite3
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_directory, 'csv.csv')
db_file_path = os.path.join(script_directory, 'csvdb.db')

conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

with open(csv_file_path, 'r', newline='', encoding='cp1251') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    headers = next(csv_reader)
    columns = ', '.join(headers)
    placeholders = ', '.join(['?' for _ in headers])
    create_table_query = f"CREATE TABLE IF NOT EXISTS table1 ({columns});"
    cursor.execute(create_table_query)

    insert_query = f"INSERT INTO table1 ({columns}) VALUES ({placeholders});"
    for row in csv_reader:
        cursor.execute(insert_query, row)

conn.commit()
conn.close()
