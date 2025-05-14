#🎓 Administrador de calificaciones de estudiantes
#Registro de estudiantes y sus calificaciones:
#Añadir estudiantes
#Registrador Calificaciones
#Calcular el promedio por estudiante

estudiantes = {}

def AñadirEstudiante(nombre="",promedio:float=0,c1:float=0.0,c2:float=0.0,c3:float=0.0,c4:float=0.0,c5:float=0.0):
    promedio = (c1+c2+c3+c4+c5)/5
    estudiantes[nombre] = (promedio,c1,c2,c3,c4,c5)
    print(f"El estudiante {nombre} se ha agregado a la lista")

def CalcularPromedio(nombre):
    cal = estudiantes.get(nombre)
    if nombre in estudiantes and cal:
        print(f"El promedio del estudiante {nombre} es: {cal[0]}")

while True:
    opcion=input("Ingrese la opcion que desea realizar:\n 1.Añadir estudiante y sus calificaciones\n 2.Calcular su promedio\n 3.Salir del menu\n")
    if opcion =="1":
        nombre = input("Nombre del estudiante:").lower().strip()
        print("Ingrese las 5 calificaciones:\n")
        c1 = float(input("Calificacion: \n"))
        c2 = float(input("Calificacion: \n"))
        c3 = float(input("Calificacion: \n"))
        c4 = float(input("Calificacion: \n"))
        c5 = float(input("Calificacion: \n"))
        promedio = 0
        AñadirEstudiante(nombre,promedio,c1,c2,c3,c4,c5)

    elif opcion =="2":
        nombre = input("Nombre del estudiante para calcular su promedio: ")
        CalcularPromedio(nombre)
    elif opcion =="3":
        print("Salio del menu")
