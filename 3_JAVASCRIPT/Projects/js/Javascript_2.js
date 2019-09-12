function validateForm() {
	var name = document.forms["form1"]["name"].value;
	var height = document.forms["form1"]["height"].value;
	var bdate = document.forms["form1"]["bdate"].value;
	if(name=="") {
		alert("Please fill in your name!");
		return false;
	}
	if(height =="") {
		alert("Please fill in your height!");
		return false;
	}
}