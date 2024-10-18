"""
En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel 	        Puntuación
Inaceptable 	0.0
Aceptable 	    0.4
Meritorio 	    0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
así como la cantidad de dinero que recibirá el usuario.
"""

def introducir_rendimiento(mensaje: str)-> str:
    rendimiento = input(mensaje)
    return rendimiento

def puntuacion(rendimiento: str)-> float:
    if rendimiento.lower() == "inaceptable":
        return 0.0 * 2400.0
    elif rendimiento.lower() == "aceptable":
        return 0.4 * 2400.0
    elif rendimiento.lower() == "meritorio":
        return 0.6 * 2400.0

def main():
    rendimiento = introducir_rendimiento("Introduce su nivel de rendimiento: ")
    print(puntuacion(rendimiento),rendimiento)

if __name__ == "__main__":
    main()