n = int(input('Ingrese el número de un mes\n'))

if n >= 1 and n <=3:
    e='Verano'
elif n >= 4 and n <= 6:
    e= 'Otoño'
elif n >= 7 and n <= 9:
    e= 'Invierno'
elif n >= 10 and n <= 12:
    e= 'Primavera'
else:
    e= 'No ingreso un valor entre 1 y 4'

print(f'Es :{e}')