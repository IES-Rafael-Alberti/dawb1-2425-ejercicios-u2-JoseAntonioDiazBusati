"""
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0.
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar
la cantidad de dígitos pares y de dígitos impares leídos en total.
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
            print("Cantidad de números pares ingresados:",cont)
            assist = True
        elif num > 0:
            suma = suma_digitos(num)
            print("La suma de los dígitos de",num,"es:",suma)
            if num % 2 != 0:
                cont += 1
        else:
            print("Introduce numeros positivos!!!")

def main():
    cont = 0
    assist = False
    bucle(assist, cont)

if __name__ == "__main__":
    main()