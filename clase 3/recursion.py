###

def suma_recursiva(n, i, suma):
    if i == n:
        return suma
    else:
        return suma_recursiva(n, i+1, suma+i)


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


# funcion que retorne la cantidad de digitos de un numero entero positivo
def cantidad_digitos(n):
    if n < 10:
        return 1
    else:
        return cantidad_digitos(n//10)+1

# funcion recursiva que dado un numero y 1 digito retorne la cantidad de veces que aparece el digito en el numero


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


print(contar_digito(100, 0))
