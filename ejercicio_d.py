# Simular el lanzamiento de un dado y 
# determine la cantidad de lanzamientos hasta que salga el numero 5

from random import *
print ("Dado lanzado")
d = 0
i = 0
while True:
    d = randint (1,100)
    print (d)
    i = i + 1
    if d == 5:
        break
print ('Cantidad de veces lazando hasta que salga 5: ' ,i)
print ('Valor de dado: ' ,d)
