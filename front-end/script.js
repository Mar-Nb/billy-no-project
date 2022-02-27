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
	
	if (txt.includes("<") && txt.includes(">")) {
		spanTexte.innerHTML = txt;
	} else {
		txtBulle = document.createTextNode(txt);
		spanTexte.appendChild(txtBulle);
	}

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
		if(ajax.response.includes("album"))
		{
			res = JSON.parse(ajax.response);
			res2 = JSON.parse(res.reponse);
			var parser = new DOMParser();
			response = ""
			for(opening  in res2){
				if(res2[opening].audio != null)
				{
					response = response + res2[opening].album + "<br/>"		
					response = response + "<audio controls src='" + res2[opening].audio + "'><code>audio</code></audio><br/>"
				}
			}	
			response = parser.parseFromString(response, 'text/html');
			console.log(response.body);
			document.getElementById("lst-conv").appendChild(createBulle(response.body.innerHTML, false));
		}
		else if (ajax.response.includes("error")){
			res = JSON.parse(ajax.response);
			res2 = JSON.parse(res.reponse);
			err = JSON.parse(res2);
			document.getElementById("lst-conv").appendChild(createBulle(err.error, false));
			document.getElementById("name-anime").value = err.anime;
		}
		else{
			res = JSON.parse(ajax.response);
			document.getElementById("lst-conv").appendChild(createBulle(res.reponse, false));	
		}
	}

	ajax.send(formData);
}

function addOp(){
	var ajax = new XMLHttpRequest();
	var formData = new FormData();
	name_anime = document.getElementById("name-anime").value;
	anime = "Opening ajouter "+document.getElementById("input-"+name_anime).value + "|" + document.getElementById("input-url-"+name_anime).value;
	console.log(anime);
	formData.append("question", anime);
	ajax.open("POST", "http://localhost:5000/bibi-reponse");
	ajax.onload = function() {
		res = JSON.parse(ajax.response);
		console.log(res);
		document.getElementById("lst-conv").appendChild(createBulle(res.reponse, false));	
	}	
	ajax.send(formData);	
}