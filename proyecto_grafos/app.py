import tkinter as tk
from tkinter import ttk, messagebox
import centro_operacion as almacen
import banco
import punto_recoleccion as punto
import vehiculos
import ladrones
import arbol_ciudad as ciudad

# Crear las instancias iniciales
banco_principal = banco.banco(0)
centro_principal = almacen.centro_operacion(0, 0, 0, 0, 0)
ladrones_principal = ladrones.ladrones(0, 0)
arbol_principal = ciudad.ArbolNoDirigidoCompleto()
vehiculos_policiales = []


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulación de Operaciones")
        self.geometry("600x800")

        # Input de 3 puntos diferentes de recolección
        self.create_collection_points_input()

        # Input de dinero en el banco
        self.create_bank_input()

        # Input de dinero a recolectar en los 3 puntos
        self.create_collection_money_input()
        
        # Input de dinero en el centro principal
        self.create_money_centro_principal_input()
        
        # Input de límite de dinero en el centro principal
        self.create_limit_centro_principal_input()

        # Selección de tipos de vehículos
        self.create_vehicle_selection()

        # Input de escudo y ataque de los ladrones
        self.create_ladrones_input()

        # Botón para enfrentar ladrones y vehículos policiales
        self.create_fight_button()

        # Botón para iniciar la simulación
        self.create_simulation_button()

        # Botón para agregar puntos de recolección, centro principal y banco principal al árbol
        self.create_city_button()
        
        # Botón para mostrar los vehículos disponibles
        self.create_show_vehicles_button()
        
    def create_collection_points_input(self):
        frame = ttk.LabelFrame(self, text="Puntos de Recolección")
        frame.pack(padx=10, pady=10, fill="x")

        self.puntos_entries = []
        self.dinero_entries = []
        self.nombre_entries = []
        for i in range(3):
            subframe = ttk.Frame(frame)
            subframe.pack(fill="x", pady=5)

            label = f"Punto de Recolección {i + 1}:"
            ttk.Label(subframe, text=label).pack(side="left")

            ttk.Label(subframe, text="Nombre:").pack(side="left", padx=(20, 5))
            nombre_entry = ttk.Entry(subframe)
            nombre_entry.pack(side="left", padx=5)
            self.nombre_entries.append(nombre_entry)

            ttk.Label(subframe, text="Dinero:").pack(side="left", padx=(20, 5))
            dinero_entry = ttk.Entry(subframe)
            dinero_entry.pack(side="left", padx=5)
            self.dinero_entries.append(dinero_entry)

    def create_bank_input(self):
        frame = ttk.LabelFrame(self, text="Banco")
        frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame, text="Dinero en el Banco:").pack(side="left")
        self.banco_entry = ttk.Entry(frame)
        self.banco_entry.pack(side="left", padx=5)

    def create_collection_money_input(self):
        frame = ttk.LabelFrame(self, text="Dinero a Recolectar")
        frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame, text="Dinero a Recolectar (dividido en 3 puntos):").pack(side="left")
        self.recoleccion_entry = ttk.Entry(frame)
        self.recoleccion_entry.pack(side="left", padx=5)
   
    def create_money_centro_principal_input(self):
        frame = ttk.LabelFrame(self, text="Dinero en el Centro Principal")
        frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame, text="Dinero en el Centro Principal:").pack(side="left")
        self.centro_principal_entry = ttk.Entry(frame)
        self.centro_principal_entry.pack(side="left", padx=5)
        
    def create_limit_centro_principal_input(self):
        frame = ttk.LabelFrame(self, text="Límite de Dinero en el Centro Principal")
        frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame, text="Límite de Dinero:").pack(side="left")
        self.centro_principal_limit_entry = ttk.Entry(frame)
        self.centro_principal_limit_entry.pack(side="left", padx=5)

    def create_vehicle_selection(self):
        frame = ttk.LabelFrame(self, text="Seleccionar Vehículos")
        frame.pack(padx=10, pady=10, fill="x")

        self.vehicle_type = tk.StringVar()
        self.vehicle_type.set("Moto")

        for vehicle in ["Moto", "Camioneta", "Furgoneta"]:
            ttk.Radiobutton(frame, text=vehicle, variable=self.vehicle_type, value=vehicle).pack(side="left")

        ttk.Button(frame, text="Agregar Vehículo", command=self.add_vehicle).pack(side="left", padx=5)

    def create_ladrones_input(self):
        frame = ttk.LabelFrame(self, text="Ladrones")
        frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame, text="Escudo de los Ladrones:").pack(side="left", padx=(20, 5))
        self.ladrones_escudo_entry = ttk.Entry(frame)
        self.ladrones_escudo_entry.pack(side="left", padx=5)

        ttk.Label(frame, text="Ataque de los Ladrones:").pack(side="left", padx=(20, 5))
        self.ladrones_ataque_entry = ttk.Entry(frame)
        self.ladrones_ataque_entry.pack(side="left", padx=5)

    def create_fight_button(self):
        ttk.Button(self, text="Enfrentar Ladrones y Vehículos Policiales", command=self.fight).pack(padx=10, pady=10)

    def create_simulation_button(self):
        ttk.Button(self, text="Iniciar Simulación", command=self.simulate).pack(padx=10, pady=10)

    def create_city_button(self):
        ttk.Button(self, text="Ciudad", command=self.show_city).pack(padx=10, pady=10)

    def create_show_vehicles_button(self):
        ttk.Button(self, text="Mostrar Vehículos Disponibles", command=self.mostrar_vehiculos).pack(padx=10, pady=10)

    def add_vehicle(self):
        vehicle = self.vehicle_type.get()
        if vehicle == "Moto":
            vehiculos_policiales.append(vehiculos.vehiculo("Moto",40, 50,30,0,0,0))
        if vehicle == "Camioneta":
            vehiculos_policiales.append(vehiculos.vehiculo("Camioneta",30, 40,20,4,0,4))
        if vehicle == "Furgoneta":
            vehiculos_policiales.append(vehiculos.vehiculo("Furgoneta",20, 30,10,2,0,8))
        print(f"Vehículo agregado: {vehicle}")

    def fight(self):
        try:
            escudo_ladrones = int(self.ladrones_escudo_entry.get())
            ataque_ladrones = int(self.ladrones_ataque_entry.get())

            # Actualizar los valores de los ladrones
            ladrones_principal.set_escudo(escudo_ladrones)
            ladrones_principal.set_ataque(ataque_ladrones)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos para el escudo y ataque de los ladrones.")
            return

        # Lógica para enfrentar ladrones y vehículos policiales
        ataque_total_vehiculos = sum([v.get_ataque() for v in vehiculos_policiales])
        escudo_total_vehiculos = sum([v.get_escudo() for v in vehiculos_policiales])

        puntos_vehiculos = 0
        puntos_ladrones = 0

        if ataque_total_vehiculos > escudo_ladrones:
            puntos_vehiculos += 1
        else:
            puntos_ladrones += 1

        if escudo_total_vehiculos > ataque_ladrones:
            puntos_vehiculos += 1
        else:
            puntos_ladrones += 1

        if puntos_vehiculos > puntos_ladrones:
            messagebox.showinfo("Resultado del Enfrentamiento", "¡Los vehículos policiales han ganado el enfrentamiento!")
            return True
        else:
            messagebox.showinfo("Resultado del Enfrentamiento", "¡Los ladrones han ganado el enfrentamiento!")
            return False

    def show_city(self):
        try:
            # Obtener los valores de dinero ingresados para los puntos de recolección
            nombre_punto_1 = self.nombre_entries[0].get()
            dinero_punto_1 = float(self.dinero_entries[0].get())
            nombre_punto_2 = self.nombre_entries[1].get()
            dinero_punto_2 = float(self.dinero_entries[1].get())
            nombre_punto_3 = self.nombre_entries[2].get()
            dinero_punto_3 = float(self.dinero_entries[2].get())
            
            
            # obtener el limite de dinero en el centro principal
            centro_principal.set_limite_dinero(float(self.centro_principal_limit_entry.get()))
            centro_principal.set_dinero_guardado(float(self.centro_principal_entry.get()))
            banco_principal.set_dinero_guardado(float(self.banco_entry.get()))


            # Agregar nodos al arbol_principal
            arbol_principal.agregar_nodo("centro principal ", 10, centro_principal.dinero_guardado)
            arbol_principal.agregar_nodo(nombre_punto_1, 15,dinero_punto_1)
            arbol_principal.agregar_nodo(nombre_punto_2, 15,dinero_punto_2)
            arbol_principal.agregar_nodo(nombre_punto_3, 15,dinero_punto_3)
            arbol_principal.agregar_nodo("punto3 apoyo",15, 10)
            arbol_principal.agregar_nodo("banco principal",15, banco_principal.dinero_guardado)
            
            arbol_principal.generar_conexiones_completas()
            arbol_principal.graficar()
            
            messagebox.showinfo("Éxito", "Los nodos se han agregado correctamente al árbol.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos para el dinero en los puntos de recolección.")
            return

    def mostrar_vehiculos(self):
        vehicle_info = {"Moto": 0, "Camioneta": 0, "Furgoneta": 0}
        for vehiculo in vehiculos_policiales:
            vehicle_info[vehiculo.get_tipo_vehiculo()] += 1
        messagebox.showinfo("Vehículos Disponibles", f"Vehículos disponibles:\n{vehicle_info}")

    def simulate(self):
        # se inicializa la variable recoleccion
        recoleccion = 0
        recoleccion_por_nodo = 0
        
        if not vehiculos_policiales:
            messagebox.showerror("Error", "No hay vehículos disponibles.")
            return
        
        if centro_principal.get_dinero_guardado() > centro_principal.get_limite_dinero():
            messagebox.showerror("Error", "El centro principal ha alcanzado su límite de dinero.")
            return
        
        #inicializa el ataque de los ladrones
        pelea = self.fight()
        
        if pelea == False:
            messagebox.showerror("Los ladrones han ganado el enfrentamiento. por ende no puede continuar la simulacion ")
            return
        

        recorrido = ["centro principal ", self.nombre_entries[0].get(), self.nombre_entries[1].get(), self.nombre_entries[2].get(),"punto3 apoyo", "banco principal"]
        dinero_a_recolectar = float(self.recoleccion_entry.get())
        dinero_recolecta_static = dinero_a_recolectar

        for vehicle in vehiculos_policiales:
            for index, nodo_actual in enumerate(recorrido[:-1]):
                siguiente_nodo = recorrido[index + 1]
                    
                
                # Si llega al banco principal, depositar el dinero
                if siguiente_nodo == "banco principal":
                    banco_principal.set_dinero_guardado(banco_principal.get_dinero_guardado() + recoleccion)
                    dinero_centro_principal = arbol_principal.obtener_dinero_nodo("centro principal ")
                    if dinero_a_recolectar <= 0:
                        messagebox.showinfo("Simulación completada", "Se ha recolectado todo el dinero.")
                        messagebox.showinfo("Resultados de la simulacion", f"El banco principal ahora tiene {banco_principal.get_dinero_guardado()} Dolares.")
                        messagebox.showinfo("Resultados de la simulacion", f"El centro principal ahora tiene {dinero_centro_principal} Dolares.")
                        for i, nombre in enumerate([self.nombre_entries[0].get(), self.nombre_entries[1].get(), self.nombre_entries[2].get()]):
                            dinero_punto = arbol_principal.obtener_dinero_nodo(nombre)
                            messagebox.showinfo("Resultados de la simulacion", f"El {nombre} ahora tiene {dinero_punto} Dolares.")
                        return
                            
                    else:
                        messagebox.showwarning("Simulación incompleta", f"Faltan por recolectar {dinero_a_recolectar} unidades de dinero.")
                        messagebox.showinfo("Resultados de la simulacion", f"El banco principal ahora tiene {banco_principal.get_dinero_guardado()} Dolares.")
                        messagebox.showinfo("Resultados de la simulacion", f"El centro principal ahora tiene {dinero_centro_principal} Dolares.")
                        for i, nombre in enumerate([self.nombre_entries[0].get(), self.nombre_entries[1].get(), self.nombre_entries[2].get()]):
                            dinero_punto = arbol_principal.obtener_dinero_nodo(nombre)
                            messagebox.showinfo("Resultados de la simulacion", f"El {nombre} ahora tiene {dinero_punto} Dolares.")
                else:
                    peso_actual = arbol_principal.obtener_peso_nodo(nodo_actual)
                    peso_siguiente = arbol_principal.obtener_peso_nodo(siguiente_nodo)
                    arista_peso = peso_actual + peso_siguiente
                    if vehicle.get_peso() > arista_peso:
                         messagebox.showerror("Error", f"El puente entre {nodo_actual} y {siguiente_nodo} colapsará.")
                         return
                           
                           
                    dinero_nodo = arbol_principal.obtener_dinero_nodo(nodo_actual)  
                    if vehicle.get_tipo_vehiculo() == "Furgoneta":
                        if self.convert_money_to_weight(dinero_nodo) < vehicle.get_peso():
                            vehicle.set_dinero_recogido(dinero_nodo)
                            vehicle.set_peso(vehicle.get_peso() - self.convert_money_to_weight(dinero_nodo))
                            recoleccion += dinero_nodo
                            recoleccion_por_nodo = dinero_nodo
                    elif vehicle.get_tipo_vehiculo() == "Camioneta":
                        if self.convert_money_to_weight(dinero_nodo) < vehicle.get_peso():
                            vehicle.set_dinero_recogido(dinero_nodo)
                            vehicle.set_peso(vehicle.get_peso() - self.convert_money_to_weight(dinero_nodo))
                            recoleccion += dinero_nodo
                            recoleccion_por_nodo = dinero_nodo
                    elif vehicle.get_tipo_vehiculo() == "Moto":
                        messagebox.showinfo("la moto no puede llevar dinero")
                        
                                                                                      
                    vehicle.set_dinero_recogido(vehicle.get_dinero_recogido() + recoleccion)
                    if recoleccion > dinero_recolecta_static:
                        arbol_principal.set_dinero(nodo_actual, dinero_nodo - (recoleccion - dinero_recolecta_static))
                        diferencia = recoleccion - dinero_recolecta_static
                        recoleccion = recoleccion - diferencia
                        dinero_a_recolectar -= recoleccion
                        recoleccion_por_nodo = 0
                    else:
                        arbol_principal.set_dinero(nodo_actual, dinero_nodo - recoleccion_por_nodo)
                        dinero_a_recolectar -= recoleccion
                        recoleccion_por_nodo = 0
                    
                    
                                
    @staticmethod
    def convert_money_to_weight(money):
        return money / 10000  # 1 tonelada por cada 10,000 unidades de dinero


if __name__ == "__main__":
    app = App()
    app.mainloop()
