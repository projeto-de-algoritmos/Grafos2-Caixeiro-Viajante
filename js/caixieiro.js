let noAtual = "A"
let mestrosAndados = 0
let listaDeVisitados = []
let contadorLetras = 0
vertices = ["A", "B", "C", "D", "E", "F", "G"]
arestas = [
    arestaA = ["A", "B", "C", "D", "E", "F", "G"],
    arestaB = ["A", "B", "C", "D", "E", "F", "G"],
    arestaC = ["A", "B", "C", "D", "E", "F", "G"],
    arestaD = ["A", "B", "C", "D", "E", "F", "G"],
    arestaE = ["A", "B", "C", "D", "E", "F", "G"],
    arestaF = ["A", "B", "C", "D", "E", "F", "G"],
    arestaG = ["A", "B", "C", "D", "E", "F", "G"],
    arestaH = ["A", "B", "C", "D", "E", "F", "G"]

]
function atualizarNo(letra) {
    const no = document.getElementById("texto1");
    no.innerHTML = "VOCE ESTÁ NA CIDADE " + letra
}

function contagemDeMetros() {
    const metro = document.getElementById("metros");
    metro.innerHTML = "VOCE ANDOU " + mestrosAndados + " METROS"
}
function verificaAresta(letra, noAtual) {
    aresta = []
    if (noAtual == "A") aresta = arestaA
    if (noAtual == "B") aresta = arestaB
    if (noAtual == "C") aresta = arestaC
    if (noAtual == "D") aresta = arestaD
    if (noAtual == "E") aresta = arestaE
    if (noAtual == "F") aresta = arestaF
    if (noAtual == "G") aresta = arestaG
    if (noAtual == "H") aresta = arestaH

    const no = aresta.indexOf(letra)
    if (no < 0) {
        console.log("vixe")
    }
    else {
        listaDeVisitados[contadorLetras] = letra;
        contadorLetras++;
        mestrosAndados += 500
        contagemDeMetros()
        noAtual = letra

    }
    atualizarNo(letra);
    let vitoria = true;
    if (contadorLetras < 7) vitoria = false
    if (vitoria == true) {
        // meengem 
        contadorLetras = 0;
    }
}


function verificaLetraEscolhida(letra) {
    mudarStyleLetra("tecla-" + letra);
    verificaAresta(letra, noAtual);

}
function mudarStyleLetra(tecla) {
    document.getElementById(tecla).style.background = "#C71585";
    document.getElementById(tecla).style.color = "#ffffff";
}

function carregarImagemGrafo(letra) {
    // carregar as imagens do grafo
}