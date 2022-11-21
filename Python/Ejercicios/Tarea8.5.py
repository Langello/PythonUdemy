n = int(input('Ingrese núumero\n'))

if n % 2 == 0:
    x = 2
    r = n*x
    m = 'PAR'
else:
    x = 3
    r = n*x
    m = 'IMPAR'

print(f'El número {n} es {m} entonces se multiplica por {x} y el resultado es {r}')
