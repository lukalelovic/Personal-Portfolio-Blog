window.onscroll = function () { scrollFunction() };
var nav = document.getElementById("navbar");
var clicked = false;

function scrollFunction() {
    let width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);

    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        nav.style.top = "0";
    } else {
        nav.style.top = "-75px";
    }

    if (width > 1000) 
    {
        nav.style.height = "60px";
        document.getElementById("navbar-right-align").style.visibility = "visible";
        clicked = false;
    } else if (clicked == false) {
        document.getElementById("navbar-right-align").style.visibility = "hidden";
    }
}

function dropDown() {
    if (nav.style.height == "60px") {
        nav.style.height = "25vw";
        document.getElementById("navbar-right-align").style.visibility = "visible";
        clicked = true;
    } else {
        nav.style.height = "60px";
        document.getElementById("navbar-right-align").style.visibility = "hidden";
    }
}