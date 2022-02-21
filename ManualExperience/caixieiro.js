metrosAndados = 0;


function selecionaAresta(numero) {
    document.getElementById("Shape-" + numero).setAttribute("disabled", "disabled");
    document.getElementById("Shape-" + numero).style.fill = "#333"
    document.getElementById("Line-" + numero).style.stroke = 'red'
    const aresta = document.getElementById("Line-" + numero);
    const metro = parseFloat(aresta.getAttribute('code'))
    metrosAndados = metrosAndados + metro
    const name = document.getElementById("text");
    name.innerText = "Você andou " + metrosAndados + " kilometros";


};





