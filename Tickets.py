from Components import clearConsole

def productPrice():
    clearConsole()
    print("--- PRECIO DE UN PRODUCTO---")
    try:
        while True:
            try:
                productPrice = float(input("Ingrese el precio del producto: "))
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            else:
                print(f"El precio es: ${productPrice:.2f}")
                break
    finally:
        print("programa finalizado")


def productsQty():
    clearConsole()
    print("--- CANTIDAD DE PRODUCTOS ---")
    try:
        while True:
            try:
                qty = int(input("Ingrese la cantidad de unidades que desea comprar: "))
            except ValueError:
                print("ERROR: debe ingresar un número entero. Intente nuevamente.\n")
            else:
                print(f"La cantidad de unidades a comprar es: {qty}")
                break
    finally:
        print("programa finalizado")

def grades():
    clearConsole()
    print("--- CALIFICACIÓN ---")
    try:
        while True:
            try:
                grade = float(input("Ingrese la calificación: "))
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            else:
                print(f"La calificación es: {grade}")
                break
    finally:
        print("programa finalizado")

def ageRegistration():
    clearConsole()
    print("--- EDAD PARA REGISTRO ---")
    try:
        age = int(input("Ingrese su edad: "))
    except ValueError:
        print("ERROR: debe ingresar un número entero.")
    else:
        print(f"Su edad es: {age}")
    finally:
        print("programa finalizado")

def threeConsecutiveEntries():
    clearConsole()
    print("--- Tres entradas consecutivas (En desarrollo) ---")
    print("Ingrese los datos solicitados: ")

    while True:
        name = input("Nombre: ").strip()
        if name:
            break
        print("ERROR: El nombre no puede estar vacío. Intente de nuevo.\n")

    
    while True:
        try:
            age = int(input("Edad: "))
            break
        except ValueError:
             print("ERROR: La EDAD debe ser un número entero. Intente de nuevo.\n")
             
    while True:
        try:
            monthlyIncomes = float(input("Salario: $ "))
            break
        except ValueError:
             print("ERROR: El SALARIO debe ser un número. Intente de nuevo.\n")
    
    print(f"\nDatos registrados: {name}, {age} años, Salario: ${monthlyIncomes:.2f}")





