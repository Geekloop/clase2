#Realizar un programa que permita calcular el valor total que una persona debe
#pagar por la compra de Confort
c = int(input("Ingrese cantidad de confort: "))
p = float(input("Ingrese precio unitario: "))
p = c * p
if c > 0 and c <= 4:        #de 1 a 4 15%
    desc = 0.15 * p
elif c >= 5 and c <= 9:    #de 5 a 9 20%
    desc = 0.2  * p
elif c > 9:                #Mayor a 10 25%  
    desc = 0.25 * p
print ("Precio total: ",p)
total = p - desc
print ("Total a pagar con: ", total)