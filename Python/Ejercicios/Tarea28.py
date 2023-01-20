n1 = int(input('Ingrese el primer número \n'))
n2 = int(input('Ingrese el segundo numero \n'))
n3 = int(input('Ingrese el tercer número \n'))
n4 = int(input('Ingrese el cuarto numero \n'))
n5 = int(input('Ingrese el quinto número \n'))
n6 = int(input('Ingrese el sexto numero \n'))

lista=[n1,n2,n3,n4,n5,n6]


nMenor = nMayor = lista[0]

for lista in lista:
    if lista < nMenor:
        nMenor = lista
    elif lista > nMayor:
        nMayor = lista 

print(f'El máximo es {nMayor}') 
print(f'El mínimo es {nMenor}')   
