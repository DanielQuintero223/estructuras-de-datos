# # diccionarios

# diccionario = {
#     "nombre": "Carlos",
#     "edad": 22,
#     "ciudad": "Madrid"
# }

# perfil = diccionario

# print(perfil["nombre"])

# diccionario anidado

# personas = {
#     "persona_1": {
#         "nombre": "Carlos",
#         "edad": 22,
#         "ciudad": "Madrid"
#     },
#     "persona_2": {
#         "nombre": "Daniel",
#         "edad": 33,
#         "ciudad": "Barcelona"
#     },
#     "persona_3": {
#         "nombre": "Ana",
#         "edad": 44,
#         "ciudad": "Valencia"
#     }
# }

# # recorrido del diccionario anidado
# for persona in personas:
#     print("")
#     for adentro in personas[persona]:
#         print(f"{adentro}: {personas[persona][adentro]}")


# # diccionario vacio

# persona = {
#     "nombre": None,
#     "edad": None,
#     "ciudad": None
# }

# persona["nombre"] = input("Introduce tu nombre: ")
# persona["edad"] = input("Introduce tu edad: ")
# persona["ciudad"] = input("Introduce tu ciudad: ")

# print(persona)


# ejercicio de diccionario


datos_personales = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None
}

datos_personales["nombre"] = input("Introduce tu nombre: ")
datos_personales["edad"] = int(input("Introduce tu edad: "))
datos_personales["direccion"] = input("Introduce tu direccion: ")
datos_personales["telefono"] = int(input("Introduce tu telefono: "))

print("Su nombre es: ", datos_personales["nombre"], "y tiene una edad de ", datos_personales["edad"],
      "años, vive en ", datos_personales["direccion"], "y su telefono es: ", datos_personales["telefono"])
