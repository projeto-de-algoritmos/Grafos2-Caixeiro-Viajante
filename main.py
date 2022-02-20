from cgitb import html
from flask import Flask, render_template, request, flash, redirect, url_for
import random
import logging
import sys

vetorPontosTuristicos = ["Praia Leblon", "Rocinha", "Lagoa", "Jardim Botanico", " Cristo Redentos",
                         "Sambodramo", "Aeroporto", "Praia de Copacana", "Pão De Acucar", "Bahia de Guanabara"
                         ]


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        resultMap = ""
        for i in range(1, self.V):
            resultMap += "{} -  {} \t {}\n".format(
                vetorPontosTuristicos[parent[i]], vetorPontosTuristicos[i], self.graph[i][parent[i]])
        return resultMap

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return(self.printMST(parent))


app = Flask(__name__)  # sempre ao iniciar um site


# criar a primeira página do site
# route -> caminho que vem depois do dominio

# funcao -> o que quero exibir naquela página
# template


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
               [aresta1, 0, aresta4, aresta5, 0, 0, 0, aresta14, 0, 0],
               [aresta2, aresta4, 0, aresta6, 0, 0, 0, aresta19, 0, 0],
               [0, aresta5, aresta6, 0, aresta7, aresta8, 0, 0, 0, 0],
               [0, 0, 0, aresta7, 0, aresta9, aresta10, aresta12, aresta13, 0],
               [0, 0, 0, aresta8, aresta9, 0, aresta11, 0, 0, 0],
               [0, 0, 0, 0, aresta10, aresta11, 0, aresta15, aresta16, 0],
               [aresta3, aresta14, aresta19, 0, aresta15,
                   0, aresta17, 0, aresta16, 0],
               [0, 0, 0, 0, aresta13, 0, aresta16, aresta17, 0, aresta18],
               [0, 0, 0, 0, 0, 0, 0, 0, aresta18, 0], ]
    resultado = g.primMST()
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
                           resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
