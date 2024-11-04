"""
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa.
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta,
informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción,
permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto.
Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""
def pedir_opcion(mensaje):
    opcion = int(input(mensaje))
    return opcion

def menu():
    assist = False
    while not assist:
        print("-------------------------------")
        print("|Elije una de estas opciones: |")
        print("| 1. Comenzar programa        |")
        print("| 2. Imprimir listado         |")
        print("| 3. Finalizar programa       |")
        print("-------------------------------")
        opcion = pedir_opcion("")
        if opcion == 1:
            print("Mucho texto\n\n\n")
        elif opcion == 2:
            print("Extenso texto\n\n\n")
        elif opcion == 3:
            assist = True
        else:
            print("No puedes elegir opciones inexistentes!!!")

def main():
    menu()

if __name__ == '__main__':
    main()