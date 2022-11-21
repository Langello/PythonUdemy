segundos = int(input('Ingrese los segundos\n'))

hora = 3600
minuto = 60

h = segundos // hora
restoSegundos = segundos % hora
m = restoSegundos//minuto
s = restoSegundos % minuto

print(f'Los segundos que ingresastes son: {segundos}\nEquivalen a {h} horas, {m} minutos y {s} segundos')

input('Presione Enter para finalizar')

