"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0.
Informar cuál fue el mayor número ingresado.
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
            print("El mayor de esos numeros es:",cont)
            assist = True
        elif num > 0:
            if num > cont:
                cont = num
        else:
            print("Introduce numeros positivos!!!")

if __name__ == "__main__":
    main()