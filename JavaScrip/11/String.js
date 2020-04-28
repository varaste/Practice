var txt = "salaam";
alert(txt.length);
alert(txt.constructor);

var txt2 = " arya !";
var txt3 = " chetori ?";

txt = txt.concat(txt2,txt3 , " khoobi ?");
alert(txt.lastIndexOf('?' , 28));

alert(txt.replace('ali' , 'mohammad'));
var slc = txt.slice(0,3);
alert(slc);

var str = "arya,reza,mehran,karim";
var names = str.split(",", 2);
alert(names);
alert(txt.substr(1,3));
alert(txt.toUpperCase());

//Wrapper Methods
alert(txt.anchor('top'));




function employee(name, job, born) {
	this.name = name;
	this.job = job;
	this.born = born;

}

var person1 = new employee("Arya Varsate", "CEO", 1990);
employee.prototype.salary = null;
person1.salary = "70000000RLS";
alert(person1.salary);
