frutas = ["manzana", "mango", "pera", "fresa", "kiwi", "naranja"]
contador = 0

# bucle for
for fruta in frutas:
    contador += 1
    print(f"{contador}.- {fruta}")


print("\n")  # salto de linea

# cuadrado de los numero

numero = [1, 2, 3, 4, 5]

for numeros in numero:
    cuadrado = numeros ** 2
    print(f"El cuadrado de {numeros} es {cuadrado}")


print("\n")  # salto de linea

numeros = [1, 2, 3, 4, 5]
suma = 0

for numero in numeros:
    suma += numero

print(suma / len(numeros))  # promedio de los numeros
