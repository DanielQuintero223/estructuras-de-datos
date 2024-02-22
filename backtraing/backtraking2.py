# movimientos del caballo
import copy

tablero = [
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

movimientos = [(-2, 1), (-2, -1), (1, 2), (1, -2),
               (-1, 2), (-1, -2), (2, -1), (2, 1)]


def es_Valido(T, f, c,):
    return 0 <= f < len(T) and 0 <= c < len(T[0])


def es_viable(T, f, c):
    return T[f][c] == 0


def imprimir_solucion(S):
    for s in S:
        for f in s:
            print(f)
        print("------")


def bckt_tablero(T, f, c, S, n):
    if es_Valido(T, f, c):
        if es_viable(T, f, c):
            T[f][c] = n
            S.append(copy.deepcopy(T))
            if n == 12:
                imprimir_solucion(S)
                return
            else:
                n += 1
                for m in movimientos:
                    bckt_tablero(T, f+m[0], c+m[1], S, n)
            T[f][c] = 0
            n -= 1
            S.pop()


bckt_tablero(tablero, 0, 0, [], 1)
