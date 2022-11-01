import flask
import number_generator

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET"])

def user_interface():
    return number_generator.return_best_numbers()

app.run()
