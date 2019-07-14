var patt = /[^ا-ی]/;
var txt = "salaam 100";
var name = prompt("Enter Your Name : ");


if (!patt.test(name))
	alert('Your name is valid');
else
	alert('Your name is wrong');

var patt2 = /\D/;
var n = prompt("Enter a number : ");
if (patt2.test(n))
	alert('Your input is NaN');
else
	alert('Your input is a number');


var patt3 = /^[a-z]/;
alert(patt3.test("ali salaam"));