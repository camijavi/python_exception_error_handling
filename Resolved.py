from Components import clearConsole

def ageConversion():
    clearConsole()
    print("--- CONVERSIÓN DE EDAD ---")
    try:
        while True:
            try:
                age = int(input("Ingrese su edad: "))
            except ValueError:
                print("ERROR: debe ingresar un número entero. Intente nuevamente.\n")
            else:
                print(f"\nCORRECTO: Su edad es {age}")
                break
    finally:
        print("Operación finalizada")
            


def secureDivision():
    clearConsole()
    print("--- DIVISIÓN SEGURA ---")
    print("Ingrese los valores para realizar la división\n")

    try:
        while True:
            try:
                a = float(input("1er número: "))
                b = float(input("2do número: "))
                result = a / b
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            except ZeroDivisionError:
                print("ERROR: no se puede dividir un número entre 0. Intente nuevamente.\n")
            else:
                print(f"\nEl resultado es: {result}")
                break
    finally:
        print("Operación finalizada")
       


def accessToAList():
    clearConsole()
    print("--- ACCESO A UNA LISTA ---")

    myDogsNames= ["Jack", "Cocoa", "Max", "Ted","Robin","Summer","Negrita","Chelincita","Otto"]

    print(myDogsNames)
    while True:
        try:
            position = int(input("Ingrese la posición a la cuál desea acceder: "))
            print(myDogsNames[position])
            break
        except ValueError:
             print("ERROR: debe ingresar un numéro entero. Intente nuevamente.\n")
        except IndexError:
             print("ERROR: la posición ingresada no existe. Intente nuevamente.\n")
    
def customerInquiry():
    clearConsole()
    print("--- CONSULTA DE CLIENTE ---")

    dictionary = {
        "nombre": "Roberto",
        "telefono": "1423-1234"
    }

    print(f"Campos disponibles: {list(dictionary.keys())}\n")

    while True:
        try:
            key = input("Dato a consultar: ").strip().lower()
            print(f"\n{key.capitalize()}: {dictionary[key]}")
            break
        except KeyError:
            print("ERROR: la clave ingresada no existe en el registro. Intente nuevamente.\n")



def guaranteedClosure():
    clearConsole()
    print("--- CIERRE GARANTIZADO ---")
    print("Operación: división de 100 entre un divisor\n")

    try:
        while True:
            try:
                numero = int(input("Ingrese un número entero: "))
                resultado = 100 / numero
            except ValueError:
                print("ERROR: Debe ingresar un número entero. Intente nuevamente.\n")
            except ZeroDivisionError:
                print("ERROR: No se puede dividir entre cero. Intente nuevamente.\n")
            else:
                print(f"\nResultado: 100 / {numero} = {resultado}")
                break
    finally:
        print("\nProceso finalizado.")


