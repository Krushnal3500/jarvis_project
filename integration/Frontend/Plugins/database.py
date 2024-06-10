# Import module
import sqlite3
import os
from django.conf import settings


# Function to get SQLite connection
def get_connection():
    return sqlite3.connect(os.path.join(settings.BASE_DIR, 'Frontend\Data', 'chats.db'))
# # Connecting to sqlite

# conn = sqlite3.connect(os.path.join(settings.BASE_DIR, 'Frontend\Data', 'chats.db'))

# Creating a cursor object using the cursor() method
# cursor = conn.cursor()

def add_data(query):
    # table = "INSERT INTO ASSISTANT(QUERY, DATE_TIME) VALUES (?, datetime('now', 'localtime'))"
    # cursor.execute(table, (query,))
    # conn.commit()
    # return True
    conn = get_connection()
    cursor = conn.cursor()
    try:
        table = "INSERT INTO ASSISTANT(QUERY, DATE_TIME) VALUES (?, datetime('now', 'localtime'))"
        cursor.execute(table, (query,))
        conn.commit()
        return True
    finally:
        cursor.close()
        conn.close()


def get_data():
    # data = cursor.execute('SELECT * FROM ASSISTANT')
    # table_head = []
    # for column in data.description:
    #     table_head.append(column[0])
    # print("{:<14} {:<79} {:<20}".format(table_head[0], table_head[1], table_head[2]))
    # print()
    # for row in data:
    #     print("{:<14} {:<79} {:<20}".format(row[0], row[1], row[2]))
    # conn.commit()
    conn = get_connection()
    cursor = conn.cursor()
    try:
        data = cursor.execute('SELECT * FROM ASSISTANT')
        table_head = [column[0] for column in data.description]
        print("{:<14} {:<79} {:<20}".format(*table_head))
        print()
        for row in data:
            print("{:<14} {:<79} {:<20}".format(*row))
    finally:
        cursor.close()
        conn.close()