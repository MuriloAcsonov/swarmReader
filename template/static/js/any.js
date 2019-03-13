var acc;
window.onload = function () { acc = document.getElementsByClassName("accordion"); var i;
for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", ScrollInfo);
}
}

function ScrollInfo(){
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight){
        panel.style.maxHeight = null;
    }
    else {
        panel.style.maxHeight = panel.scrollHeight + "px";
    }
}