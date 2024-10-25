"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
palabra = input("Introduce palabra: ")
letra = input("Introduce la letra: ")
cont = 0
for letras in palabra:
    if letras == letra:
        cont += 1
print("Aparece la letra",letra,"en la frase",cont,"veces")