"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
def pedir_float(mensaje):
    num = float(input(mensaje))
    return num

def pedir_int(mensaje):
    num = int(input(mensaje))
    return num

def calcular_capital(num_anios:int, inversion:float, intereses:float):
    res = ""
    for i in range(1,num_anios+1):
        inversion *= (1 + intereses/100)
        res += f"Año {i} => {inversion:.2f}\n"
    return res

def main():
    inversion = pedir_float("Introduce la cantidad a invertir: ")
    intereses = pedir_float("Introduce el interes anual: ")
    num_anios = pedir_int("Introduce el numero de años: ")
    print(calcular_capital(num_anios, inversion, intereses))


if __name__ == '__main__':
    main()