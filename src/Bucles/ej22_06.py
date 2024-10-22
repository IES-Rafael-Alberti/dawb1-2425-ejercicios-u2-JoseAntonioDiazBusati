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
    for i in range(num):
        print(piramide)

def main():
    num = pedir_num("Introduce un numero para hacer una piramide: ")
    hacer_piramide(num)