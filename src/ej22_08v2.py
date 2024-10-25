
def validar_numero(num: int):
    if num < 0:
        raise ValueError

def pedir_numero(mensaje):
    try:
        num = int(input(mensaje))
        validar_numero(num)
        return num
    except ValueError:
        print("Valor no valido!!!")


def par_impar(num: int):
    if num % 2 == 0:
        inicio = 0
    else:
        inicio = 1
    return inicio


def bucle(num: int,serie: str, serie_total: str,inicio: int):
    for i in range(inicio, num + 1, 2):
        serie = str(i) + " " + serie
        serie_total += serie + "\n"
    return serie_total

def main():
    serie = ""
    serie_total = ""
    num = pedir_numero("Introduce un numero: ")
    if num is not None:
        inicio = par_impar(num)
        print(bucle(num,serie,serie_total,inicio))


if __name__ == "__main__":
    main()