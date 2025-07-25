let xpf;
let eur;

const RATE = 119;

document.getElementById("sub").onclick = function(){
    eur = document.getElementById("eur").value;
    eur = Number(eur)
    xpf = eur * RATE;
    xpf = String(xpf)
    document.getElementById("xpf").value = xpf + " XPF";
}