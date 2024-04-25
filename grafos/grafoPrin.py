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

    def djk(self, v_inicial):
        distancias = {v: float('inf')for v in self.vertices}
        distancias[v_inicial] = 0
        visitados = set()
        cola = [(0, v_inicial)]
        while cola:
            d_act, v_act = min(cola)
            cola.remove((d_act, v_act))
            if v_act not in visitados:
                visitados.add(v_act)
                for ady, peso in self.vertices[v_act].items():
                    nueva_dist = d_act + peso
                    if nueva_dist < distancias[ady]:
                        distancias[ady] = nueva_dist
                        cola.append((nueva_dist, ady))
        return distancias

    def floyd_warshall(self):
        distancias = {v: {u: float('inf')for u in self.vertices}
                      for v in self.vertices}

        for v in self.vertices:
            distancias[v][v] = 0
            for u in self.obtener_adyacentes(v):
                distancias[v][u] = self.vertices[v][u]

        for k in self.vertices:
            for i in self.vertices:
                for j in self.vertices:
                    distancias[i][j] = min(
                        distancias[i][j], distancias[i][k]+distancias[k][j])

        return distancias


grafo = GrafoNoDirigido()
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')
grafo.agregar_vertice('G')
grafo.agregar_vertice('H')

grafo.agregar_arista('A', 'B', 9)
grafo.agregar_arista('A', 'C', 5)
grafo.agregar_arista('A', 'D', 6)
grafo.agregar_arista('B', 'C', 7)
grafo.agregar_arista('B', 'D', 3)
grafo.agregar_arista('B', 'E', 5)
grafo.agregar_arista('C', 'E', 2)
grafo.agregar_arista('C', 'F', 2)
grafo.agregar_arista('D', 'E', 1)
grafo.agregar_arista('D', 'G', 4)
grafo.agregar_arista('E', 'F', 7)
grafo.agregar_arista('E', 'G', 5)
grafo.agregar_arista('E', 'H', 1)
grafo.agregar_arista('F', 'H', 3)
grafo.agregar_arista('F', 'G', 9)

print("BFS:", grafo.bfs('A'))
print("DFS:", grafo.dfs('A'))
print("DJF:", grafo.djk('A'))
print("FW:")
print(grafo.floyd_warshall())
