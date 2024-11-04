"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€
y si es mayor de 18 años, 10€.
"""

def pedir_edad(mensaje:str):
    edad = int(input(mensaje))
    return edad

def comprobar_edad(edad:int):
    if edad > 18:
        return "Debes pagar 10€"
    elif edad < 18 or edad > 4:
        return "Debes pagar 5€"
    elif edad < 4:
        return "Es gratis puedes pasar"

def main():
    edad = pedir_edad("Introduce su edad para entrar: ")
    print(comprobar_edad(edad))

if __name__ == '__main__':
    main()