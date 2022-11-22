n = int(input('Ingrese un número\n'))

contador = 0
i = 0

while i < n:
    i += 1
    if i % 5 == 0:
        contador += 1

print(f'La cantidad de números multiplo de 5  de 0 a {n} es : {contador}')
