#Analizar instrucciones para comenzar el ejercicio 
#funciones = return True and False 
#Repaso estructuras de datos (tuples)

# añadir, consultar, actualizar y eliminar productos del inventario
# #el valor total del inventario

    # Añadir productos:
    # Cada producto debe estar definido por su nombre, precio y cantidad disponible
    # Esta información será almacenada de modo que el inventario pueda crecer dinámicamente

#Consultar productos:
# Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
#Si el producto no está en el inventario, se debe notificar adecuadamente

#Actualizar precios:
#El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario

#Eliminar productos:
#El programa debe permitir al usuario eliminar productos del inventario de manera segura

#Calcular el valor total del inventario:
#El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
#Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.
#precio * cantidad + (precio * cantidad_de_todos_los_productos) 

#OBSERVACION: Diccionario para contener todos los productos

panela = (1000, 9)
cantidad = panela[1]
new_price = 5000
panela = (new_price, cantidad)


inventario = {
    "Fab" : (1500, 8),
    "Panela" : (5000, 9)
}

cantidad = inventario["Panela"][1]
nuwvo_precio = 10000
inventario["Panela"] = (nuwvo_precio, cantidad)
print(inventario["Panela"])


# Tu programa debe diseñarse modularmente, con funciones bien definidas que gestionen cada operación mencionada. 
# Además, debes almacenar los productos en un diccionario, donde el nombre del producto sea la clave, y el precio 
# y la cantidad sean los valores asociados, almacenados en una tupla.



while True:
    print("\n****Menu****\n")
    print("\nOPCIONES")
    print("1.Añadir productos")
    print("2.Editar")
    print("3.Eliminar")
    print("4.Salir\n")

    menu = (input("Ingrese una opcion: "))


    if menu == "1":
        print("Has elegido añadir producto ")
    elif menu == "2":
        print("Has elegido editar  ")
    elif menu == "3":
        print("Has elegido eliminar  ")
    elif menu == "4":
        print("has elegido salir")
        break
    else:
        print("Ingresa un valor del 1-4")

cantidad = inventario["Fab"][1]
nuevo_precio = 90000
inventario["Fab"] = (nuevo_precio, cantidad)
print(inventario["Fab"])

pan = (5000, 10)
cantidad = pan[1]
nuevo_precio  = 8000000000
pan = (nuevo_precio, cantidad)
print(pan)