from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    answer = requests.get("https://api.chucknorris.io/jokes/random")
    joke = answer.json()
    return render_template("index.html", joke = joke["value"], image = joke["icon_url"])

if __name__ == '__main__':
    app.run(port = 5000)