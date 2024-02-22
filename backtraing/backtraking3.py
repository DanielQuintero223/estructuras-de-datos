def intercambiar(lista, paso=0):
    # Base case: si hemos completado todos los pasos, imprimimos la lista resultante
    if paso == len(lista):
        print(lista)
        return

    # Recorremos todas las posiciones de la lista
    for i in range(len(lista)):
        # Si la posición i está vacía (valor None), continuamos
        if lista[i] is None:
            # Si estamos en las primeras 3 posiciones, intentamos intercambiar con las últimas 3 posiciones
            if paso < 3:
                # Intentamos intercambiar con las últimas 3 posiciones
                for j in range(4, 7):
                    # Realizamos el intercambio
                    lista[i], lista[j] = lista[j], lista[i]
                    # Llamamos recursivamente a la función para el siguiente paso
                    intercambiar(lista, paso + 1)
                    # Deshacemos el intercambio para probar con el siguiente valor
                    lista[i], lista[j] = None, lista[i]
            # Si estamos en las últimas 3 posiciones, intentamos intercambiar con las primeras 3 posiciones
            else:
                # Intentamos intercambiar con las primeras 3 posiciones
                for j in range(3):
                    # Realizamos el intercambio
                    lista[i], lista[j] = lista[j], lista[i]
                    # Llamamos recursivamente a la función para el siguiente paso
                    intercambiar(lista, paso + 1)
                    # Deshacemos el intercambio para probar con el siguiente valor
                    lista[i], lista[j] = None, lista[i]


# Creamos la lista inicial con los valores dados
lista = [1, 2, 3, None, 4, 5, 6]

# Llamamos a la función para iniciar el proceso de backtracking
intercambiar(lista)
