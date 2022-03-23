listagem = ('lapis', 1.00,
            'caderno', 15.00,
             'caneta', 2.00,
             'mochila', 30.00)

print('-=-' * 15)
print(f'{"listagem de preços":^40}')
print('-=-' * 15)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-=-' * 15)
