function lookup() {
	var key = document.getElementById("query");
	var Person = {
		name:"jeremiah",
		addr1:"1234 abc street",
		addr2:"Portland, OR"
	};
	delete Person.addr1;
	document.getElementById("out").innerHTML = Person[key.value];
}