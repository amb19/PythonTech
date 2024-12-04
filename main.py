# ---------------- Funciones  ---------------- #
def agregar_producto():
    return

def mostrar_productos():
    return



# ---------------- Menu de inicio  ---------------- #
def menu():
    # ---------------- Variables  ---------------- #
    bienvenida = "Bienvenido al sistema de Inventario"
    opciones = "Menu de Opciones"
    elegir = "Eliga una Opcion del 1 al 7:"
    # ---------------- Opcion  ---------------- #
    while True:
        print("")
        print(f"{bienvenida:^60}\n{opciones:^60}\n")
        print("1- Registrar Productos")
        print("2- Mostrar Productos")
        print("3- Actualizar cantidad de Productos")
        print("4- Eliminar Productos")
        print("5- Buscar Productos")
        print("6- Reporte de bajo stock")
        print("7- Salir\n")
    
        opcion = input(f"{elegir:^35}")
    # ---------------- condiciones y llamado a funciones  ---------------- #
        if opcion == '1':
            print(agregar_producto())
        elif opcion == '2':
            print(agregar_producto())
        elif opcion == '3':
            print(agregar_producto())
        elif opcion == '4':
            print(agregar_producto())
        elif opcion == '5':
            print(agregar_producto())
        elif opcion == '6':
            print(agregar_producto())
        elif opcion == '7':
            print("*** Saliste del sistema de Inventario***")
            break
        else:
            print("\n*** ! Opcion NO correcta ! *** " f"\n*** Por Favor {elegir} ***")
# ---------------- llamado a funcion principal  ---------------- #
menu()