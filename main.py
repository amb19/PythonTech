# ---------------- Variables  ---------------- #
bienvenidad = "Bienvenido al sistema de Inventario"
menu = "Menu de Opciones"
elegir = "Eliga una Opcion del 1 al 7:"
producto = []
inventario = []
# ---------------- Menu de inicio  ---------------- #
while True:
    print("")
    print(f"{bienvenidad:^60}\n{menu:^60}\n")
    print("1- Registro de Productos")
    print("2- Consulta de Productos")
    print("3- Actualizacion de Productos")
    print("4- Eliminar Productos ")
    print("5- Listado De Productos")
    print("6- Stock de Productos ")
    print("7- Salir\n")
    
# ---------------- seleccion de Opcion  ---------------- #
    try:
        opcion = int(input(f"{elegir:^35}"))

        if opcion == 1:
            print(f"Has seleccionado la opcion: {opcion}, Registro\n")
            nombre_producto = input("Ingrese el nombre del Producto: ")
#--- condicionales para validar que la carga de informacion se realice correctamente----#                  
            precio = float(input("Ingrese el Precio del Producto: "))   
            if not precio > 0:
                print("\n *** Ingrese un Precio Mayor a 0$ ***")
                continue
            stock = int(input("Ingrese el stock del Producto: "))
            if stock <= 0:
                print("\n *** El Stock no puede ser Negativo o O *** ")
            producto = [nombre_producto, precio, stock]
            inventario.append(producto)    
            print("\n*** Producto agregado al inventario. *** !")
        elif opcion == 2:
#--- para consultar los productos cargado previament en la opcion 1----#             
            print(f"Has seleccionado la opcion: {opcion}, Consulta\n")
            if not inventario:
                print("*** El Inventario esta vacio. *** \n Por favor vaya a la Opcion 1")
            else:
                for id, producto in enumerate(inventario, start=1):
                    print(f"Producto {id}:")
                    print(f"Nombre del Producto: {producto[0]}")               
                    print(f"Precio del Producto: {producto[1]}")
                    print(f"Stock del Producto: {producto[2]}")
        elif opcion == 3:
            print(f"Has seleccionado la opcion: {opcion}, Actualizacion")
        elif opcion == 4:
            print(f"Has seleccionado la opcion: {opcion}, Elimininar")
        elif opcion == 5:
            print(f"Has seleccionado la opcion: {opcion}, Listado")
        elif opcion == 6:
            print(f"Has seleccionado la opcion: {opcion}, Stock")
        elif opcion == 7:
            print(f"Has seleccionado la opcion: {opcion}, Salir de Sistema")
            break
        else:
            print(f"\n*** Por Favor {elegir} ***")
    except ValueError:
        print("\n*** ! Opcion NO correcta ! *** " f"\n*** Por Favor {elegir} ***")