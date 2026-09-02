from Components import clearConsole

def inventoryIndex(): 
    print("--- ÍNDICE DE UN INVENTARIO ---")
    products = ["Zapatillas","Faja","Vestido","Camisa","Falda jeans","Jeans acampanado"]

    print(products)
    while True:
        try:
            position = int(input("Ingrese la posición a la cuál desea acceder: "))
            print(products[position])
            break
        except ValueError:
             print("ERROR: debe ingresar un numéro entero. Intente nuevamente.\n")
        except IndexError:
             print("ERROR: la posición ingresada no existe. Intente nuevamente.\n")


def employeeDictionary():
    clearConsole()
    # Consulta información de un empleado mediante una clave.
    # Controla KeyError y considera si get() podría ser una alternativa.
    print("--- DICCIONARIO DE EMPLEADOS ---")

    employees = {
        "nombre": "Alice Smith", 
        "correo": "alice.smith@company.com", 
        "cargo": "CEO", 
        "gerente": None, 
        "salario": 250000, 
        "activo": True
    }


    print(f"Campos disponibles: {list(employees.keys())}\n")

    while True:
        try:
            key = input("Dato a consultar: ").strip().lower()
            print(f"\n{key.capitalize()}: {employees[key]}")
            break
        except KeyError:
            print("ERROR: la clave ingresada no existe en el registro. Intente nuevamente.\n")

def optionsMenu():
    clearConsole()
    print("--- MENÚ DE OPCIONES ---")
    print("1. Ver perfil")
    print("2. Configuración")
    print("3. Salir\n")

    try:
        while True:
            try:
                option = int(input("Seleccione una opción (1-3): "))
            except ValueError:
                print("ERROR: Debe ingresar un número entero. Intente nuevamente.\n")
            else:
                while True:
                    match option:
                        case 1:
                            print("\n[Opción 1] Cargando el perfil de usuario...")
                            break
                        case 2:
                            print("\n[Opción 2] Abriendo panel de configuración...")
                            break
                        case 3:
                            print("\n[Opción 3] Saliendo del sistema...")
                            break
                        case _:
                            print("\nOpción fuera de rango (debe ser 1, 2 o 3).")
                            break
    finally:
        print("Programa finalizado.")


