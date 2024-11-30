const LAIKS = 5000;

async function sendMessage() {
    let message = document.getElementById("text").value;
    let name = document.getElementById("name").value;
    document.getElementById("text").value = "";
    const answer = await fetch("/jschat/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"saturs": message, "name": name})
    });
    readMessages()
}

async function readMessages() {
    const answer = await fetch("/jschat/read");
    messages = await answer.json();
    showMessages(messages);
    await new Promise(resolve => setTimeout(resolve, LAIKS));
    await pink()
    await readMessages();
}

function showMessages(saturs) {
    let place = document.getElementById("chat");
    text = "" ;
    for(rinda of saturs) {
        elementi = rinda.split("----");
        text += "<b>" + elementi[0] + "</b> - " + elementi[1] + "<br>";
    }
    place.innerHTML = text;
}

async function pink() {
    const place = document.getElementById("chat");
    const answer = await fetch("/jschat/pink");
    ispink = await answer.json(); 
    if (ispink === "is pink") {
        place.style.color = "pink";
    } else {
        place.style.color = "black";
    }
}
