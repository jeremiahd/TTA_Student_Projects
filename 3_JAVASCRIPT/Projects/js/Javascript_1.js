function foodF() {
	var output;
	var food = document.getElementById("input").value;
	var outString = " is delicious!";
	switch(food) {
		case "Pizza":
			output = "Pizza" + outString;
		break;
		case "Fried Chicken":
			output = "Chicken that is fried" + outString;
		break;
		case "Hamberders":
			output = "They're called hambURGERS, and yes, a hamburger" + outString;
		break;
		case "Tacos":
			output = "A taco certainly" + outString;
		break;
		case "Pasta":
			output = "Pasta" + outString;
		break;
		case "Stir Fry":
			output = "Stir Fry" + outString;
		break;
		default:
			output = "Please enter a food exactly as written on the above list.";
	}
	document.getElementById("output").innerHTML = output;
	
	var foodlist = document.getElementsByClassName("foods");
	for(i=0; i<foodlist.length; i++) 
		document.getElementById("output2").innerHTML += foodlist[i].textContent+"<br />"
	
	var canvas = document.getElementById("canvasTest");
	var ctx = canvas.getContext("2d");
	var grd = ctx.createLinearGradient(0,0,200,150);
	grd.addColorStop(0, "black");
	grd.addColorStop(1, "white");
	ctx.fillStyle = grd;
	ctx.fillRect(0,0,200,150);	
}