let min;
let max;
let result;

document.getElementById("random").onclick = function(){
    min = Number(document.getElementById("min").value);
    max = Number(document.getElementById("max").value);

    if(min > max){
        let inter;
        inter = min;
        min = max;
        max = inter;
    }
    result = String(Math.floor(Math.random() * (max - min + 1) + min));
    document.getElementById("rep").textContent = result;
}

