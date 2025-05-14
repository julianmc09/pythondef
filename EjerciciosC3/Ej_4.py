#Warehouse Box Counter
#Seguimiento de cajas en un almacén:
#Añadir tipos de caja
#Actualizar cantidades
#Verificar si hay cantidad suficiente
almacen = {}

def AñadirTipoCaja(nombre, cantidad):
    if nombre in almacen:
        print(f"El tipo de caja {nombre} ya existe.")
    else:
        almacen[nombre] = cantidad
        print(f"Caja {nombre} añadida con {cantidad} unidades.")

def ActualizarCantidad(nombre, cantidad):
    if nombre in almacen:
        almacen[nombre] += cantidad
        print(f"Cantidad actualizada. Ahora hay {almacen[nombre]} unidades de {nombre}")
    else:
        print(f"El tipo de caja {nombre} no existe.")

def VerificarCantidad(nombre, requerida):
    if nombre in almacen:
        if almacen[nombre] >= requerida:
            print(f"Hay suficiente cantidad de {nombre}. ({almacen[nombre]} disponibles)")
        else:
            print(f"No hay suficiente cantidad de {nombre}. Solo hay {almacen[nombre]} unidades.")
    else:
        print(f"El tipo de caja {nombre} no existe en el almacén.")

while True:  
    opcion = input("Seleccione la opcion que desea realizar:\n 1. Añadir tipo de caja\n 2. Actualizar cantidad de caja\n 3. Verificar cantidad disponible\n 4.salir\n ")
 
    if opcion == "1":
        nombre = input("Ingrese el nombre del tipo de caja: ")
        try:
            cantidad = int(input("Ingrese la cantidad inicial: "))
            AñadirTipoCaja(nombre, cantidad)
        except ValueError:
            print("Error: la cantidad debe ser un número entero.")
    
    elif opcion == "2":
        nombre = input("Ingrese el nombre del tipo de caja: ")
        try:
            cantidad = int(input("Ingrese la cantidad a añadir o quitar (use números negativos para restar): "))
            ActualizarCantidad(nombre, cantidad)
        except ValueError:
            print("Error: la cantidad debe ser un número entero.")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre del tipo de caja: ")
        try:
            requerida = int(input("Ingrese la cantidad requerida: "))
            VerificarCantidad(nombre, requerida)
        except ValueError:
            print("Error: la cantidad requerida debe ser un número entero.")
    
    elif opcion == "4":
        print("Salio del programa")
        break

    else:
        print("Opción no válida")
