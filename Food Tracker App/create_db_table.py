import sqlite3
import os

def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None
    if os.path.isfile(r'C:\Users\user\Desktop\Python_Flask\Food Tracker App\food_tracker.db'):
        print('Database is already exist')
    else:
        try:
            conn = sqlite3.connect(r'C:\Users\user\Desktop\Python_Flask\Food Tracker App\food_tracker.db')
            print('pysqlite version:', sqlite3.version)
            print('sqlite version:',sqlite3.sqlite_version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

def create_table(query, tablename):
    """This method will create a table if it does not exists."""
    conn = sqlite3.connect(r'C:\Users\user\Desktop\Python_Flask\Food Tracker App\food_tracker.db')
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
    conn = sqlite3.connect(r'C:\Users\user\Desktop\Python_Flask\Food Tracker App\food_tracker.db')
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        print(row)

def execute_query(query):
    conn = sqlite3.connect(r'C:\Users\user\Desktop\Python_Flask\Food Tracker App\food_tracker.db')
    c = conn.cursor()
    #create table
    c.execute(query)
    # commit changes
    conn.commit()
    c.close()
 


if __name__ == '__main__':
    create_connection()

    log_date = """
                    create table log_date (
                        id integer primary key autoincrement,\
                        entry_date integer not null)
                """
    create_table(log_date, 'log_date')

    food = """
                create table food (
                    id integer primary key autoincrement,\
                    name text not null,\
                    protein integer not null,\
                    carbohydrate integer not null,\
                    fat integer not null,\
                    calories integer not null )
            """
    create_table(food, 'food')
    
    food_date = """
                    create table food_date (
                        food_id integer not null,\
                        log_date_id integer not null,\
                        primary key (food_id, log_date_id) )
                """
    create_table(food_date, 'food_date')