from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	
	return "<h1>Hello World</h1>"
	

@app.route('/about')
def about():
	return"<h1>About page</h1>"

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)