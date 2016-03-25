from flask import Flask, render_template, url_for
from models import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/packtpub'
db.init_app(app)
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template("about.html")


if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8081, debug=True)
