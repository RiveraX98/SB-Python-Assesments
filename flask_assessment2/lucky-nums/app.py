from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=["POST"])
def get_facts():
    colors = ["red", "green", "orange", "blue", "yellow"]
    errors = {}

    try:
        name = request.json["name"]
    except KeyError:
        errors["name"] = "A required field was not given a value"
    try:
        email = request.json["email"]
    except KeyError:
        errors["email"] = "A required field was not given a value"
    color = request.json.get("color", "Purple")
    try:
        year = request.json["year"]
    except KeyError:
        errors["year"] = "A required field was not given a value"

    if color not in colors:
        errors["color"] = "Invalid value, must be one of: red, green, orange, blue, yellow."

    if errors != {}:
        return jsonify({"errors": errors})

    num = random.randint(1, 100)
    num_fact = requests.get(f"http://numbersapi.com/{num}/math").text

    year_fact = requests.get(f"http://numbersapi.com/{year}/year").text

    return jsonify({"num": {"fact": num_fact, "num": num}, "year": {"fact": year_fact, "year": year}})
