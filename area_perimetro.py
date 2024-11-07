#un programa que me permita calcular el área y perímetro de un triángulo equilátero.
opc=int(input("Ingresa 1 para Calcular la área, o pulsa 2 para calcular el Perímetro:\n"))
if (opc == 1):
    base=float(input("Ingresa la medida de la base:\n"))
    altura = float(input("Ingresa la medida de la altura:\n"))
    area= base*altura/2
    print(f"La área del triángulo es: {area:.2f}\n")
elif (opc == 2):
    lado=float(input("Ingresa la medida del  lado:\n"))
    perime=3*lado
    print(f"El perímetro es: {perime:.2f}\n")