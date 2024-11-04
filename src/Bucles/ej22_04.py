"""
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
from src.Excepciones.ej23_02 import pedir_num
from src.Excepciones.ej23_03 import cuenta_atras


def main():
    num = pedir_num("Introduce un numero entero positivo: ")
    if num is not None:
        cuenta_atras(num)

if __name__ == "__main__":
    main()