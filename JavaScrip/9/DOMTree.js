function addNewLink() {
	var newLink = document.createElement('a');

	//method 1
	var linkText = document.createTextNode('Link 3');
	newLink.appendChild(linkText);

	//method 2
	newLink.innerHTML = "Link 3";

	newLink.href = "#";
	newLink.onclick = function () {
		alert();
	}
	document.getElementById('d1').appendChild(newLink);

	var target = document.getElementById('d1').getElementsByTagName('a')[0];

	//document.getElementById('d1').insertBefore(newLink , target );
	//document.getElementById('d1').replaceChild(newLink , target );
}

function removeLink() {
	var parent = document.getElementById('d1');
	var child = document.getElementById('d1').getElementsByTagName('a')[0];

	parent.removeChild(child);
}

function ff() {
	//alert(document.documentElement.innerHTML)
	alert(document.body);
}