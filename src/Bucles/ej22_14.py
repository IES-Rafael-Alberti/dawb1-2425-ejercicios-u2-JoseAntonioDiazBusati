"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números ingresados.
"""

def pedir_numero(mensaje):
    num = int(input(mensaje))
    return num

def main():
    cont = 0
    assist = False
    while not assist:
        num = pedir_numero("Introduce un numero: ")
        if num == 0:
            print("El sumatorio de esos numeros es:",cont)
            assist = True
        else:
            cont += num

if __name__ == "__main__":
    main()