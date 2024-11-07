#hacer un programa que me permita transformar de grados a radianes.
import math

grados=float(input("Ingresa los grados que deseas convertir a radianes:\n"))

radianes=grados*math.pi/180
print(f"Los grados {grados} equivalen a {radianes:.2f} radianes.\n")
print("Usando otra forma:\n")
radianes = math.radians(grados)
print(f"{grados} grados es igual a {radianes} radianes")