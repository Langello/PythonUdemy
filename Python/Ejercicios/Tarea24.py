#número perfecto
v = int(input('Ingrese un número \n'))
 
sumMultiplo=0

for n in range(1,v):
    if v%n ==0:
        sumMultiplo+=n

if sumMultiplo==v:
    print(f'El numero {v} es PERFECTO')
else:
    print(f'El numero {v} es IMPERFECTO')



