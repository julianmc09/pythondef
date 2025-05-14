#Online Course Tracker
#Gestión de cursos en línea:
#Registrar cursos (título, duración, inscritos)
#Actualizar número de inscritos
#Filtrar por duración mínima

cursos = {}

def RegistrarCurso(titulo, duracion, inscritos):
    if titulo in cursos:
        print(f"El curso {titulo} ya está registrado.")
    else:
        cursos[titulo] = {"duracion": duracion, "inscritos": inscritos}
        print(f"Curso {titulo} registrado correctamente.")

def ActualizarInscritos(titulo, nuevos_inscritos):
    if titulo in cursos:
        cursos[titulo]["inscritos"] += nuevos_inscritos
        print(f"Inscritos actualizados. Total ahora: {cursos[titulo]['inscritos']}")
    else:
        print(f"El curso {titulo} no existe.")

def FiltrarPorDuracion(minima):
    print(f"Cursos con duración mayor o igual a {minima} horas:")
    encontrados = False
    for titulo, datos in cursos.items():
        if datos["duracion"] >= minima:
            print(f"{titulo}: {datos['duracion']} hrs, {datos['inscritos']} inscritos")
            encontrados = True
    if not encontrados:
        print("No se encontraron cursos con esa duración mínima.")

while True:
    opcion = input("Seleccione la opcion que desea realizar:\n 1.Registrar curso\n 2.Actualizar numero de inscritos\n 3.Filtrar por duracion minima\n 4.Salir ")
    if opcion == "1":
        titulo = input("Título del curso: ")
        try:
            duracion = int(input("Duración en horas: "))
            inscritos = int(input("Número de inscritos: "))
            RegistrarCurso(titulo, duracion, inscritos)
        except ValueError:
            print("Duración e inscritos deben ser números enteros.")

    elif opcion == "2":
        titulo = input("Título del curso: ")
        try:
            nuevos = int(input("Cantidad a añadir (+ o -): "))
            ActualizarInscritos(titulo, nuevos)
        except ValueError:
            print("La cantidad debe ser un número entero.")

    elif opcion == "3":
        try:
            minima = int(input("Duración mínima (en horas): "))
            FiltrarPorDuracion(minima)
        except ValueError:
            print("La duración mínima debe ser un número entero.")

    elif opcion == "4":
        print("Salio del menu")
        break

    else:
        print("Opción inválida")
