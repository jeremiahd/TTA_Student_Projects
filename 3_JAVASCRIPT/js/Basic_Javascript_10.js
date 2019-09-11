function callLoop() {
	var a = [];
		a[0]= "Some ";
		a[1] = "silly ";
		a[2] = "strings.";
	for(i = 0; i< a.length; i++) {
		document.getElementById("loop").innerHTML += a[i];
		if(i === 0) continue;
		if(i === 1) break;
	}
}

function constant_function() {
	var opinionString = "";
	{
		let opinionString = "Ugly language is ugly";
	}
	document.getElementById("opinion").innerHTML = opinionString;
	const Musical_Instrument = {type:"guitar", brand:"Ibanez", color:"black"};
	document.getElementById("constant").innerHTML = Musical_Instrument.brand;
	Musical_Instrument.type = "piano"; // wut?
	Musical_Instrument.newType = "test";
	document.getElementById("outChange").innerHTML = "Changed: "+Musical_Instrument.type+"<br/>";
	document.getElementById("outNew").innerHTML = "New: "+Musical_Instrument.newType+"<br/>";
	document.getElementById("rString").innerHTML = returnString();
}

function returnString() {
	let car = {
		make: "Dodge ",
		model: "Viper ",
		year: "2021 ",
		color: "red ",
		description : function() {
			return "The car is a "+this.year+this.color+this.make+this.model;
		}
	}
	return car.description();
}