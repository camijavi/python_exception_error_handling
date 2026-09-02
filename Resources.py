from Components import clearConsole

def reportArchive():
    clearConsole()
    print("--- Archivo de reportes ---")
    try:
        with open("reports.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: No se encontró el archivo de reportes (reports.txt).")
    finally:
        print("La operación de archivo terminó.")

def controlledImport():
    clearConsole()
    print("--- Importación controlada ---")
    
    try:
        # pyrefly: ignore [missing-import]
        import modulo_fantasma_inexistente
        
    except ModuleNotFoundError as error:
        print(f"❌ Ocurrió un error: {error}")
        print("\nSugerencias para la persona desarrolladora:")
        print("1. Verifica que el nombre del módulo esté escrito correctamente.")
        print("2. Asegúrate de que la librería esté instalada en tu sistema (ej. ejecutando 'pip install <nombre_del_modulo>').")
        print("3. Si estás usando un entorno virtual, confirma que esté activado.")
        print("4. Revisa si el archivo o paquete local se encuentra en el mismo directorio o en el PYTHONPATH.")



