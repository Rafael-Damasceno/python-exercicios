a = int(input('digite um numero: '))
b = int(input('digite outro numero: '))
c = int(input('digite mais um numero: '))
d = int(input('digite o ultimo numero: '))
tupla = (a, b, c, d)
print(f'o valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o valor 3 foi digitado na {tupla.index(3)+1} posição')
else:
    print('o valor 3 não foi digitado')
print('os valores pares digitados foram', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
