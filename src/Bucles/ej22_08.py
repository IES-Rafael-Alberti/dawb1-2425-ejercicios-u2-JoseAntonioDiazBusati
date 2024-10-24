"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""
from src.Excepciones.ej23_02 import pedir_num


def hacer_piramide_num(num: int):
    serie = ""
    for i in range(1,num + 1,2):
        serie = serie + str(i)+ " "
        print(serie)

def main():
    num = pedir_num("Introduce un numero para hacer una piramide: ")
    if num is not None:
        hacer_piramide_num(num)

if __name__ == "__main__":
    main()