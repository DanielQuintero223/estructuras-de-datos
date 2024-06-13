import networkx as nx
import matplotlib.pyplot as plt

class ArbolNoDirigidoCompleto:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, nombre, peso, dinero):
        self.grafo.add_node(nombre, peso=peso, dinero=dinero)

    def generar_conexiones_completas(self):
        nodos = list(self.grafo.nodes)
        for i in range(len(nodos)):
            for j in range(i + 1, len(nodos)):
                nodo1 = nodos[i]
                nodo2 = nodos[j]
                peso_nodo1 = self.grafo.nodes[nodo1]['peso']
                peso_nodo2 = self.grafo.nodes[nodo2]['peso']
                dinero_nodo1 = self.grafo.nodes[nodo1]['dinero']
                dinero_nodo2 = self.grafo.nodes[nodo2]['dinero']
                self.grafo.add_edge(nodo1, nodo2, weight=peso_nodo1 + peso_nodo2, money=dinero_nodo1 + dinero_nodo2)

    def obtener_peso_nodo(self, nombre):
        if nombre in self.grafo.nodes:
            return self.grafo.nodes[nombre]['peso']
        else:
            return None

    def obtener_dinero_nodo(self, nombre):
        if nombre in self.grafo.nodes:
            return self.grafo.nodes[nombre]['dinero']
        else:
            return None
        
    def mostrar_nodo(self, nombre):
        if nombre in self.grafo.nodes:
            nodo_info = self.grafo.nodes[nombre]
            return f"Nombre: {nombre}, Peso: {nodo_info['peso']}, Dinero: {nodo_info['dinero']}"
        else:
            return None

    def graficar(self):
        pos = nx.spring_layout(self.grafo)
        nx.draw(self.grafo, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=12, font_weight="bold")
        labels = nx.get_edge_attributes(self.grafo, "weight")
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        nx.draw_networkx_edges(self.grafo, pos, width=1.0, alpha=0.5) # Dibuja las aristas
        plt.title("Árbol No Dirigido Completo")
        plt.show()

    # Getters y Setters
    def get_peso(self, nombre):
        return self.grafo.nodes[nombre]['peso'] if nombre in self.grafo.nodes else None

    def set_peso(self, nombre, peso):
        if nombre in self.grafo.nodes:
            self.grafo.nodes[nombre]['peso'] = peso

    def get_dinero(self, nombre):
        return self.grafo.nodes[nombre]['dinero'] if nombre in self.grafo.nodes else None

    def set_dinero(self, nombre, dinero):
        if nombre in self.grafo.nodes:
            self.grafo.nodes[nombre]['dinero'] = dinero

# # Ejemplo de uso
# arbol = ArbolNoDirigidoCompleto()
# arbol.agregar_nodo("punto1", 10, 100)
# arbol.agregar_nodo("punto2", 20, 200)
# arbol.agregar_nodo("punto3", 30, 300)
# arbol.agregar_nodo("punto4", 40, 400)
# arbol.agregar_nodo("punto5", 50, 500)

# arbol.generar_conexiones_completas()

# # Usando getters y setters
# peso_nodo_1 = arbol.get_peso("punto1")
# dinero_nodo_3 = arbol.get_dinero("punto3")
# print(f"Peso del nodo punto1: {peso_nodo_1}")
# print(f"Dinero del nodo punto3: {dinero_nodo_3}")

# arbol.set_peso("punto1", 10)
# arbol.set_dinero("punto3", 350)
# print(f"Nuevo peso del nodo punto1: {arbol.get_peso("punto1")}")
# print("el nuevo dinero del nodo punto 3 es: ", arbol.get_dinero("punto3"))

# arbol.graficar()
