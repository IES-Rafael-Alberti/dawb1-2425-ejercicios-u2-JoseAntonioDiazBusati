"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta,
mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""

def pedir_entero()-> int:
    num = None
    while num is None:
        try:
            num = int(input("Introduce un numero entero: "))
            comprobar_entero(num)
        except ValueError:
            if num is None:
                print("La entrada no es correcta!!!")
            else:
                print("La entrada no es correcta!!!")

    return num

def comprobar_entero(num: int):
    if type(num) != int:
        raise ValueError("La entrada no es correcta")
    else:
        return num


def main():
    print(pedir_entero())

if __name__ == "__main__":
    main()