#Movie Rating System
#Sistema de calificación de películas
#Añadir películas
#Registrar calificaciones (1–5)
#Calcular promedio de calificación

peliculas = {}

def AñadirPelicula(nombre):
    if nombre in peliculas:
        print(f"La película {nombre} ya está registrada.")
    else:
        peliculas[nombre] = []
        print(f"Película {nombre} añadida correctamente.")

def RegistrarCalificacion(nombre, calificacion):
    if nombre not in peliculas:
        print(f"La película {nombre} no está registrada.")
    elif not 1 <= calificacion <= 5:
        print("La calificación debe estar entre 1 y 5.")
    else:
        peliculas[nombre].append(calificacion)
        print(f"Calificación {calificacion} añadida a {nombre}.")

def CalcularPromedio(nombre):
    if nombre not in peliculas:
        print(f"La película {nombre} no está registrada.")
    elif not peliculas[nombre]:
        print(f"ℹLa película {nombre} no tiene calificaciones aún.")
    else:
        promedio = sum(peliculas[nombre]) / len(peliculas[nombre])
        print(f"Promedio de calificación para {nombre}: {promedio:.2f}")

while True:
    opcion = input("Seleccione la opcion que desea realizar:\n 1.Añadir pelicula\n 2.Registrar calificacion\n 3.Calcular promedio de calificacion\n 4.Salir ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la película: ")
        AñadirPelicula(nombre)

    elif opcion == "2":
        nombre = input("Ingrese el nombre de la película: ")
        try:
            calificacion = int(input("Ingrese la calificación (1 a 5): "))
            RegistrarCalificacion(nombre, calificacion)
        except ValueError:
            print("La calificación debe ser un número entero.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre de la película: ")
        CalcularPromedio(nombre)

    elif opcion == "4":
        print("Salio del menu")
        break

    else:
        print("Opción no válida")
