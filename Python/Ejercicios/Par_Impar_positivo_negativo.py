n = int(input('ingrese numero\n'))
if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f'el número {n} es par POSITIVO')
        else:
            print(f"el número {n}  es impar POSITIVO")
    else:
        if n % 2 == 0:
            print(f'el número {n} es par NEGATIVO')
        else:
            print(f"el número {n}  es impar NEGATIVO")
else:
    print(f'nuúmero {n} es NEUTRO')
