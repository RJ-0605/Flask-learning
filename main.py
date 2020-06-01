#  main.py page

from flask import Flask, render_template,url_for
from forms import RegistrationForm,LoginForm

app = Flask(__name__)

# secret key below to help prevent syber and crossplatform attacks

app.config['SECRET_KEY'] = '67fe0e4d2a60c56aac5b2362b1ded716'



posts = [
	{'author':'Corey Schafer',
	 'title':'Blog post 1',
	 'content':'First post content',
	 'date_posted':'April 20,2018'

	 },
	 {
	 'author':'Jane Doe',
	 'title':'Blog post 2',
	 'content':'Second post content',
	 'date_posted':'April 21,2018'

	 }



]


@app.route('/')
def hello():

#	return ("<h1>Hello World</h1>
	return render_template("index.html", post_variable=posts) 

@app.route('/about')
def about():
	
	return render_template("about.html",title="About")



@app.route('/register')
def register():
	form=RegistrationForm()
	return render_template('register.html',title='Register', form=form)


@app.route('/login')
def login():
	form=LoginForm()
	return render_template('register.html',title='Login', form=form)

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)