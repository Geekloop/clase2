import os, sys
n = int(input("Ingrese la cantidad de cauchos a comprar: "))
p = float(input("Ingrese el precio unitario: "))
if n > 6:
    desc = 0.15 * p
else:
    desc = 0.1 * p

tot = p - desc
total = n*tot
print("El total a pagar es: " ,total)