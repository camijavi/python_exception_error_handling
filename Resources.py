from Components import clearConsole

def reportArchive():
    clearConsole()
    # Intenta abrir un archivo llamado reportes.txt.
    # Controla FileNotFoundError y utiliza finally para mostrar que la operación terminó.
    print("--- Archivo de reportes (En desarrollo) ---")

def controlledImport():
    clearConsole()
    # Simula la importación de un módulo que no existe y controla ModuleNotFoundError.
    # El mensaje debe explicar qué debe revisar la persona desarrolladora.
    print("--- Importación controlada (En desarrollo) ---")



