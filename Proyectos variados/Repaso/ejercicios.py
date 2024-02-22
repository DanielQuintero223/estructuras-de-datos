
def OperacionesAritmeticas():

    # Operaciones aritmeticas

    # SUMA
    v1 = 15
    v2 = 145

    sum = v1+v2

    print("La suma de dos variales es = {}".format(sum))

    #  RESTA

    res = v1-v2

    print("La resta de dos variables es = ", res)

    #  Multiplicacion

    mul = v1*v2

    print("La multiplicacion de dos variables es = ", mul)

    #  Division

    div = v1/v2

    print("La division entre dos variables es = ", div)

    # Residuo

    residuo = v1 % v2

    print("El residuo de dos variables es = ", residuo)


def Condicionales():

    # Numero positivo
    va1 = int(input("Ingrese el numero de la variables 1 = "))
    va2 = int(input("Ingrese el numero de la variables 2 = "))

    if va1 >= 1:
        print("La variable 1 es positiva  --  Valor de la variable = ", va1)

    if va1 <= -1:
        print("La variable 1 es Negativa  --  Valor de la variable = ", va1)

    if va1 == 0:
        print("la variable 1 es CERO -- Valor de la variable  = ", va1)

    if va2 >= 1:
        print("La variable 2 es positiva  --  Valor de la variable = ", va2)
    if va2 <= -1:
        print("La variable 2 es Negativa  --  Valor de la variable = ", va2)

    if va2 == 0:
        print("la variable 2 es CERO -- Valor de la variable  = ", va2)

    # Numero Par o Impar

    if va1 % 2 == 0:
        print("El numero de la variable 1 es par ")

    else:
        print("El numero de la variable 1 es impar ")

    if va2 % 2 == 0:
        print("El numero de la variable 2 es par ")

    else:
        print("El numero de la variable 2 es impar ")

    # Año bisiesto


def añobisiesto():

    año = int(input('Introduce un año: '))

    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print('El año es bisiesto')
            else:
                print('El año no es bisiesto')
        else:
            print('El año es bisiesto.')
    else:
        print('El año no es bisiesto.')


def mayorque():

    mayor = 0
    var1 = int(input(" Ingrese el valor = "))
    var2 = int(input(" Ingrese el valor = "))
    var3 = int(input(" Ingrese el valor = "))
    lista = [var1, var2, var3]

    for x in lista:

        if x > mayor:
            mayor = x

    print("El mayor de los tres numeros es = ", mayor)


def primo():

    var1 = int(input("ingrese el numero a verificar si es numero primo = "))

    if (var1 % var1 == 0) and (var1 % 1 == 0) and (var1 % 2 >= 1):
        print("Es primo")
    else:
        print("No es primo")


def imprimir_naturales(n):

    for i in range(1, n+1):
        print(i)


def sumar_naturales(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    print("La suma de los naturales es {}".format(suma))


def imprimir_primeros_pares(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, " es par")


def while_imprimir_impares(n):
    i = 1
    while i <= n:
        print(2+i-1)
        i += 1


def calcular_factorial(n):
    fac = 1
    i = 1
    while (i <= n):
        fac *= i
        i += 1
    return fac


def sumar_elementos_vector(vec):
    suma = 0
    for i in range(len(vec)):
        suma += vec[i]
    return suma


def producto_punto(vec1, vec2):
    total = 0

    for i in range(len(vec1)):
        total += vec1[i]*vec2[i]
    return total


def existe_n(vec, n):
    return n in vec


def ordenar_vector(vec):
    for i in range(len(vec)-1):
        for j in range(1, len(vec)):
            if vec[i] > vec[j]:
                tmp = vec[i]
                vec[i] = vec[j]
                vec[j] = tmp
    print(vec)


def media_aritmetica(vec):
    media = 0
    for i in vec:
        media += i
    return media/len(vec)


def sumar_matrices(m1, m2):
    for f in range(len(m1)):
        for c in range(len(m1[f])):
            print(m1[f][c]+m2[f][c])


def restar_matrices(m1, m2):
    for f in range(len(m1)):
        for c in range(len(m1[f])):
            print(m1[f][c]-m2[f][c])


def multiplicar_matriz_x_escalar(m1, e1):
    for f in range(len(m1)):
        for c in range(len(m1[f])):
            print(m1[f][c]*e1)


def transpuesta(m1):
    trans = []

    for f in range(len(m1)):
        for c in range(len(m1[f])):
            trans.append(m1[c][f])

    return trans


def Mostrar(m1):
    print("La matriz es la siguiente:")
    for i in m1:
        print(i, end=' ')
        print()


mt1 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mt2 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]


e1 = 5

# return sorted(vector) -- ordena automaticamente

# OperacionesAritmeticas()
# Condicionales()
# añobisiesto()
# mayorque()
# primo()
# imprimir_naturales(20)
# sumar_naturales(10)
# imprimir_primeros_pares(10)
# sumar_elementos_vector([5,9,2,4,12,122])
# multiplicar_matriz_x_escalar(mt1, e1)
transpuesta1 = transpuesta(mt1)
Mostrar(transpuesta1)
