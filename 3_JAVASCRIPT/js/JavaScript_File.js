var string1="string1", string2="string2", string3="string3";
var string1 = string1.fontcolor("red");
var string2 = string2.fontcolor("green");
var string3 = string3.fontcolor("blue");

string1 + string2; //expression example

document.write(string1+"<br>");
document.write(string2+"<br>");
document.write(string3+"<br>");

function myFirstFunction() {
	var str = "This text is green!";
	var result = str.fontcolor("green");
	document.getElementById("Green_Text").innerHTML = result;
}

function keyDown() {
	document.write("Someone pressed a key!<br/>");
}