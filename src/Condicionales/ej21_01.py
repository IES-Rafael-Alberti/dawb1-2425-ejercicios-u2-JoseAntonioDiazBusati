"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
def introducir_edad():
    return int(input("Ingrese su edad: "))

def comprobar_edad()-> int:
    age = introducir_edad()
    assist = False
    while not assist:
        if age < 0:
            print("Ingrese una edad realista!!!\n")
            age = introducir_edad()
        elif age > 120:
            print("Ingrese una edad realista!!!\n")
            age = introducir_edad()
        else:
            assist = True
    return age

def main():
    edad = comprobar_edad()
    if edad > 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

if __name__ == "__main__":
    main()
