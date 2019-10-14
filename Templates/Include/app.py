from flask import Flask , jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)

app.config['DEBUG'] = True  #app will run in debug mode
app.config['SECRET_KEY']='thisisasecretkey'  #never store sensitive information in a session


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