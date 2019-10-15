import os
import sqlite3
from sqlite3 import Error
 
def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None
    if os.path.isfile(r'C:\Users\AmitMeel\Desktop\Python_Flask\sqlitedb.db'):
        print('Database is already exist')
    else:
        try:
            conn = sqlite3.connect(r'C:\Users\AmitMeel\Desktop\Python_Flask\sqlitedb.db')
            print('pysqlite version:', sqlite3.version)
            print('sqlite version:',sqlite3.sqlite_version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

if __name__ == '__main__':
    create_connection()