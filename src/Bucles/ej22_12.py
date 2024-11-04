"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
def pedir_palabra(mensaje):
    palabra = input(mensaje)
    return palabra

def pedir_letra(mensaje):
    letra = input(mensaje)
    return letra

def main():
    palabra = pedir_palabra("Introduce palabra: ")
    letra = pedir_letra("Introduce la letra: ")
    cont = 0
    for letras in palabra:
        if letras == letra:
            cont += 1
    print("Aparece la letra",letra,"en la frase",cont,"veces")

if __name__ == "__main__":
    main()