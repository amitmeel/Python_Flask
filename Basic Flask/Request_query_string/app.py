# A query string is the portion of a URL where data is passed to a web application and/or back-end database.
# The reason we need query strings is that the HTTP protocol is stateless by design. 
# For a website to be anything more than a brochure, you need to maintain state (store data). 
# There are a number of ways to do this: On most web servers, you can use something like session state server-side.
# On the client, you can store via cookies. Or in the URL, you can store data via a query string.
# example: http://example.com/path/to/page?name=ferret&color=purple


from flask import Flask , jsonify, request

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

if __name__ == '__main__':
    app.run(debug=True) 