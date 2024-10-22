"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene,
lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""
def introducir_password():
    password1 = "programacion"
    password2 = None
    while password2 is None:
        try:
            password2 = input("Introduce la contraseña: ")
            comprobar_password(password1, password2)
        except NameError:
            if password2 is None:
                print("Incorrect Password!!!!!!")
            else:
                password2 = None
                print("Incorrect Password!!!")

    return password2

def comprobar_password(password1: str, password2: str):
    if password1.lower() == password2.lower():
        return "Bienvenido Usuario"
    else:
        raise NameError("Incorrect Password!!!")


def main():
    print(introducir_password())


if __name__ == '__main__':
    main()