import modulo_personalizado

num = int(input("Introduce un número: "))

operacion = modulo_personalizado.es_par(num)

if operacion == True:
    print("El número es par")
else:
    print("El número es impar")
