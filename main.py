from cgitb import html
from hashlib import new
from xml.dom.expatbuilder import parseString
from flask import Flask, render_template, request, flash, redirect, url_for
import random
import logging
import sys

vetorPontosTuristicos = ["Praia Leblon", "Rocinha", "Lagoa", "Jardim Botânico", " Cristo Redentor",
                         "Sambódramo", "Aeroporto", "Praia de Copacabana", "Pão De Açúcar", "Baía de Guanabara"
                         ]


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        totalMap = 0
        new_line = "\n"
        resultMap = ""
        for i in range(1, self.V):
            resultMap += '{} -  {}  R$ {},00 . '.format(
                vetorPontosTuristicos[parent[i]], vetorPontosTuristicos[i], self.graph[i][parent[i]], new_line)
            resultMap += "\n"
            totalMap += self.graph[i][parent[i]]

        return resultMap

    def printMST1(self, parent):
        totalMap = 0
        for i in range(1, self.V):
            totalMap += self.graph[i][parent[i]]

        return "R${},00".format(totalMap)

    def minKey(self, key, mstSet):

        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return(self.printMST(parent))

    def primMST1(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return(self.printMST1(parent))


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    aresta1 = random.randrange(1, 52)
    aresta2 = random.randrange(1, 52)
    aresta3 = random.randrange(1, 52)
    aresta4 = random.randrange(1, 52)
    aresta5 = random.randrange(1, 52)
    aresta6 = random.randrange(1, 52)
    aresta7 = random.randrange(1, 52)
    aresta8 = random.randrange(1, 52)
    aresta9 = random.randrange(1, 52)
    aresta10 = random.randrange(1, 52)
    aresta11 = random.randrange(1, 52)
    aresta12 = random.randrange(1, 52)
    aresta13 = random.randrange(1, 52)
    aresta14 = random.randrange(1, 52)
    aresta15 = random.randrange(1, 52)
    aresta16 = random.randrange(1, 52)
    aresta17 = random.randrange(1, 52)
    aresta18 = random.randrange(1, 52)
    aresta19 = random.randrange(1, 52)
    g = Graph(10)
    g.graph = [[0, aresta1, aresta2, 0, 0, 0, 0, aresta3, 0, 0],
               [aresta1, 0, aresta4, aresta5, 0, 0, 0, 0, 0, 0],
               [aresta2, aresta4, 0, aresta14, 0, 0, 0, aresta19, 0, 0],
               [0, aresta5, aresta6, 0, aresta7, aresta8, 0, 0, 0, 0],
               [0, 0, aresta14, aresta7, 0, aresta9,
                   aresta10, aresta12, aresta13, 0],
               [0, 0, 0, aresta8, aresta9, 0, aresta11, 0, 0, 0],
               [0, 0, 0, 0, aresta10, aresta11, 0, aresta15, aresta16, 0],
               [aresta3, 0, aresta19, 0, aresta15,
                   0, aresta17, 0, aresta16, 0],
               [0, 0, 0, 0, aresta13, 0, aresta16, aresta17, 0, aresta18],
               [0, 0, 0, 0, 0, 0, 0, 0, aresta18, 0], ]
    resultado = g.primMST()
    total = g.primMST1()
    return render_template("homepage.html", aresta1=aresta1,
                           aresta2=aresta2,
                           aresta3=aresta3,
                           aresta4=aresta4,
                           aresta5=aresta5,
                           aresta6=aresta6,
                           aresta7=aresta7,
                           aresta8=aresta8,
                           aresta9=aresta9,
                           aresta10=aresta10,
                           aresta11=aresta11,
                           aresta12=aresta12,
                           aresta13=aresta13,
                           aresta14=aresta14,
                           aresta15=aresta15,
                           aresta16=aresta16,
                           aresta17=aresta17,
                           aresta18=aresta18,
                           aresta19=aresta19,
                           resultado=resultado,
                           total=total)


if __name__ == "__main__":
    app.run(debug=True)
