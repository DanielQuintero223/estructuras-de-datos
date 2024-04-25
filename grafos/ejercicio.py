import heapq

# Definimos los puntos y las conexiones entre ellos
puntos = {
    'A': {'B': 10, 'C': 8},
    'B': {'A': 10, 'C': 90, 'D': 6},
    'C': {'A': 8, 'B': 90, 'D': 3, 'E': 12},
    'D': {'B': 6, 'C': 3, 'E': 22, 'F': 7},
    'E': {'C': 12, 'D': 22, 'F': 2},
    'F': {'D': 7, 'E': 2}
}


def dijkstra(graph, inicio):
    distancias = {vertice: float('inf') for vertice in graph}
    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        distancia_actual, vertice_actual = heapq.heappop(cola)

        if distancia_actual > distancias[vertice_actual]:
            continue

        for vecino, peso in graph[vertice_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola, (distancia, vecino))

    return distancias


# Calculamos los caminos más cortos desde cada punto
caminos_mas_cortos = {}
for punto in puntos:
    caminos_mas_cortos[punto] = dijkstra(puntos, punto)

# Imprimimos los caminos más cortos
for punto_inicio in caminos_mas_cortos:
    print(f"Caminos más cortos desde {punto_inicio}:")
    for punto_final, distancia in caminos_mas_cortos[punto_inicio].items():
        print(f"{punto_inicio} -> {punto_final}: {distancia}")
    print()
