# ---------------- Variables  ---------------- #
bienvenidad = "Bienvenido al sistema de Inventario"
menu = "Menu de Opciones"
elegir = "Eliga una Opcion del 1 al 7 :"
# ---------------- Menu de inicio  ---------------- #
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
opcion = int(input(f"{elegir:^35}"))

if opcion == 1:
    print(f"Ha seleccionado la opcion{opcion}: Registro")
elif opcion == 2:
    print(f"Ha seleccionado la opcion{opcion}: Consulta")
elif opcion == 3:
    print(f"Ha seleccionado la opcion{opcion}: Actualizacion")
elif opcion == 4:
    print(f"Ha seleccionado la opcion{opcion}: Elimininar")
elif opcion == 5:
    print(f"Ha seleccionado la opcion{opcion}: Listado")
elif opcion == 6:
    print(f"Ha seleccionado la opcion{opcion}: Stock")
elif opcion == 7:
    print(f"Ha seleccionado la opcion{opcion}: Salir de Sistema")
else:
    print("No ha selecciona una opcion correcta, Por Favor seleccione una opcion en entre el 1 y 7")
