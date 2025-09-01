import math

def line():
    a=float(input("Ingrese el coeficiente A: "))
    b=float(input("Ingrese el coeficiente B: "))
    x1=float(input("Ingrese el coeficiente X1: "))
    x2=float(input("Ingrese el coeficiente X2: "))


    y1= a*x1+b
    y2= a*x2+b

    distancia=math.sqrt((x2-x1)**2+ (y2-y1)**2)

    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")


    print("\nPara la siguiente ecuación:")
    print(f"\tY = {a}X + {b}")

    print("\nDados los siguientes puntos:")
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})")

    print(f"\nLa distancia entre ellos es: {distancia}")

line()    
