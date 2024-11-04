"""
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra
más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había.
Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""


def pedir_frase(mensaje):
    frase = input(mensaje)
    return frase.split(" ")


def devolver_palabras(frase: list[str]):
    larger = ""
    num_palabra = 0
    for palabra in frase:
        if len(palabra) > len(larger):
            larger = palabra
        num_palabra += 1
    return larger, num_palabra


def main():
    frase = pedir_frase("Introduce una frase: ")
    larger, num_palabra = devolver_palabras(frase)
    print(f"La palabra más larga es: {larger}\nLa frase tiene {num_palabra} palabras.")


if __name__ == "__main__":
    main()