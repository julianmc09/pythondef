#Editor de menú de restaurante
#Gestión de menú en un restaurante:
#Añadir platos (nombre, precio, disponibilidad)
#Modificar disponibilidad
#Calcular total de platos disponibles

menu = {}

def AñadirPlato(nombre="", precio:float=0.0, disponible=0):
    if nombre in menu:
        print(f"El plato {nombre} ya existe.")
    else:
        menu[nombre] = {"precio": precio,"disponible": disponible}
        print(f"Plato {nombre} añadido correctamente.")

def ModificarDisponibilidad(nombre, disponible,estado):
    if nombre in menu:
        menu[nombre]["disponible"] = disponible
        estado = ""
        if estado == "disponible":
            print(f"El plato {nombre} ahora está {estado}.")
        elif estado == "no disponible":
            print(f"El plato {nombre} ahora no esta disponible ")
    else:
        print(f"El plato {nombre} no se encuentra en el menú.")

def TotalDisponibles():
    disponibles = sum(1 for plato in menu.values() if plato["disponible"])
    print(f"Total de platos disponibles: {disponibles}")
    return disponibles

while True:
    opcion=input("Ingrese la opcion que desea realizar:\n 1.Añadir plato\n 2.Modificar disponibilidad\n 3.Mostrar total de platos disponibles\n 4.Salir del menu\n")
    if opcion == "1":
        nombre = input("Nombre del plato: ").lower().strip()
        precio = float(input("Precio del plato: "))
        disponible = input("Disponibilidad: ")
        AñadirPlato(nombre,precio,disponible)

    elif opcion == "2":
        nombre = input("Nombre del plato a modificar: ").lower().strip()
        estado = input("Nuevo estado: ")
        ModificarDisponibilidad(nombre,disponible,estado)

    elif opcion == "3":
        TotalDisponibles()

    elif opcion == "4":
        print("Salio del menu")
        break