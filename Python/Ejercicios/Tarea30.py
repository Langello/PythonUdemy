n1 = int(input('Ingrese el primer número \n'))
n2 = int(input('Ingrese el segundo numero \n'))
n3 = int(input('Ingrese el tercer número \n'))
n4 = int(input('Ingrese el cuarto numero \n'))
n5 = int(input('Ingrese el quinto número \n'))
n6 = int(input('Ingrese el sexto numero \n'))

lista=[n1,n2,n3,n4,n5,n6]
cPares=0
cImpares=0
cCeros=0
for i in lista:
    if i!=0:
        if i % 2 ==0:
            cPares+=1
        else:
            cImpares+=1
    else:
        cCeros+=1

print(f'La cantidad de números impares es {cImpares}\nLa cantidad de números pares es {cPares}\nLa cantidad de ceros es {cCeros}')