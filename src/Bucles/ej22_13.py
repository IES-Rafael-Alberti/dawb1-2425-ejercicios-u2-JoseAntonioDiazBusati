"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.
"""
def pedir_eco(mensaje):
    eco = input(mensaje)
    return eco

def main():
    assist = False
    while not assist:
        eco = pedir_eco("Introduce una palabra: ")
        if eco.lower() == "salir":
            assist = True
        else:
            print(eco)

if __name__ == '__main__':
    main()