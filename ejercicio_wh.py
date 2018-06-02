#En un cultivo se tiene una cantidad de bacterias inicial; cada dia esta cantidad se
#duplica. Determine en que dia la cantidad de bacterias excede a un valor maximo.
d = 0
bac = 5
vmax = 1000
while bac <= vmax:
    bac = bac * 2
    d = d + 1
print ('El dia en el que la cantidad de bacterias excedio el valor maximo es: ',d)
print ('Cantidad de bacterias: ',bac)