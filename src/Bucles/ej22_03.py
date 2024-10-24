"""
Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
from src.Excepciones.ej23_02 import pedir_num, mostrar_impares


def main():
    num = pedir_num("Introduce un numero entero: ")
    mostrar_impares(num)

if __name__ == "__main__":
    main()