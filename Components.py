import os

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuFooter():
    print(" [0] Volver al Menú Principal")
    print("-" * 55)
    return input("Seleccione una opción: ").strip()

def invalidOptionMessage():
    print("\nOpción no válida. Intente de nuevo.")

def pause():
    input("\nPresione Enter para continuar...")

