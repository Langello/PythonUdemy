n = input('Número 1 = "Verano"\nNúmero 2 = "Otoño"\nNúmero 3 = "Invierno"\nNúmero 4 = "Primareva" \n')

if n == '1':
    e='Verano'
elif n == '2':
    e= 'Otoño'
elif n == '3':
    e= 'Invierno'
elif n == '4':
    e= 'Primavera'
else:
    e= 'No ingreso un valor entre 1 y 4'

print(e)