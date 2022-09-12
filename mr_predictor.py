import flask
import number_generator

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/feelinglucky', methods=["GET"])

def user_interface():
    return number_generator.generate()

@app.route('/', methods=["GET"])

def home():
    return "HOME"

app.run()
