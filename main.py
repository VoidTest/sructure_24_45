from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    answer = requests.get("https://api.chucknorris.io/jokes/random")
    joke = answer.json()
    answer = requests.get("https://api.chucknorris.io/jokes/categories")
    categories = answer.json()
    if request.method == "POST" :
        categorie = request.form["cat"]
        answer = requests.get(f"https://api.chucknorris.io/jokes/random?category={categorie}")
        joke = answer.json()
    return render_template("index.html", joke = joke["value"], image = joke["icon_url"], categories = categories)

@app.route("/uni")
def uni():
    answer = requests.get("http://universities.hipolabs.com/search?country=latvia")
    all = answer.json()
    print(all[3]["web_pages"][0])
    nosaukumi = []
    for elements in all:
        added = {
            "nosaukums" : elements["name"],
            "majaslapas" : elements["web_pages"]
        }
        nosaukumi.append(added)

    return render_template("uni.html", uni=nosaukumi)

if __name__ == '__main__':
    app.run(port = 5000)


