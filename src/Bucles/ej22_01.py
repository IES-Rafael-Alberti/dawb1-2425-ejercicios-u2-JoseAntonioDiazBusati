"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def pedir_palabra(mensaje)-> str:
    palabra = input(mensaje)
    return palabra

def main():
    palabra = pedir_palabra("Introduce una palabra: ")
    for i in range(10):
        print(palabra)

if __name__ == '__main__':
    main()