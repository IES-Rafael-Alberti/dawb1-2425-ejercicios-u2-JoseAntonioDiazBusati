"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno,
imprimir la suma de los dígitos que lo componen. La condición de corte es que se
ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
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
        if num == -1:
            print("Cantidad de números pares ingresados:",cont)
            assist = True
        elif num > -1:
            suma = suma_digitos(num)
            print("La suma de los dígitos de",num,"es:",suma)
            if num % 2 == 0:
                cont += 1
        else:
            print("Introduce numeros positivos!!!")

def main():
    cont = 0
    assist = False
    bucle(assist, cont)

if __name__ == "__main__":
    main()