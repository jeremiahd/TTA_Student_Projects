var incDec = 5;
incDec++;
document.write("5++ is "+incDec);
incDec--;
document.write(", but used to be "+incDec+".<br/><br/>");

var rand99 = Math.round(Math.random() * 99);
document.write("Random number from 0-99: "+rand99);

function rollOnAdd() {
	var x=5, y=6, z;
	var outString = x+" plus "+y+" equals ";
	z = x + y;
	document.getElementById("add").innerHTML = outString + z;
}
function rollOffAdd() {
	document.getElementById("add").innerHTML = "Hover for addition.";
}

function rollOnSub() {
	var x=9, y=2, z;
	var outString = x+" minus "+y+" equals ";
	z = x - y;
	document.getElementById("sub").innerHTML = outString + z;
}
function rollOffSub() {
	document.getElementById("sub").innerHTML = "Hover for subtraction.";
}

function rollOnMlt() {
	var x=95, y=4, z;
	var outString = x+" multiplied by "+y+" equals ";
	z = x * y;
	document.getElementById("mlt").innerHTML = outString + z;
}
function rollOffMlt() {
	document.getElementById("mlt").innerHTML = "Hover for multiplication.";
}

function rollOnDiv() {
	var x=99, y=11, z;
	var outString = x+" divided by "+y+" equals ";
	z = x / y;
	document.getElementById("div").innerHTML = outString + z;
}
function rollOffDiv() {
	document.getElementById("div").innerHTML = "Hover for division.";
}

function rollOnMod() {
	var x=61, y=5, z;
	var outString = x+" divided by "+y+" has a remainder of ";
	z = x % y;
	document.getElementById("mod").innerHTML = outString + z;
}
function rollOffMod() {
	document.getElementById("mod").innerHTML = "Hover for the remainder.";
}

function rollOnXxx() {
	var a=3, b=6, c=9, d=4, e=1, f;
	var outString = a+" * "+c+" + "+b+" / ("+d+" - "+e+") = ";
	f = a*c + b / (d-e);
	document.getElementById("xxx").innerHTML = outString + f;
}
function rollOffXxx() {
	document.getElementById("xxx").innerHTML = "Hover for order of ops fun.";
}

function rollOnNeg() {
	var x = 10;
	document.getElementById("neg").innerHTML = "Negative "+x+" is "+-x;
}
function rollOffNeg() {
	document.getElementById("neg").innerHTML = "Hover for negative value";
}