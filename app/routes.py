from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
	user = {'name':"Bubuda"}
	title = "The Bublog"
	posts = [
			{'author':{'name':"Bubuda"},
			'body':"Why did you never ask me out?"},
			{'author':{'name':"Bubudu"},
			'body':"Because you ate all my muruku"},
	]

	return render_template('index.html',title= title,user= user,posts= posts)
