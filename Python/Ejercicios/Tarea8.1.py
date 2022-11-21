n1 = float(input('Ingrese el primer numero\n'))
n2 = float(input('Ingrese el segundo numero\n'))
if n1 > n2:
    print(f'Entre el número {n1} y el numero {n2} el mayor es {n1}')
elif n2 > n1:
    print(f'Entre el número {n1} y el numero {n2} el mayor es {n2}')
else:
    print('Los números son iguales')
