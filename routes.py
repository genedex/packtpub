from flask import Flask, render_template, url_for, request, redirect, session
from models import db, User, Place
from forms import SignupForm, LoginForm, AddressForm
import geocoder
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:1988g@localhost:5432/postgres'
db.init_app(app)

app.secret_key = "super-secret-key"
bcrypt = Bcrypt(app)
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template("about.html")

@app.route('/signup', methods = ['GET','POST'])
def signup():
	if "email" in session:
		return redirect(url_for('home'))

	form = SignupForm()
	if request.method =='POST':
		if not form.validate():
			return render_template('signup.html', form=form)
		else:
			newUser = User(form.first_name.data, form.last_name.data,form.email.data,form.password.data)
			db.session.add(newUser)
			db.session.commit()
			session['email'] = newUser.email
			return  redirect(url_for('home'))
	elif request.method == 'GET':
		return render_template('signup.html',form=form)

@app.route("/login", methods=['POST','GET'])
def login():
	if "email" in session:
		return redirect(url_for('home'))

	form = LoginForm()
	if request.method == 'POST':
		if not form.validate():
			return render_template('login.html', form=form)
		else:
			email = form.email.data
			password = form.password.data

			user = User.query.filter_by(email=email).first()
			if user and user.check_password(password):
				session['email'] = form.email.data
				return redirect(url_for('home'))
			else:
				return redirect(url_for('login'))
	elif request.method == 'GET':
		return render_template('login.html',form=form)

@app.route('/logout')
def logout():
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route('/home', methods=['GET','POST'])
def home():
	if 'email' not in session:
		return redirect(url_for('login'))
	form = AddressForm()
	places = []
	my_coords = geocoder.google('Mountain View, CA').latlng
	if request.method == 'POST':
		if not form.validate():
			return render_template('home.html', form=form, my_coords=my_coords)
		else:
			address = form.address.data
			p = Place()
			my_coords = p.address_to_latlng(address)
			places = p.query(address)
			return render_template('home.html', form=form, my_coords=my_coords, places=places)
	elif request.method == 'GET':
		return render_template('home.html', form=form, my_coords=my_coords,places=places)

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8081, debug=True)
