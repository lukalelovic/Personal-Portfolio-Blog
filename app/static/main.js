window.onscroll = function () { scrollFunction() };
var nav = document.getElementById("nBar");

function scrollFunction() {
    let width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);

    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        nav.style.top = "0";
    } else {
        nav.style.top = "-75px";
    }
}
