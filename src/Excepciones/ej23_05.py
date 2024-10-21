"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene,
lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""
def introducir_password(mensaje):
    password = input(mensaje)
    return password

def comparar_password(password1: str, password2: str):
    while password1 != password2:


def main():
    password1 = "programacion"
    password2 = introducir_password("Introduzca la contraseña: ")


if __name__ == '__main__':
    main()