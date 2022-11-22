ni = int(input('Numero 1 \n'))
nf = int(input('Numero 2 \n'))


cp = 0
i=ni+1
while i < nf:
    if i % 2 == 0:
        cp += 1
    i += 1

print(f'CANTIDAD DE PARES: {cp}')

