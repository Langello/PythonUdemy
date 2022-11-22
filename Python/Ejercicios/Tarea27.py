r1 = int(input('Ingrese el primer número \n'))
r2 = int(input('Ingrese el segundo numero \n'))
m = int(input('Ingrese el múltiplo\n'))
cantMultiplos = 0
for i in range(r1, r2 + 1):
    if i != 0:
        if i % m == 0:
            cantMultiplos += 1
print(f'La cantidad de multiplos de {m} en el rango {r1} hasta {r2} es : {cantMultiplos}')
