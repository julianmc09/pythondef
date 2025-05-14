#Billetera digital con gastos por categoría:
#Registrar gastos
#Calcular total gastado
#Calcular porcentaje por categoría

# Lista de gastos, cada uno con monto y categoría
gastos = []

def RegistrarGastos(monto, categoria):
    gastos.append({"monto": monto, "categoria": categoria.lower()})
    print(f"Gasto de {monto:.2f} registrado en la categoria {categoria}.")

def CalcularTotal():
    total = sum(gasto["monto"] for gasto in gastos)
    print(f"Total gastado: {total:.2f}")
    return total

def PorcentajePorCategoria():
    if not gastos:
        print("No hay gastos registrados.")
        return
    total = CalcularTotal()
    categorias = {}
    for gasto in gastos:
        cat = gasto["categoria"]
        categorias[cat] = categorias.get(cat, 0) + gasto["monto"]

    print("Porcentaje de gastos por categoria:")
    for categoria, monto in categorias.items():
        porcentaje = (monto / total) * 100
        print(f" {categoria.capitalize()}: {monto:.2f} ({porcentaje:.2f}%)")


while True:
    opcion = input("Seleccione la opcion que desea realizar:\n 1.Registrar gasto\n 2.Calcular total gastado\n 3.Calcular porcentaje por categoria\n 4.Salir ")
    if opcion == "1":
        try:
            monto = float(input("Ingrese el monto del gasto: "))
            categoria = input("Ingrese la categoría del gasto: ")
            RegistrarGastos(monto, categoria)
        except ValueError:
            print("El monto debe ser un número valido.")

    elif opcion == "2":
        CalcularTotal()

    elif opcion == "3":
        PorcentajePorCategoria()

    elif opcion == "4":
        print("Salio del menu")
        break

    else:
        print("Opción invalida.")
