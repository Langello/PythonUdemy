c=int(input('Ingrese capital:\n'))
t=int(input('Ingrese tiempo:\n'))
r=int(input('Ingrese tasa interés:\n'))

m=((1+r/100)**t)*c
i= m-c
print(f'El capital ingresado fue {c}, el plazo fue {t} con una tasa de interes del {r}%')
print(f'El monto obtenido es de {m}\nEl interés generado es de {i}')