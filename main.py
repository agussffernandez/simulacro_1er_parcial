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


def ordenar_inventario(inventario: list) -> list:
    """ 
    Ordenar los productos en función de su precio de manera ascendente y luego mostrar por pantalla los productos ordenados.
    """
    longitud = len(inventario)
    
    # Implementación de Bubble Sort:
    # Compara dos elementos adyacentes. Si el primer elemento es mayor que el segundo (en caso de orden ascendente), se intercambian.
    for i in range(longitud):
        for j in range(0, longitud-i-1):
            if inventario[j][1] > inventario[j+1][1]:  # Comparar precios
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                temporal = inventario[j+1]
                inventario[j+1] = inventario[j]
                inventario[j] = temporal
    print("El inventario ordenado por precio es: ")
    print(inventario)
    return inventario



def mostrar_producto_mas_caro(inventario: list) -> list:
    """
    Muestra el producto con el precio mas caro del inventario
    """
    if not inventario: #Verifica si el inventario está vacio
        print("El inventario esta vacío")
        return
    
    producto_mas_caro = inventario[0] # Inicializo con el primer producto
    
    for i in range(1, len(inventario)): # comienzo desde el segundo elemento
        if inventario[i][1] > producto_mas_caro[1]:
            producto_mas_caro = inventario[i]
    print(producto_mas_caro)




def menu_principal():
    
    inventario = []
    
    print("Bienvenido!...Elija una de las opciones")
    mostrar_menu_principal()
    
    opcion = int(input("Elija una opción del 1 al 6: "))
    
    while opcion != 6:
        
        if opcion == 1:
            cargar_inventario(inventario)
        
        elif opcion == 2:
            buscar_producto(inventario)
        
        elif opcion == 3:
            ordenar_inventario(inventario)
        
        elif opcion == 4:
            mostrar_menu_principal(inventario)
        
        opcion = int(input("Elija una opción del 1 al 6: "))
    
    print(inventario)




menu_principal()


