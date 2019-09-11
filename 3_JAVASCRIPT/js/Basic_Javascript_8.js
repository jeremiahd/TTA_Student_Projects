var a = "text a ";
var b = "text b ";
var c = "text c";

var d = a.concat(b, c);

function outF() {
	document.getElementById("out").innerHTML = d;
}

/* a method is a member of a class, so we named our function sliceF, even
	though step144 clearly asks for a method...I don't think you want me to 
	write a class for this exercise?...*/
function sliceF() {
	var sentence = "All work and no play makes Johnny a dull boy.";
	var index = sentence.search("Johnny");
	if(index != -1)
		var section = sentence.slice(index, index+6).toUpperCase();
	else
		var section = "String does not contain substring.";
	
	document.getElementById("slice").innerHTML = section;
}

function myToString() {
	var someNum = 12345.12345;
	var someOtherNum = someNum.toPrecision(5);
	var someOtherOtherNum = someNum.toFixed();
	out = someOtherOtherNum.toString();
	document.getElementById("tostring").innerHTML = out.valueOf();
}