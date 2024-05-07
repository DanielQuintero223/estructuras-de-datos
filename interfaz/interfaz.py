from tkinter import *
import random

raiz = Tk()  # Creamos la raíz de la interfaz

raiz.title("Interfaz gráfica con Python")  # Título de la ventana
raiz.geometry("800x600")  # Tamaño de la ventana
#  raiz.resizable(0, 0)  # No permitir redimensionar la ventana
# raiz.config(bg="white")  # Color de fondo de la ventana


primer_frame = Frame(raiz, width=800, height=200)  # Creamos un frame
# Empaquetamos el frame con el lado donde estara
# primer_frame.pack(side="left", anchor="n") # se usa para colocar el frame en x posicion
# el expand es para que se exopandan en toda la ventana
primer_frame.pack(fill="both",)
primer_frame.config(bg="gray")  # Color de fondo del frame
primer_frame.config(bd=35)  # Tamaño del borde en pixeles
primer_frame.config(relief="sunken")  # Tipo de borde
primer_frame.config(cursor="pirate")  # Tipo de cursor

# creacion de label en el frame - se usa para colocar texto y si le agregamos un entry se puede ingresar datos
milabel = Label(primer_frame, text="Hola Mundo", font=("Arial", 20))
milabel.place(x=100, y=100)


for i in range(10):
    goles_ganador = random.randrange(1, 5, 1)
    print(goles_ganador)

raiz.mainloop()  # Bucle principal
