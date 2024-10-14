"""
Actividad 1: Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra
cosa que no sea un número, (mas adelante veremos como detectar los fallos usando try y except)

Introduzca un número: 4
Introduzca un número: 5
Introduzca un número: dato erróneo
Entrada inválida
Introduzca un número: 7
Introduzca un número: fin
16 3 5.33333333333
"""

def pedir_dato():
    return input("Introduce un número: ")

def bucle():
    assist = False
    cont = 0
    total = 0
    while not assist:
        num = pedir_dato()
        if num.isdigit():
            total = total + int(num)
            cont += 1
        elif num.lower() == "fin":
            assist = True
        else:
            print("\nEntrada inválida!!!\n")
    media = total / cont
    return total, cont, media

def main():
    ejemplo = bucle()
    print(ejemplo)

if __name__ == '__main__':
    main()