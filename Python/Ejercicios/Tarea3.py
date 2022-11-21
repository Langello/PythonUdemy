num = int(input('Número: ')) #12345


res = num % 10 #5
num = num // 10 #1234
ni = res * 10 #50

res = num % 10 #4
num = num // 10 #123
ni = (ni + res) * 10 #540

res = num % 10 #3
num = num // 10 #12 
ni = (ni + res) * 10 #5430

res = num % 10 #2
num = num // 10 #1
ni = (ni + res) * 10 #54320

ni = ni + num #54321


print('Inverso: ', ni)