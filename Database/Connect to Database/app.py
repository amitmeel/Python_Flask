from flask import Flask , jsonify, request, url_for, redirect, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True  #app will run in debug mode
app.config['SECRET_KEY']='thisisasecretkey'  #never store sensitive information in a session

def connect_db():
    conn = sqlite3.connect(r'C:\Users\user\Desktop\Python_Flask\sqlitedb.db')
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


@app.route('/')  # 'GET' request only
def index():
    session.pop('name',None)
    return '<h1>Hello, World!</h1>'

@app.route('/home', methods=['GET','POST'], defaults={'name':'Amit'})
@app.route('/home/<name>', methods=['GET', 'POST'])  # you can use the <string:name> for type casting
def home(name):
    session['name']=name
    return render_template('home.html', name=name, display=False, mylist=[1,2,3,4], \
                            listofdictionaries=[{'name':'amit'}, {'name':'sumit'}] )    # here name is template varibale

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {} , you are at {}<h1>'.format(name,location)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'namenotinsession'
    return jsonify({'key':'value', 'key2':[123,4345], 'name':name})

@app.route('/theform', methods=['GET','POST'])
def theform():
    if request.method=='GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        # location = request.form['location']

        # return '''Hello {}, you are from {}. you have submitted the form successfully'''.format(name,location)
        return redirect(url_for('home', name=name))

"""
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return '''Hello {}, you are from {}. you have submitted the form successfully'''.format(name,location)
"""

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    return jsonify({'result':'Success','Name':name, 'Location':location })


if __name__ == '__main__':
    app.run() 