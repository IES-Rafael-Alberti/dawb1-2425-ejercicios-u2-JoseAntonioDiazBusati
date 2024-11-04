"""
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo,
no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar
el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se
le debe aplicar un 10% de descuento.
"""

def pedir_monto(mensaje:str):
    assist = False
    while not assist:
        monto = int(input(mensaje))
        if monto < 0:
            print("No puede ser negativo!!")
        elif monto == 0:
            print("No puede ser 0!!")
        else:
            assist = True
    return monto

def calcular_monto(monto:int):
    if monto > 1000:
        monto = monto-(monto * 0.1)
        return monto
    return monto


def main():
    monto = pedir_monto("Introduce el total de montos de compra: ")
    print(calcular_monto(monto))

if __name__ == "__main__":
    main()