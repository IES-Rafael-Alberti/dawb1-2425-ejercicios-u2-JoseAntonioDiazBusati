"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
que ha cumplido (desde 1 hasta su edad).
"""

def validar_edad(edad: int):
    if edad < 0:
        raise ValueError("No puede ser negativa")
    if edad == 0:
        raise ValueError("No puede ser 0")
    if edad > 125:
        raise ValueError("No puede ser mayor que 125")



def pedir_edad() -> int:
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduzca su edad: "))
            validar_edad(edad)
        except ValueError as e:
            if edad is None:
                print("La edad introducida no es valida!!!")
            else:
                edad = None
                print(f"**ERROR**\n{e}\nValor invalido!!!")

    return edad

def mostrar_anios(edad: int):
    for i in range(1,edad+1):
        print(i)

def main():
    edad = pedir_edad()
    if edad is not None:
        mostrar_anios(edad)

if __name__ == '__main__':
    main()