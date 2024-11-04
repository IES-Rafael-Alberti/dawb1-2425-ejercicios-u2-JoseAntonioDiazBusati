"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""

def introducir_numero():
    return int(input("Introduce un numero cualquiera: "))

def comprobar_divisible(num1: int,num2: int)-> bool:
    assist = False
    while not assist:
        if num2 == 0:
            print("***ERROR***\nNo se puede dividir por 0.")
            num2 = introducir_numero()
        else:
            print("El resultado de su division es:", num1 / num2)
            assist = True
    return True

def main():
    num1 = introducir_numero()
    num2 = introducir_numero()
    comprobar_divisible(num1,num2)

if __name__ == "__main__":
    main()