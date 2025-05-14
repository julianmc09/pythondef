#1. 📚 Rastreador de libros de la biblioteca
#Sistema para gestionar una biblioteca virtual:
#Añadir libros (título, autor, páginas)
#Buscar libros por título
#Mostrar todos los libros disponibles

libros = {}

def AñadirLibros(titulo="",autor="",paginas:int=0):
    if titulo in libros:
        print(f"El libro {titulo} ya existe")
    else:
        libros[titulo] = (autor, paginas)
        print(f"El libro {titulo} se ha agregado")

def BuscarLibros(titulo):
    libro = libros.get(titulo)
    if libro:
        print(f" Libro: {titulo}\n Autor: {libro[0]}\n Paginas: {libro[1]}")   
    else:
        print(f"El libro {titulo} no esta en el inventario")

def MostrarLibros(titulo):
    if titulo in libros:
        print("Libros disponibles:")
        for i in libros:
            print(i)
while True:
    opcion = input("Ingrese la opcion que desea realizar:\n 1.Añadir libro\n 2.Buscar libro\n 3.Mostrar libros disponibles\n 4.Salir del menu\n")
    if opcion == "1":
        titulo = input("Nombre del libro: ").strip().lower()
        autor = input("Autor del libro: ")
        paginas = int(input("Paginas que contiene el libro: "))
        if paginas is not None:
            AñadirLibros(titulo,autor,paginas)
    
    elif opcion =="2":
        titulo = input("Titulo del libro a consultar: ").strip().lower()
        BuscarLibros(titulo)

    elif opcion =="3":
        MostrarLibros(titulo)

    elif opcion =="4":
        print("Salio del menu")
        break
