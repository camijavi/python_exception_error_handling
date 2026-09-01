from Components import (clearConsole, menuFooter)

def drawHeader(title):
    print("=" * 55)
    print(f"{title.center(55)}")
    print("=" * 55)


def showMainMenu():
    clearConsole()
    drawHeader("SISTEMA DE EJERCICIOS CONDICIONALES")
    print(" [1] Ejercicios con 'If Simples'")
    print(" [2] Ejercicios con 'If Anidados'")
    print(" [0] Salir")
    print("-" * 55)
    return input("Seleccione una opción: ").strip()
