"""
Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
Deberá solicitar el número hasta introducir uno correcto.
"""

from src.Excepciones.ej23_02 import pedir_num

def cuenta_atras(num: int):
    serie = ""
    for i in range(0, num + 1):
        serie = serie + str(i) + ", "
    print(serie)

def main():
    num = pedir_num("Introduce un numero entero positivo: ")
    if num is not None:
        cuenta_atras(num)

if __name__ == "__main__":
    main()