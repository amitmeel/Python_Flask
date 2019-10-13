from flask import Flask , jsonify, request, url_for, redirect

app = Flask(__name__)

@app.route('/')  # 'GET' request only
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/home', methods=['GET','POST'], defaults={'name':'Amit'})
@app.route('/home/<name>', methods=['GET', 'POST'])  # you can use the <string:name> for type casting
def home(name):
    return '<h1>Hello {} You are on the home</h1>'.format(name)

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {} , you are at {}<h1>'.format(name,location)

@app.route('/json')
def json():
    return jsonify({'key':'value', 'key2':[123,4345]})

@app.route('/theform', methods=['GET','POST'])
def theform():
    if request.method=='GET':
        return '''<form method="POST" action="/theform">
              <input type="text" name="name">
              <input type="text" name="location">
              <input type="submit">
              </form>'''
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
    app.run(debug=True) 