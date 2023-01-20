n1 = int(input('Ingrese el primer número \n'))
n2 = int(input('Ingrese el segundo numero \n'))
n3 = int(input('Ingrese el tercer número \n'))
n4 = int(input('Ingrese el cuarto numero \n'))
n5 = int(input('Ingrese el quinto número \n'))
n6 = int(input('Ingrese el sexto numero \n'))
n7 = int(input('Ingrese el séptimo número \n'))
n8 = int(input('Ingrese el octavo numero \n'))
n9 = int(input('Ingrese el noveno número \n'))
n10 = int(input('Ingrese el décimo numero \n'))
n11 = int(input('Ingrese el onceavo número \n'))
n12 = int(input('Ingrese el doceavo numero \n'))

lista1=[n1,n2,n3,n4]
lista2=[n5,n6,n7,n8]
lista3=[n9,n10,n11,n12]

sum1=0
for i in lista1:
    sum1+=i


sum2=0
for j in lista2:
    sum2+=j
sum3=0
for k in lista3:
    sum3+=k

print(f'La primera lista es {lista1} y su suma es {sum1}')
print(f'La primera lista es {lista2} y su suma es {sum2}')
print(f'La primera lista es {lista3} y su suma es {sum3}')