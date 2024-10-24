"""
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def validar_num(num: int):
    if num < 0:
        raise ValueError("No puede ser negativa!!!")
    if num == 0:
        raise ValueError("No puede ser 0!!!")

def pedir_num(mensaje):
    num = None
    while num is None:
        try:
            num = int(input(mensaje))
            validar_num(num)
        except ValueError as e:
            if num is None:
                print("El numero introducido no es valido!!!")
            else:
                num = None
                print(f"**ERROR**\n{e}\nValor invalido!!!")
    return num

def mostrar_impares(num: int):
    serie = ""
    for i in range(1,num+1,2):
        serie = serie+str(i)+", "
    print(serie)

def main():
    num = pedir_num("Introduce un numero entero positivo: ")
    if num is not None:
        mostrar_impares(num)

if __name__ == '__main__':
    main()