from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def root_page():
	return "this is the root page!"

@app.route('/hello/')
def hello():
	return "Hello World!"
@app.route('/porg',methods=['GET','POST'])
def porg():
	if request.method == 'POST':
		return "post"
	else:
		return 'not post'
@app.route('/index/')
def index():
	title = "flask templates"
	body = "this is just a flask template test!"
	return render_template('index.html',title=title,body=body)

if __name__ == "__main__":
	app.debug = True
	app.run()

