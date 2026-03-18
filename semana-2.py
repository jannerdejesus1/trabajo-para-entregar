from funciones import *
# Sistema de gestión de inventario
inventario = []

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
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        calcular_estadisticas(inventario)
    elif opcion == "4":
        print("\n¡Hasta luego!\n")
        ejecutando = False
    else:
        print("\nOpción inválida. Ingrese un número del 1 al 4.\n")
 
# Objetivo: gestionar un inventario con menú interactivo,
# validación de datos y estadísticas usando listas y diccionarios.