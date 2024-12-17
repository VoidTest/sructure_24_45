from flask import Flask, render_template, request, jsonify
import os, requests, random

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["POST", "GET"])
def index():
    answer = requests.get("https://api.chucknorris.io/jokes/random")
    joke = answer.json()
    answer = requests.get("https://api.chucknorris.io/jokes/categories")
    categories = answer.json()
    if request.method == "POST":
        search = request.form["search"]
        if search:
            try:
                query = search
                answer = requests.get(f"https://api.chucknorris.io/jokes/search?query={query}")
                joke = answer.json()
                return render_template("index.html", joke=joke["result"][random.randint(0, joke["total"]-1)]["value"], categories=categories)
            except:
                return render_template("index.html", joke="Invalid search", categories=categories)
        else:
            categorie = request.form["cat"]
            answer = requests.get(f"https://api.chucknorris.io/jokes/random?category={categorie}")
            joke = answer.json()
            return render_template("index.html", joke=joke["value"], image=joke["icon_url"], categories=categories)
    return render_template("index.html", joke=joke["value"], image=joke["icon_url"], categories=categories)

@app.route("/uni", methods=["POST", "GET"])
def uni():
    answer = requests.get("http://universities.hipolabs.com/search?country=latvia")
    all = answer.json()
    nosaukumi = []
    for elements in all:
        added = {
            "nosaukums": elements["name"],
            "majaslapas": elements["web_pages"]
        }
        nosaukumi.append(added)

    return render_template("uni.html", uni=nosaukumi)

@app.route("/jschat", methods=["POST", "GET"])
def jschat():
    return render_template("jschat.html")

@app.route("/jschat/send", methods=["POST"])
def send():
    answer = request.json
    banned = []
    with open("chatBan.txt", "r") as f:
        banned = f.readlines()
    if answer["name"] + "\n" in banned:
        return "User is banned"

    if answer["saturs"] == "\\clear":
        with open("chatMessage.txt", "w") as f:
            f.write("")
        with open("chatBan.txt", "w") as f:
            f.write("")
        return "Izdzests"
    elif answer["saturs"] == "\\pink":
        pink("is pink")
    elif answer["saturs"] == "\\ban":
        with open("chatBan.txt", "a") as f:
            f.write(answer["name"])
            f.write("\n")
        return "Banned"
    with open("chatMessage.txt", "a") as f:
        f.write(answer["name"])
        f.write("----")
        f.write(answer["saturs"])
        f.write("\n")
    return jsonify("OK")

globalPink = "not pink"

@app.route("/jschat/pink")
def pink(ispink="not pink"):
    global globalPink
    if ispink != "not pink":
        globalPink = ispink
    elif globalPink != "is pink":
        globalPink = "not pink"
    return jsonify(globalPink)

@app.route("/jschat/read")
def read():
    answer = []
    with open("chatMessage.txt", "r") as f:
        answer = f.readlines()
    return answer

# File upload route (allows all file formats)
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Check if the request has a file part
        if "file" not in request.files:
            return "No file part in the request", 400
        file = request.files["file"]
        # If no file is selected
        if file.filename == "":
            return "No file selected for uploading", 400
        # Save the file without format restrictions
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        return f"File successfully uploaded: {filepath}", 200
    return render_template("upload.html")

if __name__ == '__main__':
    # Bind to 0.0.0.0 to make it accessible to all devices on the network
    app.run(host='0.0.0.0', port=5000)
