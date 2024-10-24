"""
Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""
from src.Excepciones.ej23_02 import pedir_num


def hacer_piramide(num: int):
    piramide = "*"
    serie = ""
    for i in range(num):
        serie = serie + piramide
        print(serie)

def main():
    num = pedir_num("Introduce un numero para hacer una piramide: ")
    if num is not None:
        hacer_piramide(num)

if __name__ == "__main__":
    main()