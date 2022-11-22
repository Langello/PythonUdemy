n = int(input('Ingrese un número \n'))
n += 1
sumImpares = 0
sumPares = 0
for n in range(1, n):
    if n % 2 == 0:
        sumPares += n
    else:
        sumImpares += n


print(f'Suma pares : {sumPares}\nSuma Impares : {sumImpares} ')


