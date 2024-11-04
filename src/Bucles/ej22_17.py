"""
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
"""
def pedir_numero(mensaje):
    num = int(input(mensaje))
    return num

def suma_digitos(cont: int):
    suma = 0
    while cont > 0:
        suma += cont % 10
        cont //= 10
    return suma

def bucle(assist: bool, cont: int):
    while not assist:
        num = pedir_numero("Introduce un numero: ")
        if num == 0:
            suma = suma_digitos(cont)
            print("El mayor de esos numeros es:",cont,"\nY la suma de sus dígitos es:",suma)
            assist = True
        elif num > 0:
            if num > cont:
                cont = num
        else:
            print("Introduce numeros positivos!!!")

def main():
    cont = 0
    assist = False
    bucle(assist, cont)

if __name__ == "__main__":
    main()