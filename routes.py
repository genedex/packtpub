from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template("about.html")

	
if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8081, debug=True)
