var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");

function randomColor(){
    var r = Math.floor(Math.random()*256);
    var g = Math.floor(Math.random()*256);
    var b = Math.floor(Math.random()*256);
    return "rgb("+r+","+g+","+b+")";
}

function initGradient() {
	body.style.background = 
	"linear-gradient(to right, " 
	+ randomColor() 
	+ ", " 
	+ randomColor()
	+ ")";

	// css.texntent = body.style.background + ";";
}
initGradient();

function setGradient() {
	body.style.background = 
	"linear-gradient(to right, " 
	+ color1.value 
	+ ", " 
	+ color2.value 
	+ ")";

	// css.textContent = body.style.background + ";";
}

color1.addEventListener("input", setGradient);

color2.addEventListener("input", setGradient);