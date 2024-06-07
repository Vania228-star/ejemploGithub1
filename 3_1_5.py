curso = []
alumno = []

for i in range(2):
    nombre= input("INGRESE NOMBRE ")
    dirección = input("INGRESE DIRECCIÓN ")
    telefono=int(input("INGRESE TELÉFONO "))
    alumno = [nombre,dirección,telefono]
    curso.append(alumno)

for i in range(len(curso)):
    print(f"REGISTRO N {curso.index(i)}")
    print(f"NOMBRE: {curso[i][0]}")
    print(f"DIRECCIÓN: {curso[i][1]}")
    print(f"TELÉFONO: {curso[i][2]}")
    print("-------------------------")

buscar = input("INGRESE NOMBRE ")
posicionNombre = curso.index(buscar)
direccion = curso[posicionNombre][1]
posicionDireccion = curso.index(direccion)
print(f"indice nombre {posicionNombre}")
print(F"indice dirección {posicionDireccion}")