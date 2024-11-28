from flask import Flask, render_template, request, jsonify
import requests, random

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    answer = requests.get("https://api.chucknorris.io/jokes/random")
    joke = answer.json()
    answer = requests.get("https://api.chucknorris.io/jokes/categories")
    categories = answer.json()
    if request.method == "POST" :
        search = request.form["search"]
        if search:
            try:
                query = search
                answer = requests.get(f"https://api.chucknorris.io/jokes/search?query={query}")
                joke = answer.json()
                return render_template("index.html", joke = joke["result"][random.randint(0, joke["total"]-1)]["value"], categories = categories)
            except:
                return render_template("index.html", joke = "Invalid search", categories = categories)
        else:
            categorie = request.form["cat"]
            answer = requests.get(f"https://api.chucknorris.io/jokes/random?category={categorie}")
            joke = answer.json()
            return render_template("index.html", joke = joke["value"], image = joke["icon_url"], categories = categories)
    return render_template("index.html", joke = joke["value"], image = joke["icon_url"], categories = categories)

@app.route("/uni", methods=["POST", "GET"])
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

@app.route("/jschat", methods=["POST", "GET"])
def jschat():
    return render_template("jschat.html")

@app.route("/jschat/send", methods=["POST"])
def send():
    answer = request.json
    if answer ["saturs"] == "\clear":
        with open("chatMessage.txt", "w") as f:
            f.write("")
        return "Izdzests"
    with open("chatMessage.txt", "a") as f:
        f.write(answer["name"])
        f.write("----")
        f.write(answer["saturs"])
        f.write("\n")
    return jsonify("OK")

@app.route("/jschat/read")
def read():
    answer = []
    with open("chatMessage.txt", "r") as f:
        answer = f.readlines()
    return answer

if __name__ == '__main__':
    app.run(port = 5000)


