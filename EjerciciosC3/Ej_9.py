#Centro de adopción de mascotas:
#Añadir mascotas (nombre, especie, edad)
#Buscar por especie
#Filtrar por edad

mascotas = []

def AñadirMascota(nombre, especie, edad):
    mascota = { "nombre": nombre,"especie": especie.lower(),"edad": edad}
    mascotas.append(mascota)
    print(f"Mascota añadida: {nombre}, {especie}, {edad} años.")

def BuscarPorEspecie(especie):
    especie = especie.lower()
    print(f"Mascotas de especie {especie}:")
    encontradas = [m for m in mascotas if m["especie"] == especie]
    if encontradas:
        for m in encontradas:
            print(f"{m['nombre']} ({m['edad']} años)")
    else:
        print("No se encontraron mascotas de esa especie.")

def FiltrarPorEdad(max_edad):
    print(f"Mascotas con edad menor o igual a {max_edad}:")
    filtradas = [m for m in mascotas if m["edad"] <= max_edad]
    if filtradas:
        for m in filtradas:
            print(f"{m['nombre']} ({m['especie']}, {m['edad']} años)")
    else:
        print("No se encontraron mascotas con esa edad.")

while True:
    opcion = input("Seleccione la opcion que desea realizar:\n 1.Añadir mascota\n 2.Buscar mascota por especie\n 3.Filtrar por edad\n 4.Salir")
    if opcion == "1":
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie: ")
        try:
            edad = int(input("Edad (en años): "))
            AñadirMascota(nombre, especie, edad)
        except ValueError:
            print("La edad debe ser un numero entero.")

    elif opcion == "2":
        especie = input("Especie a buscar: ")
        BuscarPorEspecie(especie)

    elif opcion == "3":
        try:
            max_edad = int(input("Edad maxima: "))
            FiltrarPorEdad(max_edad)
        except ValueError:
            print("La edad debe ser un numero entero.")


    elif opcion == "4":
        print("Salio del menu")
        break

    else:
        print("Opción invalida")
