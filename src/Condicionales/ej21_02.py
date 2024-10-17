"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def introducir_password()-> str:
    password = input("Introduce la contraseña: ")
    return password


def comprobar_password(password: str, contrasena: str)-> bool:
    assist = False
    while not assist:
        if password.lower() != contrasena.lower():
            print("La contraseña introducida es incorrecta!!!\n")
            introducir_password()
        else:
            print("Contraseña correcta!!!\n\nBienvenido usuario.")
            assist = True
    return True


def main():
    contrasena = "programacion"
    password = introducir_password()
    comprobar_password(password, contrasena)

if __name__ == "__main__":
    main()