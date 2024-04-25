from Modelos.ArbolBST import ArbolBST
from Modelos.arbolesalv import ArbolAVL


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

arbol2 = ArbolBST()
arbol2.insertar(20)
arbol2.insertar(15)
arbol2.insertar(33)
arbol2.insertar(10)
arbol2.insertar(18)
arbol2.insertar(25)
arbol2.insertar(50)
arbol2.insertar(5)


# print(arbol.buscar(5))  # Output: True
# print(arbol.buscar(7))  # Output: False

arbol.postorden()
# arbol.imprimir_arbol()


# Dibujar el árbol
arbol.dibujar()
arbol2.dibujar()

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


print("")
print("---------------------")
print("")

# ejercicio #03 - 9 punto


def indicar_si_dos_arboles_son_iguales(Nodo1, Nodo2):
    if Nodo1 is None and Nodo2 is None:
        return True
    if Nodo1 is not None and Nodo2 is not None:
        if (Nodo1.valor == Nodo2.valor):
            return print("los arboles son iguales") and indicar_si_dos_arboles_son_iguales(Nodo1.izquierda, Nodo2.izquierda) and indicar_si_dos_arboles_son_iguales(Nodo1.derecha, Nodo2.derecha)
        else:
            print("Los árboles no son iguales")
            return False


indicar_si_dos_arboles_son_iguales(arbol.raiz, arbol2.raiz)


print("")
print("---------------------")
print("")

# ejercicio #04 - 15 punto


def cuantas_veces_se_encuentra_un_dato_especifico(nodo, valor):
    if nodo is None:
        return 0
    if nodo.valor == valor:
        return 1 + cuantas_veces_se_encuentra_un_dato_especifico(nodo.izquierda, valor) + cuantas_veces_se_encuentra_un_dato_especifico(nodo.derecha, valor)
    else:
        return cuantas_veces_se_encuentra_un_dato_especifico(nodo.izquierda, valor) + cuantas_veces_se_encuentra_un_dato_especifico(nodo.derecha, valor)


veces = cuantas_veces_se_encuentra_un_dato_especifico(arbol.raiz, 20)
print(veces)

print("")
print("---------------------")
print("")

# ejercicio #05 - 20 punto


def Dados_dos_nodos_intercambiar_sus_datos(nodo1, nodo2):
    if nodo1 is None and nodo2 is None:
        return
    if nodo1 is not None and nodo2 is not None:
        temporal = nodo1.valor
        nodo1.valor = nodo2.valor
        nodo2.valor = temporal
        return Dados_dos_nodos_intercambiar_sus_datos(nodo1.izquierda, nodo2.izquierda) and Dados_dos_nodos_intercambiar_sus_datos(nodo1.derecha, nodo2.derecha)
    # no se como mostrarlos en el arbol


Dados_dos_nodos_intercambiar_sus_datos(arbol.raiz, arbol2.raiz)

print("")
print("---------------------")
print("")
