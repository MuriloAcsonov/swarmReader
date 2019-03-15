var acc;
var timer;
window.onload = function () { acc = document.getElementsByClassName("accordion"); var i;
for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", ScrollInfo);
}
clearCache();
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

function FillInfo(microservice){
    if(localStorage[microservice]){
        console.log(microservice+" "+localStorage.getItem(microservice));
    }
    else{        
        getInfo(microservice);
        
    }    
}

async function getInfo(microservice){
    var req = new XMLHttpRequest();
    var url = 'http://127.0.0.1:5000/info'
    req.open("GET", url, true);    
    req.send();    
    
    req.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            localStorage.setItem(microservice, req.responseText);            
            organizeDict(microservice);
        }
    }

}

function organizeDict(microservice){
        console.log("ORGANIZE");
        var info = JSON.parse(localStorage[microservice]).filter(function(item){
            return typeof(item);
        });
        console.log(info);
}

function CreateHtml(element, subtitle, value){
    var para = document.createElement("p");
    var node = document.createTextNode(subtitle+": "+value);
    para.appendChild(node)
    element.appendChild(para)
}

function clearCache(){    
    localStorage.clear();
    setTimeout(clearCache, 300000);
}