from Components import clearConsole

def averageSales():
    clearConsole()
    print("--- PROMEDIO DE VENTAS ---")
    print("Ingrese los valores de las ventas")

    try:
        while True:
            try:
                sale1 = float(input("Venta (1)"))
                sale2 = float(input("Venta (2)"))
                sale3= float(input("Venta (3)"))

                sales = [sale1, sale2, sale3]
                count = len(sales)

                average = sum (sales) / count
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            except ZeroDivisionError:
                print("ERROR: no se puede dividir por cero.")
            else:
                print(f"El promedio de las ventas es: ${average:.2f}")
                break
    finally:
        print("programa finalizado")


def proportionalDiscount():
    clearConsole()
    print("--- DESCUENTO PROPORCIONAL ---")
    try:
        while True:
            try:
                amount = float(input("Ingrese el monto: $"))
                base = float(input("Ingrese la base: $"))
                
                percentage = (amount / base) * 100
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            except ZeroDivisionError:
                print("ERROR: la base no puede ser igual a cero. Intente nuevamente.\n")
            else:
                print(f"El porcentaje correspondiente es: {percentage:.2f}%")
                break
    finally:
        print("programa finalizado")


def currencyConversion():
    clearConsole()
    print("--- CONVERSIÓN DE MONEDA ---")
    try:
        while True:
            try:
                amount = float(input("Ingrese el monto: $"))
                exchangeRate = float(input("Ingrese la tasa de cambio: "))
                
                result = amount / exchangeRate
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            except ZeroDivisionError:
                print("ERROR: la tasa de cambio no puede ser igual a cero. Intente nuevamente.\n")
            else:
                print(f"El valor es : {result:.2f}")
                break
    finally:
        print("programa finalizado")



def incompatibleTypes():
    clearConsole()
    print("--- TIPOS INCOMPATIBLES ---")
    try:
        while True:
            try:
                num1 = float(input("Ingrese un valor: "))
                num2 = float(input("Ingrese otro valor: "))
                result = num1 + num2
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            else:
                print(f"El resultado es: {result}")
                break
    finally:
        print("programa finalizado")

def commissionCalculator():
    clearConsole()
    print("--- CÁLCULO DE COMISIÓN ---")
    try:
        while True:
            try:
                sales = float(input("Ingrese el total de ventas: $"))
                percentage = float(input("Ingrese el porcentaje de comisión: %"))
                
                result = sales * (percentage / 100)
            except ValueError:
                print("ERROR: debe ingresar un valor numérico. Intente nuevamente.\n")
            else:
                print(f"El resultado es: {result:.2f}")
                break
    finally:
        print("programa finalizado")


