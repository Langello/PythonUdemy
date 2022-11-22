v1 = int(input('Ingrese el primer número \n'))
v2 = int(input('Ingrese el segundo numero \n'))

sumMultiplos1 = 0
sumMultiplos2 = 0

for n in range(1, v1):
    if v1 % n == 0:
        sumMultiplos1 += n

for i in range(1, v2):
    if v2 % i == 0:
        sumMultiplos2 += i

if sumMultiplos1 == v2 and sumMultiplos2 == v1:
    print(f'Los números {v1} y {v2} son amigos')
else:
    print(f'Los números {v1} y {v2}  NO son amigos')
