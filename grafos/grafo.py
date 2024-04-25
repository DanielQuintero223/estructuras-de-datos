# -*- coding: utf-8 -*-
from collections import deque


class GrafoNoDirigido:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, valor):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1][vertice2] = valor
            self.vertices[vertice2][vertice1] = valor

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_adyacentes(self, vertice):
        return list(self.vertices[vertice].keys())

    def bfs(self, vertice_inicial):
        visitados = set()
        cola = deque([vertice_inicial])
        recorrido = []

        while cola:
            vertice = cola.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                recorrido.append(vertice)
                for adyacente in self.vertices[vertice]:
                    if adyacente not in visitados:
                        cola.append(adyacente)
        return recorrido

    def dfs(self, vertice_inicial):
        visitados = set()
        pila = [vertice_inicial]
        recorrido = []

        while pila:
            vertice = pila.pop()
            if vertice not in visitados:
                visitados.add(vertice)
                recorrido.append(vertice)
                for adyacente in self.vertices[vertice]:
                    if adyacente not in visitados:
                        pila.append(adyacente)
        return recorrido

    def dijkstra(self, vertice_inicial):
        distancias = {v: float('inf')for v in self.vertices}
        distancias[vertice_inicial] = 0
        visitados = set()
        cola = [(0, vertice_inicial)]
        while cola:
            d_act, v_act = min(cola)
            cola.remove((d_act, v_act))
            if v_act not in visitados:
                visitados.add(v_act)
                for ady, peso in self.vertices[v_act].items():
                    n_dist = d_act+peso
                    if n_dist < distancias[ady]:
                        distancias[ady] = n_dist
                        cola.append((n_dist, ady))
        return distancias

    def floyd_warshall(self):
        distancias = {v: {u: float('inf') for u in self.vertices}
                      for v in self.vertices}

        for v in self.vertices:
            distancias[v][v] = 0

        for v1 in self.vertices:
            for v2 in self.vertices[v1]:
                distancias[v1][v2] = self.vertices[v1][v2]

        for k in self.vertices:
            for i in self.vertices:
                for j in self.vertices:
                    distancias[i][j] = min(
                        distancias[i][j], distancias[i][k] + distancias[k][j])

        return distancias

    def primm(self, vertice_inicial):
        arbol_recubridor = []
        visitados = set()
        visitados.add(vertice_inicial)
        aristas_candidatas = []

        for adyacente, peso in self.vertices[vertice_inicial].items():
            aristas_candidatas.append((peso, vertice_inicial, adyacente))

        while aristas_candidatas:
            aristas_candidatas.sort()
            peso, origen, destino = aristas_candidatas.pop(0)

            if destino not in visitados:
                visitados.add(destino)
                arbol_recubridor.append((origen, destino, peso))

                for adyacente, peso in self.vertices[destino].items():
                    if adyacente not in visitados:
                        aristas_candidatas.append((peso, destino, adyacente))

        return arbol_recubridor

    def bellman_ford(self, vertice_inicial):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[vertice_inicial] = 0

        for _ in range(len(self.vertices) - 1):
            for origen in self.vertices:
                for destino, peso in self.vertices[origen].items():
                    if distancias[origen] + peso < distancias[destino]:
                        distancias[destino] = distancias[origen] + peso

        for origen in self.vertices:
            for destino, peso in self.vertices[origen].items():
                if distancias[origen] + peso < distancias[destino]:
                    raise ValueError("El grafo contiene un ciclo negativo.")

        return distancias

    def kruskal(self):
        arbol_recubridor = []
        aristas = []

        for origen in self.vertices:
            for destino, peso in self.vertices[origen].items():
                aristas.append((peso, origen, destino))

        aristas.sort()
        conjuntos = [{vertice} for vertice in self.vertices]

        for peso, origen, destino in aristas:
            conjunto_origen = None
            conjunto_destino = None

            for conjunto in conjuntos:
                if origen in conjunto:
                    conjunto_origen = conjunto
                if destino in conjunto:
                    conjunto_destino = conjunto

            if conjunto_origen != conjunto_destino:
                arbol_recubridor.append((origen, destino, peso))
                conjunto_origen.update(conjunto_destino)
                conjuntos.remove(conjunto_destino)

        return arbol_recubridor


def numero_componentes_conexos(grafo):
    visitados = set()
    componentes_conexos = 0

    def dfs(nodo):
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                dfs(vecino)

    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo)
            componentes_conexos += 1

    return componentes_conexos


# Ejemplo de uso de componentes conexos:
 # grafo_ejemplo = {
 #   'A': ['B', 'C'],
 #   'B': ['A', 'D'],
 #   'C': ['A'],
 #   'D': ['B'],
 #   'E': ['F'],
 #   'F': ['E']
# }

 # print(numero_componentes_conexos(grafo_ejemplo))
