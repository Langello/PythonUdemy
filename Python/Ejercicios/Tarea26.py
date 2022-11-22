v1 = int(input('Ingrese el primer número \n'))
v2 = int(input('Ingrese el segundo numero \n'))

sumPositivos=0
sumNegativos=0
for n in range(v1, v2+1):
    if n > 0:
        sumPositivos+=1
    elif n<0:
        sumNegativos+=1

print(f'En el rango de {v1} hasta {v2}\nLa cantidad de numeros negativos es {sumNegativos}\nLa cantidad de numeros positivos es {sumPositivos}')