n=int(input('Ingrese un número entre 0 y 9\n'))
if n == 0:
    r='CERO'
elif n == 1:
    r='UNO'
elif n == 2:
    r='DOS'
elif n == 3:
    r='TRES'
elif n == 4:
    r='CUATRO'
elif n == 5:
    r='CINCO'
elif n == 6:
    r='SEIS'
elif n == 7:
    r='SIETE'
elif n == 8:
    r='OCHO'
elif n == 9:
    r='NUEVE'
else:
    print('El número no esta entre 0 y 9')
    quit()

print(f'El número es {n} y se escribe así : {r}')
