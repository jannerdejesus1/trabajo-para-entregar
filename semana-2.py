# Sistema de gestión de inventario
inventario = []
 
# Pide un número decimal al usuario hasta que sea válido
def pedir_precio():
    precio_valido = False
    while not precio_valido:
        try:
            precio = float(input("Precio del producto: "))
            precio_valido = True
        except ValueError:
            print("Valor inválido. Ingrese un número.")
    return precio
 
# Pide un número entero al usuario hasta que sea válido
def pedir_cantidad():
    cantidad_valida = False
    while not cantidad_valida:
        try:
            cantidad = int(input("Cantidad del producto: "))
            cantidad_valida = True
        except ValueError:
            print("Valor inválido. Ingrese un número entero.")
    return cantidad

# Solicita los datos del producto y lo guarda en el inventario
def agregar_producto():
    nombre   = input("Nombre del producto: ")
    precio   = pedir_precio()
    cantidad = pedir_cantidad()
 
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"\nProducto '{nombre}' agregado.\n")

# Muestra todos los productos del inventario
def mostrar_inventario():
    print("\n--- Inventario ---")
    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()
 
# Muestra el total de productos y el valor total del inventario
def calcular_estadisticas():
    print("\n--- Estadísticas ---")
    if len(inventario) == 0:
        print("No hay productos registrados.\n")
    else:
        valor_total = 0
        for producto in inventario:
            valor_total += producto["precio"] * producto["cantidad"]
        print(f"Total de productos: {len(inventario)}")
        print(f"Valor total del inventario: {valor_total:.2f}\n")
 
# Muestra las opciones del menú y retorna la opción elegida
def mostrar_menu():
    print("=============================")
    print("  MENÚ - GESTIÓN INVENTARIO  ")
    print("=============================")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("-----------------------------")
    return input("Seleccione una opción: ")
 
# --- PROGRAMA PRINCIPAL ---
# El menú se repite hasta que el usuario elija salir
ejecutando = True
while ejecutando:
    opcion = mostrar_menu()
 
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("\n¡Hasta luego!\n")
        ejecutando = False
    else:
        print("\nOpción inválida. Ingrese un número del 1 al 4.\n")
 
# Objetivo: gestionar un inventario con menú interactivo,
# validación de datos y estadísticas usando listas y diccionarios.