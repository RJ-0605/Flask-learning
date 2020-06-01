# real main.py page

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
#	return ("<h1>Hello World</h1>"+utc_time
	return render_template("index.html", utc_time=utc_time) 

@app.route('/about')
def about():
	utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	return render_template("about.html", utc_time=utc_time) 

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)