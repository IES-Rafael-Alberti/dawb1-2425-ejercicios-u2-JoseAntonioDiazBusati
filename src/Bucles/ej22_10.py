"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""
def pedirnum()-> int:
    num = int(input("Introduce un numero: "))
    return num

def comprobar_primo(num : int):
    assist = False
    div = 2
    while not assist:
        resto = num%div
        if div == num:
            print("El numero es primo")
            assist = True
        elif num == 1 or num == 0:
            print("El numero no es primo")
            assist = True
        elif num < 0:
            print("El numero no puede ser primo")
            assist = True
        elif resto != 0 :
            div += 1
        else:
            print("El numero no es primo")
            assist = True

def main():
    num = pedirnum()
    comprobar_primo(num)

if __name__ == "__main__":
    main()