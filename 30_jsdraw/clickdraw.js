var  c  = document.getElementById("slate")

var ctx = c.getContext("2d")

var mode = "rect";
var toggleMode = (e) =>{
    console.log("toggling...");
    if(mode === "rect"){
        mode = "circle";
        bToggler.textContent = "rectangle";
    }
    else{
        mode = "rect";
        bToggler.textContent = "circle";
    }
}

var drawRect = function(e){
    var mouseX = e.clientX - c.offsetLeft;
    var mouseY = e.clientY - c.offsetTop;
    console.log("mouseclick registered at ", mouseX, mouseY);

    ctx.fillRect(mouseX, mouseY, 20, 80);

}
var drawCircle = function(e) {
    var mouseX = e.clientX - c.offsetLeft;
    var mouseY = e.clientY - c.offsetTop;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 30, 0, 2 * Math.PI  );
    ctx.fill();

}

var draw = (e) => {
    if(mode == "rect"){
        drawRect(e);
    } else{
        drawCircle(e);
    }
}
var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.innerText = "circle";
bToggler.addEventListener("click", toggleMode)

var clearB = document.getElementById("buttonClear");
clearB.innerText = "wipe";
clearB.addEventListener("click", wipeCanvas);

