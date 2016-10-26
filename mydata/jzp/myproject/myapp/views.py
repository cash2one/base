from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your Browser is %s</p>' % user_agent


if __name__ == "__main__":
    app.debug = True
    app.run()
