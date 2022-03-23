lista = []
pares = []
impares = []
while True:
    n = (int(input('digite um numero: ')))
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=-' * 15)
print(f'a lista completa é {lista}')
print(f'a lista com numeros pares é {pares}')
print(f'a lista com numeros ímpares é {impares}')
