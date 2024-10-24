"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
from src.Condicionales.ej21_02 import introducir_password, comprobar_password

def main():
    contrasena = "Diegooool"
    password = introducir_password()
    comprobar_password(password, contrasena)

if __name__ == "__main__":
    main()