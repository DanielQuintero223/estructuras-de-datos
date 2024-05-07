# ejercicios de manera recursiva

def cantidad_digitos(n):
    if n < 10:
        return 1
    else:
        return cantidad_digitos(n//10)+1

# conteo de cantidad de veces que aparece el digito


def contar_digito(n, d):
    if n < 10:
        if n == d:
            return 1
        else:
            return 0
    else:
        if n % 10 == d:
            return contar_digito(n//10, d) + 1
        else:
            return contar_digito(n//10, d)


# inverso


def inverso_lista(lista):
    if lista == []:
        inversa = lista
    else:
        inversa = [lista[-1]] + inverso_lista(lista[:-1])

    return inversa


# cantidad de pares de digitos

def pares_digitos(n, par):
    if n == 0:
        return 0
    else:
        d = n % 10
        if d % 2 == 0:
            par += +1
            return pares_digitos(n/10, par)
        else:
            return par


def suma_de_digitos(n, d):
    if n < 10:
        return n
    else:
        return n % 10 + suma_de_digitos(n//10, d)
