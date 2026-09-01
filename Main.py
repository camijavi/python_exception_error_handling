from Operations import (averageSales, proportionalDiscount, currencyConversion, incompatibleTypes, commissionCalculator)
from Tickets import (productPrice, productsQty, grades, ageRegistration, threeConsecutiveEntries)
from Stuctures import (inventoryIndex, employeeDictionary, optionsMenu)
from Resolved import (ageConversion, secureDivision, accessToAList, customerInquiry, guaranteedClosure)
from Resources import (reportArchive, controlledImport)

from UI import (showMainMenu, showResolvedMenu, showTicketsMenu, showOperationsMenu, showStructuresMenu, showResourcesMenu)
from Components import invalidOptionMessage, pause


def handleResolved():
    while True:
        option = showResolvedMenu()
        match option:
            case "1":
                print("\n" + ageRegistration())
            case "2":
                print("\n" + secureDivision())
            case "3":
                print("\n" + accessToAList())
            case "4":
                print("\n" + customerInquiry())
            case "5":
                print("\n" + guaranteedClosure())
            case "0":
                break
            case _:
                invalidOptionMessage()
        pause()


def handleTickets():
    while True:
        option = showTicketsMenu()
        match option:
            case "1":
                print("\n" + productPrice())
            case "2":
                print("\n" + productsQty())
            case "3":
                print("\n" + grades())
            case "4":
                print("\n" + ageRegistration())
            case "5":
                print("\n" + threeConsecutiveEntries())
            case "0":
                break
            case _:
                invalidOptionMessage()
        pause()

def handleOperations():
    while True:
        option = showOperationsMenu()
        match option:
            case "1":
                print("\n" + averageSales())
            case "2":
                print("\n" + proportionalDiscount())
            case "3":
                print("\n" + currencyConversion())
            case "4":
                print("\n" + incompatibleTypes())
            case "5":
                print("\n" + commissionCalculator())
            case "0":
                break
            case _:
                invalidOptionMessage()
        pause()

def handleStructures():
    while True:
        option = showResourcesMenu()
        match option:
            case "1":
                print("\n" + inventoryIndex())
            case "2":
                print("\n" + employeeDictionary())
            case "3":
                print("\n" + optionsMenu())
            case "0":
                break
            case _:
                invalidOptionMessage()
        pause()

def handleResources():
    while True:
        option = showResourcesMenu()
        match option:
            case "1":
                print("\n" + reportArchive())
            case "2":
                print("\n" + controlledImport())
            case "0":
                break
            case _:
                invalidOptionMessage()
        pause()

def main():
    while True:
        choice = showMainMenu()
        match choice:
            case "1":
                handleResolved()
            case "2":
                handleTickets()
            case "3":
                handleOperations()
            case "4":
                handleStructures()
            case "5":
                handleResources()
            case "0":
                print("\n¡Gracias por utilizar el sistema! Hasta luego.\n")
                break
            case _:
                invalidOptionMessage()
                pause()


if __name__ == "__main__":
    main()