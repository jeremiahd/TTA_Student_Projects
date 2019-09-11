function Vehicle(Make, Model, Year, Color) {
	this.Vehicle_Make = Make;
	this.Vehicle_Model = Model;
	this.Vehicle_Year = Year;
	this.Vehicle_Color = Color;
}
var Jack = new Vehicle("Dodge", "Viper", 2020, "Red");
var Emily = new Vehicle("Jeep", "Trail Hawk", 2019, "White and Black");
var Erik = new Vehicle("Ford", "Pinto", 1971, "Mustard");

function JavascriptClass(param1, param2) {
	this.attr1 = param1;
	this.attr2 = param2;

}

var Jclass = new JavascriptClass("functionsCan", "beClasses?");

/* attempt to use a keyword per step 124
var null = NaN;
document.write(null);
*/

function myFunction() {
	document.getElementById("keywordsAndConstructors").innerHTML = 
	"Erik drives a " + Erik.Vehicle_Color + "-colored " + Erik.Vehicle_Model +
	" manufactured in " + Erik.Vehicle_Year;
}

function step122() {
	var out = Jclass.attr1 + Jclass.attr2;
	document.getElementById("newAndThis").innerHTML = out;
}

function nest() {
	var attr1 = getAttr1();
	document.getElementById("nestedFunction").innerHTML = attr1;
	function getAttr1() {
		return Jclass.attr1;
	}
}