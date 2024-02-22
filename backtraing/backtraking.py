# metodo para salir de un laberinto ( matriz )

import copy

laberinto = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

movimientos = [(-1, 0), (1, 0), (0, 1), (0, 1)]


def es_valido(f, c, L):
    return 0 <= f < len(L) and 0 <= c < len(L[0])


def es_viable(L, f, c):
    return L[f][c] == 0


def imprimir_solucion(S):
    for s in S:
        for f in s:
            print(f)
        print("------")


def bckt_laberinto(L, f, c, S):
    if es_valido(f, c, L):
        if es_viable(L, f, c):
            L[f][c] = 2
            S.append(copy.deepcopy(L))
            if f == 4 and c == 4:
                imprimir_solucion(S)
                return
            else:
                for m in movimientos:
                    bckt_laberinto(L, f+m[0], c+m[1], S)
            L[f][c] = 0
            S.pop()


bckt_laberinto(laberinto, 0, 0, [])
