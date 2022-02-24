document.getElementById("send-msg").addEventListener("click", sendMessage);

function sendMessage() {
	msg = document.getElementById("zone-msg").value;
	document.getElementById("zone-msg").value = "";
	document.getElementById("lst-conv").appendChild(createBulle(msg, true));
	responseBot(msg);
}

function createBulle(txt, isUser) {
	bulle = document.createElement("li");
	bulle.classList.add(isUser ? "user-msg" : "bot-msg");

	bulleDiv = document.createElement("div");
	spanTexte = document.createElement("span");
	txtBulle = document.createTextNode(txt);
	spanTexte.appendChild(txtBulle);
	bulleDiv.appendChild(spanTexte); 
	bulle.appendChild(bulleDiv);

	return bulle;
}

function responseBot(question) {
	var ajax = new XMLHttpRequest();
	var formData = new FormData();

	formData.append("question", question);
	ajax.open("POST", "http://localhost:5000/bibi-reponse");
	ajax.onload = function() {
		res = JSON.parse(ajax.response);
		document.getElementById("lst-conv").appendChild(createBulle(res.reponse, false));
	}

	ajax.send(formData);
}