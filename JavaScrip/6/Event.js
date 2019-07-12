function page_load() {
	//some code
}

function txt2_focus() {

	//alert("I'm in")
}

function txt1_blur() {
	//	alert("I'm Out")
}

function txt1_keyup(e) {
	if (e.keyCode != 8 && e.keyCode != 13)
		document.getElementById('counter').innerHTML = eval(document.getElementById('counter').innerHTML) + 1
	else if (document.getElementById('counter').innerHTML != 0 && e.keyCode == 8)
		document.getElementById('counter').innerHTML = eval(document.getElementById('counter').innerHTML) - 1
	else if (e.keyCode == 13)
		document.getElementById('txt2').focus()
}

function txt1_keydown(e) {
	if (e.keyCode == 56)
		e.preventDefault()
}

function txt2_mouseover(elem) {
	elem.value = "mouseover"
}

function txt2_mouseout(elem) {
	elem.value = ""
}