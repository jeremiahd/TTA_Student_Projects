var someFloat = Math.random();
var varType = typeof someFloat;
document.write(someFloat+" is a "+varType+".<br/><br/>");

var testNan = 0/0;
document.write("var testNan = 0/0;<br/>");
document.write("Hey javascript, why does a variable that is "+testNan+" return a typeof '"+typeof testNan+"'? :\\<br/>");
document.write("If we use the isNaN() function, we can see it is ");
if(isNaN(testNan))
	document.write("TRUE");
else
	document.write("FALSE");
document.write(" that testNan is 'Not a Number'.<br/><br/>");

document.write("displaying infinity: "+2E310+" and negative infinity: "+-2E310);

document.write("<br/><br/>");

document.write(10>2);
document.write(10<2);

console.log(2 + 2);

document.write("<br/><br/>");

var z = 12;
console.log(typeof z == 'string');
var x = 5;
var y = "five";
z = x + y;
document.write("Type coercion: "+z);
console.log(typeof z == 'string');

document.write("<br/><br/>");

var a = 10;
var b = 10;
var c = "20";
var d = "10";
var e = 20;
var f = 20;

document.write("Matching data type and value: "+(a===b)+"<br/>");
document.write("Different data type and different value: "+(a===c)+"<br/>");
document.write("Different data type but same value: "+(a===d)+"<br/>");
document.write("Same data type but different value: "+(a===e)+"<br/>");

document.write("<br/><br/>");

document.write("&&<br/>");
document.write( "True: "+(a===b &&  e ===f)+" False: "+(a===b && a===d) );
document.write("<br/><br/>||<br/>");
document.write( "True: "+(a===b ||  a ===d)+" False: "+(a===d || c===d) );

document.write("<br/><br/>Not<br/>");
document.write("True: "+(a!=e)+" False: "+(a!=b));