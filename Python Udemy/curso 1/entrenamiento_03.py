# se crea el grupo en una lista
GrupoA = {}


def calificaciones(Grupo):
    for nombre, notas in Grupo.items():
        print(
            f"El estudiante {nombre} tiene las siguientes notas: {notas}")
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es: {promedio}")
        if promedio >= 3:
            print(f"{nombre} ha aprobado")
        else:
            print(f"{nombre} ha reprobado")


print("Desea agregar estudiantes ? ")
ingreso = input(
    'Ingrese y para agregar o n para no agregar? (y/n): ').lower().strip() == 'y'
while ingreso:
    nombre = input("Ingrese el nombre del estudiante: ")
    print("Por favor ingrese las notas del estudiante: ")
    notas = []
    for i in range(3):
        nota = float(input("Ingrese la nota: "))
        notas.append(nota)
        GrupoA[nombre] = notas
    print(GrupoA)
    print("Desea agregar otro estudiante ? ")
    ingreso = input(
        'Ingrese y para agregar o n para no agregar? (y/n): ').lower().strip() == 'y'

calificaciones(GrupoA)
