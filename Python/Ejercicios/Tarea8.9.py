n1=int(input('Numero 1:\n'))
op=input('Operador:\n')
n2=int(input('Numero 2:\n'))
if op == '+':
    r= n1 + n2
elif op == '-':
    r= n1 - n2
elif op == '/' and n2 !=0:
    r= n1 / n2
elif op == '*':
    r= n1 * n2
else:
    print('ERROR')
    quit()
print(f'El resultado de {n1} {op} {n2} es : {r}')