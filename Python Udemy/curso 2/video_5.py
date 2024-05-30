# personas = (('Juan', 22), ('Maria', 33), ('Luis', 44))

# for nombre, edad in personas:
#     if edad > 18:
#         print(nombre, " es mayor de edad")


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5000]

# suma = sum(numeros)

# print(suma)


# ejercicio video

palabras = ["Daniel", "Estefania", "Juan", "Maria", "Luis", "Pedro", "Ana", "Jose", "Carlos", "Andres", "Sofia", "Camila", "Valentina", "Mariana", "Fernando", "Javier", "Cristian",
            "Jorge", "Andrea", "Diana", "Laura", "Sara", "Santiago", "Felipe", "Miguel", "Alejandro", "Ricardo", "Roberto", "Raul", "Rosa", "Lina", "Luz", "Lorena", "Liliana", "Luisa"]

buscador = input("Ingrese el nombre a buscar: ")

if buscador in palabras:
    print("El nombre se encuentra en la lista")
else:
    print("El nombre no se encuentra en la lista")
