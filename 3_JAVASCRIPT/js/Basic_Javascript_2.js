function addForm() {
	var x = parseFloat( document.getElementById("xValue").value );
	var y = parseFloat( document.getElementById("yValue").value );
	z = x + y;
	outputString = x;
	outputString += " plus ";
	outputString += y;
	outputString += " equals ";
	outputString += z;
	outputString += ".<br/>";
	document.getElementById("output").innerHTML = outputString;
}