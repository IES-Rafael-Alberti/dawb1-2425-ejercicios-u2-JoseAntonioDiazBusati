"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores
a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y
muestre por pantalla si el usuario tiene que tributar o no.
"""
from src.Condicionales.ej21_01 import comprobar_edad


def preguntar_ingresos():
    return float(input("Ingrese los ingresos mensuales que posea: "))

def es_mayor(edad: int)-> bool:
    if edad > 16:
        return True
    else:
        return False

def comprobar_ingresos(ingreso: float)-> bool:
    if ingreso >= 1000.0:
        return True
    else:
        return False

def main():
    edad = comprobar_edad()
    ingreso = preguntar_ingresos()
    if comprobar_ingresos(ingreso) and es_mayor(edad) == True:
        print("\nPuedes tributar.")
    else:
        print("\nNo puedes tributar.")

if __name__ == "__main__":
    main()