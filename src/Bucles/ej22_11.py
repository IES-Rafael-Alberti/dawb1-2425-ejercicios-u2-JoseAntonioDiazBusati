"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una
a una las letras de la palabra introducida empezando por la última.
"""

def pedir_palabra(mensaje):
    word = input(mensaje)
    return word

def leer_reves(word: str):
    for palabra in word[::-1]:
        print(palabra)

def main():
    word = pedir_palabra("Introduce una palabra: ")
    leer_reves(word)

if __name__ == '__main__':
    main()