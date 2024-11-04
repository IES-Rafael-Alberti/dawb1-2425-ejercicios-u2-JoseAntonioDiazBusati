"""
Escribir un programa que pregunte al usuario su edad y muestre por
pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
from src.Excepciones.ej23_01 import pedir_edad

def mostrar_anios(edad: int):
    for i in range(1, edad+1):
        print(i)

def main():
    edad = pedir_edad()
    mostrar_anios(edad)

if __name__ == '__main__':
    main()