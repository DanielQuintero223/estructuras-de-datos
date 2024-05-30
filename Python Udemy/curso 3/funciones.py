def saludar(nombre):
    print(f"Hola {nombre}!")


saludar("DANIEL")


# ejercicio

def calculadora(numero_1, numero_2, operacion):
    if operacion == "+":
        return numero_1 + numero_2
    if operacion == "-":
        return numero_1 - numero_2
    if operacion == "*":
        return numero_1 * numero_2
    if operacion == "/":
        return numero_1 / numero_2
    else:
        return "Operación no válida"


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
op = input("Introduce la operación a realizar: ")

print(calculadora(num1, num2, op))
