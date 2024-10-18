"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres
con un nombre posterior a la N y el grupo B por el resto. Escribir un programa
que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

def introducir_nombre(mensaje: str):
    nombre = input(mensaje)
    return nombre

def introducir_sexo(mensaje: str):
    sexo = input(mensaje)
    return sexo

def comprobar_grupo(nombre: str, sexo: str):
    return nombre

def main():
    nombre = introducir_nombre("Introduzca su nombre: ")
    sexo = introducir_sexo("Introduzca su sexo: ")

if __name__ == '__main__':
    main()