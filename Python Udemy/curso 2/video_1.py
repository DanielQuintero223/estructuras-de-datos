# sentencia match

numero = 3

match numero:
    case 1:
        print("Es 1")
    case 2:
        print("Es 2")
    case 3:
        print("Es 3")
    case _:
        print("No es ni 1 ni 2 ni 3")


# ejercicio

numero = int(input("Introduce un número: "))

match numero:
    case 0:
        print("No sirve ya que es 0 ")
    case numero if numero % 2 == 0:
        print("Es par")
    case numero if numero % 2 != 0:
        print("Es impar")


# ejercicio tarea 2

numero2 = int(input("Introduce un número: "))

match numero2:
    case numero2 if numero2 < 0:
        print("Pertenece al Rango 1")
    case numero2 if numero2 > 0 and numero2 < 10:
        print("Pertenece al Rango 2")
    case numero2 if numero2 >= 10:
        print("Pertence al Rango 3")
