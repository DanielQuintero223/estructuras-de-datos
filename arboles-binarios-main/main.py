from Modelos.ArbolBST import ArbolBST


# Ejemplo de uso
arbol = ArbolBST()
arbol.insertar(20)
arbol.insertar(15)
arbol.insertar(33)
arbol.insertar(10)
arbol.insertar(18)
arbol.insertar(25)
arbol.insertar(50)
arbol.insertar(5)


# print(arbol.buscar(5))  # Output: True
# print(arbol.buscar(7))  # Output: False

arbol.postorden()
# arbol.imprimir_arbol()


# Dibujar el árbol
arbol.dibujar()

print("")
print("---------------------")
print("")

# ejercicio #01 - 1 punto


def indicar_si_es_ordenado_de_busqueda(nodo):
    if nodo is None:  # corregir si es hoja
        return print("Es un árbol de búsqueda")
    if nodo.izquierda is not None:
        if nodo.izquierda.valor > nodo.valor:
            return False
    if nodo.derecha is not None:
        if nodo.derecha.valor < nodo.valor:
            return False
    return True and indicar_si_es_ordenado_de_busqueda(nodo.izquierda) and indicar_si_es_ordenado_de_busqueda(nodo.derecha)


indicar_si_es_ordenado_de_busqueda(arbol.raiz)

print("")
print("---------------------")
print("")

# ejercicio #02 - 8 punto


def mostrar_hojas(nodo):
    if nodo.izquierda is None and nodo.derecha is None:
        print(nodo.izquierda, nodo.derecha)
    else:
        return mostrar_hojas(nodo.izquierda) and mostrar_hojas(nodo.derecha)


mostrar_hojas(arbol.raiz)
