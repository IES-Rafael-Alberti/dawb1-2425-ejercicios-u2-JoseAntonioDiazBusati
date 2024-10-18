"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

    Renta 	             Tipo impositivo
Menos de 10000€ 	        5%
Entre 10000€ y 20000€ 	    15%
Entre 20000€ y 35000€ 	    20%
Entre 35000€ y 60000€ 	    30%
Más de 60000€ 	            45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
el tipo impositivo que le corresponde.
"""

def preguntar_renta(mensaje: str):
    renta = float(input(mensaje))
    return renta

def comparativo(renta: float):
    if renta < 10000.0:
        return "Te corresponde un 5% de impositivo."
    elif renta > 10000.0 or renta < 20000.0:
        return "Te corresponde un 15% de impositivo."
    elif renta > 20000.0 or renta < 35000.0:
        return "Te corresponde un 20% de impositivo."
    elif renta > 35000.0 or renta < 60000.0:
        return "Te corresponde un 30% de impositivo."
    else:
        return "Te corresponde un 45% de impositivo."

def main():
    renta = preguntar_renta("Introduzca su salario anual: ")
    print(comparativo(renta))

if __name__ == '__main__':
    main()