var mass = prompt("Enter Your Mass: ");
alert("Ok Your Mass is: " + mass);

var hight = prompt("Enter Your Hight: ");
alert("Ok Your Hight is: " + hight);

var BMI = mass / ((hight / 100) * (hight / 100));
alert("Your BMI is: " + BMI);

if (BMI >= 30) {
	alert("Obese Class VI (Hyper Obese)");
} else if (BMI < 30 && BMI >= 25) {
	alert("Overweight");
} else if (BMI < 25 && BMI >= 18.5) {
	alert("Normal (healthy weight)	");
} else if (BMI < 18.5 && BMI >= 16) {
	alert("Underweight");
} else {
	alert("Severely underweight");
}


switch (x) {
	case "a":
		alert("great");
		break;
	case "b":
		alert("good");
		break;
	case "c":
		alert("not bad")
		break;
	default:
		alert("bad")
}