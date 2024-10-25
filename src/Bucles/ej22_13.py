"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.
"""
assist = False
while not assist:
    eco = input("Introduce una palabra: ")
    if eco.lower() == "salir":
        assist = True
    else:
        print(eco)