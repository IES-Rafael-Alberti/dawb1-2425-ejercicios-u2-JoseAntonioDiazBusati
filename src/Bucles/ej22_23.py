"""
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando
el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese
un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea.
Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9)
aparecieron en total (en todos los títulos de libros que componen en esa línea).
Finalmente, informar cuántas líneas completas se ingresaron.

Ejemplo de ejecución:

Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
"""

def contar_digitos(libros:str, contador:int):
    for i in libros:
        if i.isdigit():
            contador+=1
    return contador

def pedir_libros(libros:str, contador:int):
    total_libros = 0
    while libros != "*":
        libros = input("Libro: ")
        if libros != "/":
            digitos = contar_digitos(libros, contador)
        elif libros == "/":
            print(f"Linea completa. Aparecen {digitos} digitos numericos.")
            total_libros +=1
    return f"Fin. Se leyeron {total_libros} lineas completas."

def main():
    contador = 0
    libros = ""
    print(pedir_libros(libros,contador))

if __name__ == '__main__':
    main()