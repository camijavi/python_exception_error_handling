from Components import (clearConsole, menuFooter)

def drawHeader(title):
    print("=" * 55)
    print(f"{title.center(55)}")
    print("=" * 55)


def showMainMenu():
    clearConsole()
    drawHeader("SISTEMA DE EJERCICIOS: MANEJO DE EXCEPCIONES")
    print(" [1] Ejercicios Resueltos")
    print(" [2] Ejercicios de Entradas")
    print(" [3] Ejercicios de Operaciones")
    print(" [4] Ejercicios de Estructuras")
    print(" [5] Ejercicios de Recursos")
    print(" [0] Salir")
    print("-" * 55)
    return input("Seleccione una opción: ").strip()


def showResolvedMenu():
    clearConsole()
    drawHeader("EJERCICIOS: RESUELTOS (MEJORADOS)")
    print(" [1] Conversión de edad")
    print(" [2] División segura")
    print(" [3] Acceso a una lista")
    print(" [4] Consulta de cliente")
    print(" [5] Cierre garantizado")
    return menuFooter()
    
def showTicketsMenu():
    clearConsole()
    drawHeader("EJERCICIOS: ENTRADAS")
    print(" [1] Precio de un producto")
    print(" [2] Cantidad de productos")
    print(" [3] Calificación")
    print(" [4] Edad para registro")
    print(" [5] Tres entradas consecutivas")
    return menuFooter()

def showOperationsMenu():
    clearConsole()
    drawHeader("EJERCICIOS: OPERACIONES")
    print(" [1] Promedio de ventas")
    print(" [2] Descuento proporcional")
    print(" [3] Conversión de moneda")
    print(" [4] Tipos incompatibles")
    print(" [5] Cálculo de comisión")
    return menuFooter()

def showStructuresMenu():
    clearConsole()
    drawHeader("EJERCICIOS: ESTRUCTURAS")
    print(" [1] Índice de inventario")
    print(" [2] Diccionario de empleados")
    print(" [3] Menú de opciones")
    return menuFooter()

def showResourcesMenu():
    clearConsole()
    drawHeader("EJERCICIOS: RECURSOS")
    print(" [1] Archivo de reportes")
    print(" [2] Importación controlada")
    return menuFooter()