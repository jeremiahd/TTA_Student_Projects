// set our starting index
var slideIndex = 1;
// display our slide...this writes to our document on load
showSlides(slideIndex);

//increment slide index
function incSlide(n) {
	showSlides(slideIndex += n);
}

/*set slide index to the slide indicated by n, and call
	showSlides for the new index */
function showSlide(n) {
	showSlides(slideIndex = n);
}

/*iterate through slides and dots, set all to inactive,
	then set active slide and dot at the correct indices */
function showSlides(n) {
	var i;
	var slides = document.getElementsByClassName("slide");
	var dot = document.getElementsByClassName("dot");
	if(n > slides.length) {slideIndex = 1} // don't increment past our images
	if(n < 1) {slideIndex = slides.length} // don't decrement into negatives
	for(i=0;i<slides.length; i++)
		slides[i].style.display = "none";
	for(i=0; i<dot.length; i++)
		dot[i].className = dot[i].className.replace(" active", "");
	slides[slideIndex-1].style.display = "block";
	dot[slideIndex-1].className += " active";
}