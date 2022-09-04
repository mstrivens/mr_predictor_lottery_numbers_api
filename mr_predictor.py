import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/feelinglucky', methods=["GET"])

def user_interface():
    return "<h1>NUMBERS:</h1>"

@app.route('/', methods=["GET"])

def home():
    return "HOME"

app.run()
