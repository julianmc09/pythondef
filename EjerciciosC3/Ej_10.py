#Gestión de socios de gimnasio:
#Registrar nuevos socios
#Cambiar plan de membresía
#Listar socios con pagos atrasados

socios = []

def RegistrarSocio(nombre, plan, PagoAlDia=True):
    socio = { "nombre": nombre,"plan": plan.lower(),"PagoAlDia": PagoAlDia}
    socios.append(socio)
    print(f"Socio registrado: {nombre} Plan: {plan}, Pago al dia: {PagoAlDia})")

def CambiarPlan(nombre, NuevoPlan):
    for socio in socios:
        if socio["nombre"].lower() == nombre.lower():
            socio["plan"] = NuevoPlan.lower()
            print(f"Plan de {nombre} cambiado a '{NuevoPlan}'.")
            return
    print("Socio no encontrado.")

def ListarAtrasados():
    print("Socios con pagos atrasados:")
    encontrados = False
    for socio in socios:
        if not socio["PagoAlDia"]:
            print(f"{socio['nombre']} (Plan: {socio['plan']})")
            encontrados = True
    if not encontrados:
        print("Todos los socios estan al dia.")

while True:
    opcion = input("Seleccione la opcion que desea realizar:\n 1.Registrar nuevo socio\n 2.Cambiar plan de membresia\n 3.Lista de socios con pagos atrasados\n 4.Salir ")
    if opcion == "1":
        nombre = input("Nombre del socio: ")
        plan = input("Plan de membresia: ")
        PagoInput = input("¿El pago esta al dia? (s/n): ").lower()
        PagoAlDia = True if PagoInput == 's' else False
        RegistrarSocio(nombre, plan, PagoAlDia)

    elif opcion == "2":
        nombre = input("Nombre del socio a actualizar: ")
        NuevoPlan = input("Nuevo plan de membresia: ")
        CambiarPlan(nombre, NuevoPlan)

    elif opcion == "3":
        ListarAtrasados()

    elif opcion == "4":
        print("Salio del menu")
        break

    else:
        print("Opción invalida")
