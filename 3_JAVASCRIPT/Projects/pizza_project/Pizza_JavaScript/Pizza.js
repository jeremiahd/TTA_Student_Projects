// Lets store our data in an object
class Order {
	constructor() {	
		this.size = "";
		this.sizeTotal = 0;
		
		this.meats = [];
		this.meatTotal = 0.00;
		
		this.veg = [];
		this.vegTotal = 0.00;
	}
	pieSize() {
		// All size elements
		var allSizes = document.getElementsByClassName("size");
		
		// Store only selected size
		for(var i=0; i<allSizes.length; i++)
			if(allSizes[i].checked)
				this.size = allSizes[i].value;
		
		// set sizeTotal
		switch(this.size) {
			case "Personal Pizza":
				this.sizeTotal = 6;
			break;
			case "Small Pizza":
				this.sizeTotal = 8;
			break;
			case "Medium Pizza":
				this.sizeTotal = 10;
			break;
			case "Large Pizza":
				this.sizeTotal = 14;
			break;
			case "Extra Large Pizza":
				this.sizeTotal = 16;
			break;
		}		
	}
	addMeats() {
		// All meat elements
		var allMeats = document.getElementsByClassName("meats");
		
		// Store only selected meat elements
		for(var i=0; i<allMeats.length; i++)
			if(allMeats[i].checked)
				this.meats.push(allMeats[i].value)
			
		// Set meat cost
		if(this.meats.length <= 1) this.meatTotal = 0.00;
		else this.meatTotal = this.meats.length-1;
	}
	addVeggies() {
		// All veggie elements
		var allVeg = document.getElementsByClassName("veg");
		
		// Store only selected veggie elements
		for(var i=0; i<allVeg.length; i++)
			if(allVeg[i].checked)
				this.veg.push(allVeg[i].value);
		
		// Set veg cost
		if(this.veg.length <= 1) this.vegTotal = 0.00;
		else this.vegTotal = this.veg.length-1;
	}
	total() {
		return (this.sizeTotal + this.meatTotal + this.vegTotal).toFixed(2);
	}
}

function getReceipt() {
	// create order object
	order = new Order();
	
	// compute order
	order.pieSize();
	order.addMeats();
	order.addVeggies();
	
	// format output string
	var output = order.size + ": $"+order.sizeTotal.toFixed(2)+"<br /><br />";
	output += order.meats.length + " meats: $"+order.meatTotal.toFixed(2)+"<br />";
	output += order.veg.length + " veg: $"+order.vegTotal.toFixed(2)+"<br /><br />";
	output += "TOTAL: "+order.total();
	
	// output order details
	document.getElementById("output").innerHTML = output;
}