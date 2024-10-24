"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
def tablas_multiplicar():
    for i in range(1,11):
        print("\nTabla del",i,"\n")
        for j in range(1,11):
            print(i,"x",j,"=",i*j)

def main():
    tablas_multiplicar()

if __name__ == "__main__":
    main()