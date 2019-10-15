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

def create_table(query, tablename):
    conn = sqlite3.connect(r'C:\Users\AmitMeel\Desktop\Python_Flask\sqlitedb.db')
    c = conn.cursor()

    table_name = (tablename,)
    #get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''', table_name)
    # if the count is 1, then table exists
    if c.fetchone()[0]==1 :
	    print('Table exists.')
    else:
        #create table
        c.execute(query)
        # commit changes
        conn.commit()
    c.close()

def print_rows(query):
    conn = sqlite3.connect(r'C:\Users\AmitMeel\Desktop\Python_Flask\sqlitedb.db')
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        print(row)

def execute_query(query):
    conn = sqlite3.connect(r'C:\Users\AmitMeel\Desktop\Python_Flask\sqlitedb.db')
    c = conn.cursor()
    #create table
    c.execute(query)
    # commit changes
    conn.commit()
    c.close()
 

if __name__ == '__main__':
    create_connection()
    create_table_query = ''' create table users(id integer primary key autoincrement,\
                                                name text, location text)'''
    create_table(create_table_query, 'users')
    
    insert_query = '''insert into users (name, location) values ('Amit', 'Bangalore')'''
    execute_query(insert_query)

    select_query = '''select * from users'''
    print_rows(select_query)


     
