def mostrar_menu_principal():
    """ 
    Muestra el menú de opciones
    """
    print(""" 
    1. Cargar producto/s
    2. Buscar producto
    3. Ordenar inventario
    4. Mostrar producto más caro y más barato
    5. Mostrar productos con precio mayor a 15000
    6. Salir
    """)

def cargar_inventario(inventario:list) -> list:
    """ 
    Carga el inventario con los datos del o los productos en una matriz (nombre, precio, cantidad).
    """
    nombre = input("Ingrese el nombre del nuevo producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))
    nuevo_producto = [nombre, precio, cantidad]
    inventario.append(nuevo_producto)
    return inventario


def buscar_producto(inventario: list) -> list|None:
    """ 
    Busca un producto por su nombre y muestra por pantalla todos los datos de ese producto (nombre, precio y cantidad)
    """
    nombre_producto_a_buscar = input("Ingrese el producto que quiere buscar: ")
    for i in range(len(inventario)):
        if inventario[i][0] == nombre_producto_a_buscar:
            datos_de_producto = inventario[i]
            return print(datos_de_producto)
    
    print(f"Producto {nombre_producto_a_buscar} no encontrado")
    return None





def menu_principal():
    
    inventario = []
    
    print("Bienvenido!...Elija una de las opciones")
    mostrar_menu_principal()
    
    opcion = int(input("Elija una opción del 1 al 6: "))
    
    while opcion != 6:
        
        if opcion == 1:
            cargar_inventario(inventario)
        
        
        opcion = int(input("Elija una opción del 1 al 6: "))
    
    print(inventario)


menu_principal()


