from collections import defaultdict
import tkinter as tk
from tkinter import ttk, messagebox
import random


class Equipo:
    def __init__(self, nombre, resistencia, fuerza, velocidad, precision):
        self.nombre = nombre
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.precision = precision
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.puntos = 0


class Nodo:
    def __init__(self, equipo):
        self.equipo = equipo
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar_equipo(self, equipo):
        if self.raiz is None:
            self.raiz = Nodo(equipo)
        else:
            self._agregar_equipo_recursivo(self.raiz, equipo)

    def _agregar_equipo_recursivo(self, nodo, equipo):
        if nodo.equipo.puntos < equipo.puntos:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(equipo)
            else:
                self._agregar_equipo_recursivo(nodo.izquierda, equipo)
        elif nodo.equipo.puntos > equipo.puntos:
            if nodo.derecha is None:
                nodo.derecha = Nodo(equipo)
            else:
                self._agregar_equipo_recursivo(nodo.derecha, equipo)


class VentanaFaseFinal:
    def __init__(self, root, equipos_fase_final, partidos_fase_final, app):
        self.root = root
        self.root.title("Fase Final del Torneo")
        self.equipos_fase_final = equipos_fase_final
        self.partidos_fase_final = partidos_fase_final
        self.app = app

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.enfrentamientos_text = tk.Text(self.frame, width=50, height=10)
        self.enfrentamientos_text.grid(row=0, column=0, padx=5, pady=5)

        self.resultado_label = ttk.Label(
            self.frame, text="Ganador del Torneo:")
        self.resultado_label.grid(row=1, column=0, padx=5, pady=5)

        self.btn_cerrar = ttk.Button(
            self.frame, text="Cerrar", command=self.cerrar_ventana)
        self.btn_cerrar.grid(row=2, column=0, padx=5, pady=5)

        self.enfrentar_equipos()

    def enfrentar_equipos(self):
        ganador = None
        enfrentamientos = ""
        for partido in self.partidos_fase_final:
            equipo1 = partido[0]
            equipo2 = partido[1]
            equipo_ganador, _ = self.app.simular_partido(
                equipo1, equipo2, self.app.criterio_combobox.get())
            if equipo_ganador:
                enfrentamientos += f"{equipo1.nombre} vs {equipo2.nombre}: Ganador - {equipo_ganador.nombre}\n"
                if ganador is None or equipo_ganador.puntos > ganador.puntos:
                    ganador = equipo_ganador

        self.enfrentamientos_text.insert(tk.END, enfrentamientos)
        if ganador:
            self.resultado_label.config(
                text=f"Ganador del Torneo: {ganador.nombre}")
        else:
            self.resultado_label.config(text="No hay un ganador")

    def cerrar_ventana(self):
        self.root.destroy()


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Torneo de Fútbol")

        self.equipos = {'A': [], 'B': [], 'C': [], 'D': []}

        self.create_equipo_widgets()
        self.create_criterio_widgets()
        self.create_simular_fecha_button()
        self.create_grupos_table()
        self.create_resultados_jornadas_widgets()
        self.fase_final = ArbolBinario()
        self.create_fase_final_button()

    def create_equipo_widgets(self):
        equipo_frame = ttk.Frame(self.root)
        equipo_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(equipo_frame, text="Nombre del Equipo:").grid(
            row=0, column=0, padx=5, pady=5)
        self.equipo_entry = ttk.Entry(equipo_frame)
        self.equipo_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(equipo_frame, text="Resistencia (1-10):").grid(row=1,
                                                                 column=0, padx=5, pady=5)
        self.resistencia_entry = ttk.Entry(equipo_frame)
        self.resistencia_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(equipo_frame, text="Fuerza (1-10):").grid(row=2,
                                                            column=0, padx=5, pady=5)
        self.fuerza_entry = ttk.Entry(equipo_frame)
        self.fuerza_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(equipo_frame, text="Velocidad (1-10):").grid(row=3,
                                                               column=0, padx=5, pady=5)
        self.velocidad_entry = ttk.Entry(equipo_frame)
        self.velocidad_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(equipo_frame, text="Precisión:").grid(
            row=4, column=0, padx=5, pady=5)
        self.precision_combobox = ttk.Combobox(
            equipo_frame, values=["bajo", "medio", "alto"], state="readonly")
        self.precision_combobox.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(equipo_frame, text="Grupo:").grid(
            row=5, column=0, padx=5, pady=5)
        self.grupo_combobox = ttk.Combobox(
            equipo_frame, values=["A", "B", "C", "D"], state="readonly")
        self.grupo_combobox.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(equipo_frame, text="Agregar Equipo", command=self.add_equipo).grid(
            row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_equipo(self):
        grupo = self.grupo_combobox.get()
        if len(self.equipos[grupo]) >= 4:
            messagebox.showwarning(
                "Alerta", f"Ya se han agregado 4 equipos al Grupo {grupo}. No se pueden agregar más.")
            return

        nombre = self.equipo_entry.get()
        resistencia = int(self.resistencia_entry.get())
        fuerza = int(self.fuerza_entry.get())
        velocidad = int(self.velocidad_entry.get())
        precision = self.precision_combobox.get()

        equipo = Equipo(nombre, resistencia, fuerza, velocidad, precision)
        self.equipos[grupo].append(equipo)

        self.equipo_entry.delete(0, tk.END)
        self.resistencia_entry.delete(0, tk.END)
        self.fuerza_entry.delete(0, tk.END)
        self.velocidad_entry.delete(0, tk.END)

        # Actualizar la tabla del grupo
        self.update_grupo_table(grupo)

    def update_grupo_table(self, grupo):
        # limpiar la tabla del grupo
        for widget in self.grupos_notebook.winfo_children():
            widget.destroy()

        # Crear y actualizar la tabla del grupo
        tab = ttk.Frame(self.grupos_notebook)
        self.create_grupo_table(tab, grupo)
        self.grupos_notebook.add(tab, text=f"Grupo {grupo}")

    def create_criterio_widgets(self):
        criterio_frame = ttk.Frame(self.root)
        criterio_frame.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(criterio_frame, text="Criterio:").grid(
            row=0, column=0, padx=5, pady=5)
        self.criterio_combobox = ttk.Combobox(
            criterio_frame, values=["fuerza", "velocidad", "precision"], state="readonly")
        self.criterio_combobox.grid(row=0, column=1, padx=5, pady=5)

    def create_simular_fecha_button(self):
        simular_frame = ttk.Frame(self.root)
        simular_frame.grid(row=0, column=2, padx=10, pady=10)

        ttk.Button(simular_frame, text="Simular Fecha", command=self.simular_fecha).grid(
            row=0, column=0, padx=5, pady=5)

    def simular_partido(self, equipo1, equipo2, criterio):
        if criterio == "resistencia":
            if equipo1.resistencia > equipo2.resistencia:
                return equipo1, equipo2
            elif equipo1.resistencia < equipo2.resistencia:
                return equipo2, equipo1
            else:
                if equipo1.fuerza > equipo2.fuerza:
                    return equipo1, equipo2
                elif equipo1.fuerza < equipo2.fuerza:
                    return equipo2, equipo1
                else:
                    return None, None

        elif criterio == "fuerza":
            if equipo1.fuerza > equipo2.fuerza:
                return equipo1, equipo2
            elif equipo1.fuerza < equipo2.fuerza:
                return equipo2, equipo1
            else:
                if equipo1.velocidad > equipo2.velocidad:
                    return equipo1, equipo2
                elif equipo1.velocidad < equipo2.velocidad:
                    return equipo2, equipo1
                else:
                    return None, None

        elif criterio == "velocidad":
            if equipo1.velocidad > equipo2.velocidad:
                return equipo1, equipo2
            elif equipo1.velocidad < equipo2.velocidad:
                return equipo2, equipo1
            else:
                if equipo1.precision == "alto":
                    return equipo1, equipo2
                elif equipo2.precision == "alto":
                    return equipo2, equipo1
                elif equipo1.precision == "medio":
                    return equipo1, equipo2
                elif equipo2.precision == "medio":
                    return equipo2, equipo1
                else:
                    return None, None

        elif criterio == "precision":
            if equipo1.precision == "alto" and equipo2.precision != "alto":
                return equipo1, equipo2
            elif equipo1.precision != "alto" and equipo2.precision == "alto":
                return equipo2, equipo1
            elif equipo1.precision == "alto" and equipo2.precision == "alto":
                if equipo1.resistencia > equipo2.resistencia:
                    return equipo1, equipo2
                elif equipo1.resistencia < equipo2.resistencia:
                    return equipo2, equipo1
                else:
                    return None, None
            else:
                if equipo1.resistencia > equipo2.resistencia:
                    return equipo1, equipo2
                elif equipo1.resistencia < equipo2.resistencia:
                    return equipo2, equipo1
                else:
                    return None, None

    def simular_fecha(self):
        criterio = self.criterio_combobox.get()
        for grupo, equipos in self.equipos.items():
            for i in range(len(equipos)):
                for j in range(i+1, len(equipos)):
                    equipo1 = equipos[i]
                    equipo2 = equipos[j]
                    equipo_ganador, equipo_perdedor = self.simular_partido(
                        equipo1, equipo2, criterio)
                    if equipo_ganador and equipo_perdedor:
                        equipo_ganador.partidos_jugados += 1
                        equipo_ganador.partidos_ganados += 1
                        equipo_perdedor.partidos_jugados += 1
                        equipo_perdedor.partidos_perdidos += 1
                        goles_ganador = random.randrange(1, 5, 1)
                        if goles_ganador == 1:
                            goles_perdedor = 0
                        else:
                            goles_perdedor = random.randrange(
                                0, goles_ganador-1, 1)
                        equipo_ganador.goles_a_favor += goles_ganador
                        equipo_ganador.goles_en_contra += goles_perdedor
                        equipo_perdedor.goles_a_favor += goles_perdedor
                        equipo_perdedor.goles_en_contra += goles_ganador
                        equipo_ganador.puntos += 3
                        equipo_perdedor.puntos += 0
                    else:
                        equipo1.partidos_jugados += 1
                        equipo2.partidos_jugados += 1
                        equipo1.partidos_empatados += 1
                        equipo2.partidos_empatados += 1
                        goles = random.randrange(1, 3, 1)
                        equipo1.goles_a_favor += goles
                        equipo1.goles_en_contra += goles
                        equipo2.goles_a_favor += goles
                        equipo2.goles_en_contra += goles
                        equipo1.puntos += 1
                        equipo2.puntos += 1

        # Actualizar la tabla de posiciones
        for grupo in ["A", "B", "C", "D"]:
            self.update_grupo_table(grupo)

        # Mostrar resultados de la fecha
        self.mostrar_resultados_fecha()

        mejores_equipos_por_grupo = self.obtener_mejores_equipos_por_grupo()
        for grupo, equipos in mejores_equipos_por_grupo.items():
            for equipo in equipos[:2]:
                self.fase_final.agregar_equipo(equipo)

    def create_grupos_table(self):
        grupo_frame = ttk.Frame(self.root)
        grupo_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.grupos_notebook = ttk.Notebook(grupo_frame)

        for grupo in ["A", "B", "C", "D"]:
            self.grupos_notebook.add(
                self.create_grupo_tab(grupo), text=f"Grupo {grupo}")

        self.grupos_notebook.grid(row=0, column=0, padx=5, pady=5)

    def create_grupo_tab(self, grupo):
        tab = ttk.Frame(self.grupos_notebook)
        self.create_grupo_table(tab, grupo)
        return tab

    def create_grupo_table(self, tab, grupo):
        treeview = ttk.Treeview(tab, columns=(
            "Equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "Pts"))
        treeview.heading("#0", text="Grupo")
        treeview.heading("Equipo", text="Equipo")
        treeview.heading("PJ", text="Partidos Jugados")
        treeview.heading("PG", text="Partidos Ganados")
        treeview.heading("PE", text="Partidos Empatados")
        treeview.heading("PP", text="Partidos Perdidos")
        treeview.heading("GF", text="Goles a Favor")
        treeview.heading("GC", text="Goles en Contra")
        treeview.heading("Pts", text="Puntos")

        equipos = sorted(
            self.equipos[grupo], key=lambda equipo: equipo.puntos, reverse=True)
        for equipo in equipos:
            treeview.insert("", "end", values=(equipo.nombre, equipo.partidos_jugados, equipo.partidos_ganados,
                            equipo.partidos_empatados, equipo.partidos_perdidos, equipo.goles_a_favor, equipo.goles_en_contra, equipo.puntos))

        treeview.pack()

    def create_resultados_jornadas_widgets(self):
        resultados_frame = ttk.Frame(self.root)
        resultados_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        ttk.Label(resultados_frame, text="Resultados de las Jornadas:").grid(
            row=0, column=0, padx=5, pady=5)

        self.resultados_text = tk.Text(resultados_frame, width=60, height=10)
        self.resultados_text.grid(row=1, column=0, padx=5, pady=5)

    def mostrar_resultados_fecha(self):
        self.resultados_text.delete("1.0", tk.END)
        self.resultados_text.insert(
            tk.END, "Resultados de las Jornadas:\n\n")
        for grupo, equipos in self.equipos.items():
            for i in range(len(equipos)):
                for j in range(i+1, len(equipos)):
                    equipo1 = equipos[i]
                    equipo2 = equipos[j]
                    resultado = f"{equipo1.nombre} {equipo1.goles_a_favor} - {equipo2.goles_a_favor} {equipo2.nombre}\n"
                    self.resultados_text.insert(tk.END, resultado)

    def obtener_mejores_equipos_por_grupo(self):
        mejores_equipos_por_grupo = defaultdict(list)
        for grupo, equipos in self.equipos.items():
            equipos_ordenados = sorted(
                equipos, key=lambda equipo: equipo.puntos, reverse=True)
            mejores_equipos_por_grupo[grupo] = equipos_ordenados[:2]
        return mejores_equipos_por_grupo

    def create_fase_final_button(self):
        fase_final_frame = ttk.Frame(self.root)
        fase_final_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        ttk.Button(fase_final_frame, text="Fase Final", command=self.mostrar_fase_final).grid(
            row=0, column=0, padx=5, pady=5)

    def fase_final_en_lista_inorden(self, nodo):
        if nodo is None:
            return []
        lista = []
        lista.extend(self.fase_final_en_lista_inorden(nodo.izquierda))
        lista.append(nodo)
        lista.extend(self.fase_final_en_lista_inorden(nodo.derecha))
        return lista

    def mostrar_fase_final(self):
        equipos_fase_final = []
        partidos_fase_final = []
        for nodo in self.fase_final_en_lista_inorden(self.fase_final.raiz):
            equipos_fase_final.append(nodo.equipo)

        # Generar todos los posibles enfrentamientos en la fase final
        for i in range(len(equipos_fase_final)):
            for j in range(i + 1, len(equipos_fase_final)):
                partido = (equipos_fase_final[i], equipos_fase_final[j])
                partidos_fase_final.append(partido)

        ventana_fase_final = tk.Toplevel(self.root)
        ventana_fase_final.geometry("400x300")
        VentanaFaseFinal(ventana_fase_final, equipos_fase_final,
                         partidos_fase_final, self)


root = tk.Tk()
app = App(root)
root.mainloop()
