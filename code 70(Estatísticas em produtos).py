from time import sleep
cont = p = soma = contador_p = menor = 0
b = ' '
while True:
    print('-=-' * 10)
    print('{:-^30}'.format('LOJA SUPER BARATÃO'))
    print('-=-' * 10)
    produto = str(input('nome do produto: '))
    p = int(input('digite o preço: '))
    cont += 1
    soma += p
    if p > 1000:
        contador_p += 1
    if cont == 1 or menor > p:
        menor = p
        b = produto
    print('-=-' * 8)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
sleep(1)
print(f'o total de gasto na compra foi de {soma}')
sleep(1)
print(f'{contador_p} foi a quantidade de produtos a cima de 1000 reais')
sleep(1)
print(f'o produto mais barato é {b} que custa {menor}')



