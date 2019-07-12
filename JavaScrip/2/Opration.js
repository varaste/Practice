var name = "arya";
var family = "Varaste";
var n1 = 'reza';
var fullName = "reza'tavasoli'";
var test = 'arya \'varaste\' sina';

var byear = 1377;
var tavani = 8e9; //8 be tavane 9
var flo = 137.7;
var tavaniManfi = 2e-4;

var t = true;
var fal = false;

var friends = new Array();
friends[0] = "soroush";
friends[1] = "Danilal";
friends[2] = "Reza";
friends[3] = "Mehran";
friends[4] = "Mahdis";

var family = new Array("Arya", "Nastaran", "Hoseean", "Sina");

var car = ["2008", "Mazda3", "Tondar", "405"];

var friends1 = {
	firstName: "Reza",
	lastName: "Tavasoli",
	age: 22,
	BDate: "1999/10/10"
}


var student1 = {
	firstName: "soroush",
	lastName: "Mehran",
	age: 22,
	BDate: "1994/10/10"
}
var student2 = {
	firstName: "arya",
	lastName: "Mahdis",
	age: 20,
	BDate: "1996/04/10"
}
var student3 = {
	firstName: "Reza",
	lastName: "soroush",
	age: 21,
	BDate: "1995/06/10"
}
var students = [student1, student2, student3];
// alert(student1["firstName"]);
// alert(names[2]);
alert(students[1].firstName);

var sum = n1 + n2;
var remain = n1 % n2;

function changeText() {
	var sumAge = student1.age + student2.age + student3.age;
	document.getElementById("sum").innerHTML = sumAge;
}

++n1;
--n2;
n1++;
n2--;

var n3 = n1++;
//alert(n3);

var s = 10;
s += n1; // s = s+n1;
//alert(s);

var s1 = "Hi";
var s2 = "Ali";
var s3 = s1 + " " + s2;
//alert(("5"+10)+2);

var x = n1 > 50 ? 2 : 3;
//alert(x);


//var nn = null;