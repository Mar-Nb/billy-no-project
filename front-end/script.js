document.getElementById("send-msg").addEventListener("click", sendMessage);
document.getElementById("zone-msg").addEventListener("keyup", function(evt) {
	if (evt.key == "Enter") { sendMessage(); }
});

function sendMessage() {
	msg = document.getElementById("zone-msg").value;
	document.getElementById("zone-msg").value = "";
	createBulle(msg, true);
	responseBot(msg);
	document.getElementsByTagName("main")[0].scrollTop = document.getElementsByTagName("main")[0].scrollHeight;
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
	
	document.getElementById("lst-conv").appendChild(bulle);
}

function loadingBulle() {
	bulle = document.createElement("li");
	bulle.classList.add("bot-msg");
	bulleDiv = document.createElement("div");
	spanImage = document.createElement("span");
	imageLoad = document.createElement("img");

	imageLoad.src = "loader-bibi.gif";
	imageLoad.width = 30;
	bulle.id = "loader";
	
	spanImage.appendChild(imageLoad);
	bulleDiv.appendChild(spanImage);
	bulle.appendChild(bulleDiv);
	document.getElementById("lst-conv").appendChild(bulle);
}

function responseBot(question) {
	loadingBulle();
	var ajax = new XMLHttpRequest();
	var formData = new FormData();

	formData.append("question", question);
	ajax.open("POST", "http://localhost:5000/bibi-reponse");
	ajax.onload = function() {
		res = JSON.parse(ajax.response);
		console.log(res);
		document.getElementById("loader").remove();
		createBulle(res.reponse, false);
		document.getElementsByTagName("main")[0].scrollTop = document.getElementsByTagName("main")[0].scrollHeight;
	}

	ajax.send(formData);
}