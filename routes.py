from flask import Flask, render_template, url_for, request
from models import db, User
from forms import SignupForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:1988g@localhost:5432/postgres'
db.init_app(app)

app.secret_key = "super-secret-key"

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template("about.html")

@app.route('/signup', methods = ['GET','POST'])
def signup():
	form = SignupForm()
	if request.method =='POST':
		if not form.validate():
			return render_template('signup.html', form=form)
		else:
			newUser = User(form.first_name.data, form.last_name.data,form.email.data,form.password.data)
			db.session.add(newUser)
			db.session.commit()
			return 'Success!'
	elif request.method == 'GET':
		return render_template('signup.html',form=form)

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8081, debug=True)
