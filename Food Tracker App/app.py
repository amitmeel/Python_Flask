from flask import Flask, render_template

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect(r'C:\Users\user\Desktop\Python_Flask\Food Tracker App\food_tracker.db')
    conn.row_factory = sqlite3.Row #in order to get the rows in a dict format instead of tuples
    return conn

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext #Flask to call that function when cleaning up after returning the response.
def close_connection(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/view')
def view():
    return render_template('day.html')

@app.route('/food')
def food():
    return render_template('add_food.html')

if __name__ == '__main__':
    app.run(debug=True)