#Lista de tareas con prioridades y estado:
#Añadir tareas
#Marcar tareas como completadas
#Filtrar por prioridad o estado

tareas = []

def AñadirTarea(descripcion, prioridad):
    tarea = { "descripcion": descripcion,"prioridad": prioridad.lower(),"estado": "pendiente"}
    tareas.append(tarea)
    print(f"Tarea añadida: {descripcion} (Prioridad: {prioridad})")

def MarcarCompletada(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["estado"] = "completada"
        print(f"Tarea {tareas[indice]['descripcion']} marcada como completada.")
    else:
        print("Índice inválido.")

def FiltrarTareas(filtro, valor):
    valor = valor.lower()
    print(f"Tareas filtradas por {filtro} = {valor}:")
    encontradas = False
    for i, tarea in enumerate(tareas):
        if tarea[filtro] == valor:
            print(f"{i}. [{tarea['estado'].upper()}] {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")
            encontradas = True
    if not encontradas:
        print("No se encontraron tareas con ese filtro.")

while True:

    opcion = input("Ingrese la opcion que desea realizar:\n 1.Añadir tarea\n 2.Marcar tarea como completada\n 3.Filtrar tareas por estado\n 4.Salir\n ")

    if opcion == "1":
        descripcion = input("Descripción de la tarea: ")
        prioridad = input("Prioridad (alta/media/baja): ")
        AñadirTarea(descripcion, prioridad)

    elif opcion == "2":
        prioridad = input("Ingrese la prioridad a filtrar (alta/media/baja): ")
        FiltrarTareas("prioridad", prioridad)

    elif opcion == "3":
        estado = input("Ingrese el estado a filtrar (pendiente/completada): ")
        FiltrarTareas("estado", estado)

    elif opcion == "4":
        print("Salio del menu")
        break

    else:
        print("Opción inválida")
