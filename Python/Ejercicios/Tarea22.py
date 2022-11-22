n = int(input('Ingrese un número \n'))


contador = 0

while n >= 1:
    if n%2==0:
        contador+=1
    n= n//10
    
print(f'Cantidad de digitos pares : {contador}')

