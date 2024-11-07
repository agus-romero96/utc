def sumar(n1,n2):
    return n1+n2

def restar(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1//n2

n1=int(input("Ingresa el primer número\n"))
n2=int(input("Ingresa el segundo número\n"))
print(f"La suma es: {sumar(n1,n2)}")
print(f"La resta es: {restar(n1,n2)}")
print(f"La multiplicación es: {multiplicar(n1,n2)}")
print(f"La divición es: {dividir(n1,n2)}")