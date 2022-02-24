document.getElementById("send-msg").addEventListener("click", function() {
	// alert("Message adressé");
	msg = document.getElementById("zone-msg").value;
	document.getElementById("zone-msg").value = "";
	
	bulle = document.createElement("li");
	bulle.classList.add("user-msg");

	bulleDiv = document.createElement("div");
	spanTexte = document.createElement("span");
	txtBulle = document.createTextNode(msg);
	spanTexte.appendChild(txtBulle);
	bulleDiv.appendChild(spanTexte); 
	bulle.appendChild(bulleDiv);
	// console.log(bulle);

	document.getElementById("lst-conv").appendChild(bulle);
});