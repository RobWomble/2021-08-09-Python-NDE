from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to my api!"


@app.route('/menu')
def json_menu():
    menu = {"kung pao chicken": {"price": 12.99, "desc": "Yummy dark meat chicken with a kick"},
            "kung pao beef": {"price": 13.99, "desc": "Yummy beef with a kick"},
            "white rice": {"price": 2.99, "desc": "Fluffy white rice"},
            "fried rice": {"price": 4.99, "desc": "White rice with carrots, peas, and soy sauce fried "
                                                  "to perfection"},
            }
    return jsonify(menu)


if __name__ == "__main__":
    app.run()
