var names = ["arya", "varaste", "nastaran"];
alert(names.length);
var names2 = ["hp", "mahdi"];
var names3 = ["reza", "soroush", "mehran"];

names = names.concat(names2, names3);

alert(names.join("*"));
alert(names);
alert(names.pop());
names.push("mostafa", "danial", "Amir");
names.reverse();
alert(names.slice(-4,-2));
alert(names);
names.splice(4, 2, "pari", "sina");
alert(names);