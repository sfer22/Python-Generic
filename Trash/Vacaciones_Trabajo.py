
nombre = input("Por favor digite su nombre: ")
print("")
print("Bienvenido", nombre)
print("")
getDecision = int(input("Por favor seleccione una opción:\n\n"
                        "1- Trabajar\n"
                        "2- Ir de vacaciones\n\n"
                        "Selección: "))

while getDecision < 1 or getDecision > 2:
    getDecision = int(input("\nERROR!!! "
                            "Por favor seleccione una opcion valida: \n\n"
                            "1- Trabajar\n"
                            "2- Ir de vacaciones\n\n"
                            "Selección: "))

if getDecision == 1:
    print("")
    print("***** Ha seleccionado Trabajar, escoja un cafe *****\n")
    getCafe = int(input("Estos son los cafes disponibles: \n\n"
                        "#    Cafe        Precio\n\n"
                        "1-   Mocca        1300\n"
                        "2-   Capuccino    1200\n"
                        "3-   Latte        900\n"
                        "4-   Americano    700\n\n"
                        "Selección: "))

    while getCafe < 1 or getCafe > 4:
        getCafe = int(input("ERROR!!! "
                            "Por favor seleccione una opcion valida: \n\n"
                            "#    Cafe        Precio\n\n"
                            "1-   Mocca        1300\n"
                            "2-   Capuccino    1200\n"
                            "3-   Latte        900\n"
                            "4-   Americano    700\n\n"
                            "Selección: "))

    if getCafe == 1:
        print("Ha seleccionado, Mocca, el monto a pagar es de 1300")

    elif getCafe == 2:
        print("Ha seleccionado, Capuccino, el monto a pagar es de 1200")

    elif getCafe == 3:
        print("Ha seleccionado, Latte, el monto a pagar es de 900")

    elif getCafe == 4:
        print("Ha seleccionado, Americano, el monto a pagar es de 700")

    print("Muchas gracias por su compra!!!")

elif getDecision == 2:
    print("***** Excelente ha decidido ir de viaje *****")
    getDestino = int(input("Estos son los destinos disponibles: \n\n"
                           "#    Destino\n\n"
                           "1-   Japón\n"
                           "2-   Rusia\n"
                           "3-   Brasil\n"
                           "4-   Inglaterra\n\n"
                           "Selección: "))

    while getDestino < 1 or getDestino > 4:
        getDestino = int(input("ERROR!!! "
                               "Por favor seleccione una opcion valida: \n\n"
                               "#    Destino\n\n"
                               "1-   Japón\n"
                               "2-   Rusia\n"
                               "3-   Brasil\n"
                               "4-   Inglaterra\n\n"
                               "Selección: "))

    if getDestino == 1:
        print("Ha seleccionado viajar a Japón, el monto a pagar es de 1.000.000")

    elif getDestino == 2:
        print("Ha seleccionado viajar a Rusia, el monto a pagar es de 800.000")

    elif getDestino == 3:
        print("Ha seleccionado viajar a Brasil, el monto a pagar es de 400.000")

    elif getDestino == 4:
        print("Ha seleccionado viajar a Inglaterra, el monto a pagar es de 600.000")

    print("")
    print("Buen viaje!!!")
