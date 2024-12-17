Instrucciones para Ejecutar la Aplicación

1.	Requisitos previos:
	    Asegúrate de tener instalado Python 3.x en tu sistema.
2.	Ejecución del código:
	    Abre una terminal o línea de comandos.
	    Navega hasta la ubicación donde está el archivo.
	    Ejecuta el programa escribiendo:  python main.py
3.	Interacción con la aplicación:
    	Cuando ejecutes el programa, se te pedirá que ingreses los datos de un producto. Sigue las instrucciones en pantalla para ingresar cada dato correctamente.
    	La aplicación “NO” incluye validaciones, por lo que si ingresas un dato incorrecto (por ejemplo, texto en lugar de un número), el mismo no funcionará y dará error nuevamente.
-----------------------------------------------------------------------------------------------------------------------------
Funcionalidades Implementadas

1.	Agregar Productos al Inventario:
	    Descripción: Permite agregar un producto con los datos requeridos: nombre, descripción, precio, y cantidad.
    Almacenamiento:
        Cada producto se almacena en la lista inventario, donde cada elemento es una lista con los datos del producto.
    Flujo de Interacción:
        1.	Solicita el nombre del producto.
        2.	Solicita la descripción del producto.
        3.	Solicita el precio 
        4.	Solicita la cantidad 
2.	Almacenamiento de Datos en Estructuras de Lista:
        Cada producto agregado al inventario se almacena en una lista con el formato:
        ["NOMBRE", "DESCRIPCIÓN", PRECIO, CANTIDAD, CATEGORIA]
3.	Extensibilidad:
        La aplicación está diseñada para facilitar la adición de nuevas funcionalidades, como mostrar el inventario, eliminar productos o actualizar datos.
