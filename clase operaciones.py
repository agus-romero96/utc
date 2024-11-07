# operaciones básicas en una clase usando init
class Operaciones:
    def __init__(self):
        self.n1=int(input("Ingrese primer valor:\n"))
        self.n2=int(input("Ingrese segundo valor:\n"))

    def sumar(self):
        return self.n1+self.n2

    def restar(self):
        return self.n1-self.n2

    def multiplicar(self):
        return self.n1*self.n2

    def dividir(self):
        return self.n1//self.n2

# función principal
ope =Operaciones()
print(f"la suma es: {ope.sumar()}\n")
print(f"la resta es: {ope.restar()}\n")
print(f"la multiplicación es: {ope.multiplicar()}\n")
print(f"la división es: {ope.dividir()}\n")