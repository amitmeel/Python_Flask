from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')  # 'GET' request only
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/home')  # GET request only
def home():
    return '<h1>You are on the home</h1>'

@app.route('/json') # Git request only
def json():
    return jsonify({'key':'value', 'key2':[123,4345]})

if __name__ == '__main__':
    app.run(debug=True)  # when developing if you dont want to start your app again and again \
                         # set debug=True