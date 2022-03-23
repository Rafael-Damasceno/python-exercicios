lista = [[], []]
for c in range(0, 7):
    valor = int(input(f'digite o {c}o. numero: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-=-' * 15)
lista[0].sort()
lista[1].sort()
print(f'os valores pares foram {lista [0]}')
print(f'os valores impares foram {lista[1]}')
print('-=-' * 15)


