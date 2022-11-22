numInicial = int(input('Número Inicial: '))
numFinal = int(input('Número Final: '))
i = 0
contador = 0


i = numInicial + 1
while i < numFinal:
    contador += 1
    i += 1


print(f'CANTIDAD: {contador}')