"""
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide,
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
"""
def pedir_frase(mensaje):
    frase = input(mensaje)
    return frase

def pedir_letra(mensaje):
    letra = input(mensaje)
    return letra

def buscar_coincidencia(frase,letra):
    assist = False
    while not assist:
        for posicion, caracter in enumerate(frase):
            if caracter == letra:
                print("Coincidencia encontrada en la posición",posicion)
                assist = True
            else:
                print("No hay coincidencia en la posición",posicion)
        else:
            print("No se encontró la letra en la frase.")

def main():
    frase = pedir_frase("Introduce una frase: ")
    letra = pedir_letra("Introduce una letra: ")
    buscar_coincidencia(frase,letra)

if __name__ == "__main__":
    main()