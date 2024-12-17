# ---------------- Aclarariones  ---------------- #
# decidi usar el metodo .upper(), para igualar todo los string en mayuscula, para evitar los acentos. 

# ---------------- Variables de las funciones  ---------------- #
inventario = []
prod_bajo_stock = []
# ---------------- Funciones  ---------------- #
def agregar_producto():
    articulo = input("Ingrese nombre del producto: ").upper()
    descripcion = input("Ingrese la descripcion del Producto: ").upper()
    precio = float(input("Ingrese el Precio del Producto: "))
    cantidad = int(input("Ingrese la cantidad del Producto: "))
    categoria = input("Ingrese la categoria del producto: ").upper()
    
    producto = {"articulo": articulo, "descripcion": descripcion, "precio": precio, "cantidad": cantidad, "categoria": categoria}
    inventario.append(producto)
    return f"\n*** El Producto: {articulo} se ha Registador con exito. ***\n"

def mostrar_productos():
    if not inventario:
        return "*** El inventario esta vacio. ***\n *** Por favor Registre un Producto en la opcion 1 ***\n"
    for producto in inventario:
        print(f"\n- Producto: {producto['articulo']} - Descripcion: {producto['descripcion']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']} - Categoria: {producto['categoria']}")
    return f"\n*** La cantidad de Productos en el inventario es: {len(inventario)}. ***\n"

def actualizar_productos():
    articulo_buscar = input("Indique el producto y cantidad a actualizar: ").upper()
    for producto in inventario:
        if producto["articulo"] == articulo_buscar:
            nueva_cantidad = int(input(f" - Cantidad actual: {producto['cantidad']} - Nueva cantidad: "))
            producto["cantidad"] = nueva_cantidad
            return f"\n*** La cantidad de Productos: {articulo_buscar} actualizado! Nueva cantidad: {nueva_cantidad} ***\n"
    
    return f"\n*** No se encontro Producto, Puede ser que No este Registrado ***\n " 

def eliminar_productos():
    articulo_eliminar = input("Ingrese el nombre del Producto a eliminar: ").upper()
    
    for producto in inventario:
        if producto["articulo"] == articulo_eliminar:
            inventario.remove(producto)
            return f"\n*** El Producto {articulo_eliminar} Eliminado ! ***\n"
    
    return f"\n*** No se encontro Producto, Puede ser que No este Registrado ***\n" 

def buscar_productos():
    articulo_buscar = input("Indique el Producto a buscar: ").upper()
    
    for producto in inventario:
        if producto["articulo"] == articulo_buscar:
            return(
            f"- Articulo: {producto['articulo']}\n"
            f"- Descripcion: {producto['descripcion']}\n"
            f"- Precio: ${producto['precio']}\n"
            f"- Cantidad: {producto['cantidad']}\n"
            f"- Categoria: {producto['categoria']}\n"
            )
    
    return f"\n*** No se encontro Producto, Puede ser que No este Registrado ***\n" 

def stock_productos():
    bajo_stock = int(input("Ingrese La cantidad a contemplar como ¡ Bajo Stock !: "))
    if bajo_stock <= 0:
        return "El Stock No debe ser Menor o Igual a cero"
    
    for producto in inventario:
        if producto["cantidad"] <= bajo_stock:
            prod_bajo_stock.append(producto)
            print(f"- Producto: {producto['articulo']}; con bajo stock: {producto['cantidad']}")
    
    if not prod_bajo_stock:
        return "\n*** No hay Productos en riesgo de bajo stock ***\n"
    
    return f" Productos totales con bajo stock: {len(prod_bajo_stock)}\n"


# ---------------- Menu de inicio  ---------------- #
def menu():
    # ---------------- Variables del menu  ---------------- #
    bienvenida = "Bienvenido al sistema de Inventario"
    opciones = "Menu de Opciones"
    elegir = " Eliga una Opcion del 1 al 7: "
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
    
        opcion = input(f"{elegir:^30}")
    # ---------------- condiciones y llamado a funciones  ---------------- #
        if opcion == '1':
            print(agregar_producto())
        elif opcion == '2':
            print(mostrar_productos())
        elif opcion == '3':
            print(actualizar_productos())
        elif opcion == '4':
            print(eliminar_productos())
        elif opcion == '5':
            print(buscar_productos())
        elif opcion == '6':
            print(stock_productos())
        elif opcion == '7':
            print("*** Saliste del sistema de Inventario ***")
            break
        else:
            print("\n*** ! Opcion NO correcta ! *** " f"\n*** Por Favor {elegir} ***")
# ---------------- llamado a funcion principal  ---------------- #
menu()