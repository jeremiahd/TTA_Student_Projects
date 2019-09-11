var globalVar = "This is global scope";

function newScope() {
	var localVar = "This is local scope";
}

/* intentionally cause an error and debug in console
document.write(localVar);
ok */

function compDate() {
	compHour = parseFloat( document.getElementById("in").value );
	if( compHour > 23 || compHour < 0|| isNaN(compHour))
		document.getElementById("out").innerHTML = "Please enter an integer between 0 and 23.";
	else if( new Date().getHours() < compHour )
		document.getElementById("out").innerHTML = "It's not time to eat yet.";
	else
		document.getElementById("out").innerHTML = "Did you eat yet?";
}