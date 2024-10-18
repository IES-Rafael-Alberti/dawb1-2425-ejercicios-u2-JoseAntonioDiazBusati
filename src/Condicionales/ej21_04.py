"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
from src.Condicionales.ej21_03 import introducir_numero

def comprobar_par_impar(num: int):
    if num % 2 == 0:
        print("Este numero es par.")
    else:
        print("Este numero es impar.")

def main():
    num = introducir_numero()
    comprobar_par_impar(num)

if __name__ == '__main__':
    main()