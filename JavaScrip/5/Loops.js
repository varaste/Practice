function printNumbers(min, max) {
	for (var i = min; i <= max; i = i + 2)
		document.write(i + "<br />");
}

function printNumbers2(min, max) {
	var i = min;
	while (i <= max) {
		document.write(i + "<br />");
		i += 2;
	}
}

function f1() {
	var input = prompt("Enter a Number (* for Finish): ");
	var sum = 0;
	while (input != "*") {
		sum += eval(input);
		input = prompt("Enter a Number (* for Finish): ");
	}

	alert(sum);
}

//f1()

function f2() {
	var i = 1;

	do {
		alert(i);
		i += 1;
	}
	while (i < 3);
}

//f2()
var names = ["Arya", "Soroush", "Raza", "Mehran"];

function mySearch(name) {
	for (var i = 0; i < names.length; ++i) {
		if (names[i] == name) {

			continue;
		} else
			alert(names[i]);
	}


}

//mySearch("hasan")

function myObject() {
	var txt = "";
	var person = {
		fname: "Arya",
		lname: "Varaste",
		age: 20
	}
	for (var x in person) {
		txt += person[x] + "-";
	}
	alert(txt);

}

myObject();
/*var names = ["arya" , "Reza" , "Mahdi" , "sina" , "Ashkan" , "nasser"]
for(var i=0;i<names.length;++i)
	document.write(names[i]+"<br />")*/