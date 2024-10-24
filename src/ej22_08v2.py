
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



def par_impar(num: int,serie: str, serie_total: str):
    if num % 2 == 0:
        for i in range(0, num + 1, 2):
            serie = str(i)+ " " + serie
            serie_total += serie+"\n"
    else:
        for i in range(1, num + 1, 2):
            serie = str(i) + " " + serie
            serie_total += serie + "\n"
    return serie_total
#Cambiar bucle por par_impar :D
def bucle(num: int):
    if num % 2 == 0:
        inicio = 0
    else:
        inicio = 1
    return inicio

def main():
    serie = ""
    serie_total = ""
    num = pedir_numero("Introduce un numero: ")
    if num is not None:
        print(par_impar(num,serie,serie_total))


if __name__ == "__main__":
    main()