

var x = document.getElementById("firstblock");
var z = document.getElementById("secondblock");
var y = document.getElementById("thirdblock");

function showfirst() {
    if (x.style.display === "none") {
        x.style.display = "block";
        z.style.display = "none";
        y.style.display = "none";
    } else {
        x.style.display = "none";
    }
}

function showsecond() {
    if (z.style.display === "none") {
        z.style.display = "block";
        x.style.display = "none";
        y.style.display = "none";
    } else {
        z.style.display = "none";
    }
}

function showthird() {
    if (y.style.display === "none") {
        y.style.display = "block";
        z.style.display = "none";
        x.style.display = "none";
    } else {
        y.style.display = "none";
    }
}

