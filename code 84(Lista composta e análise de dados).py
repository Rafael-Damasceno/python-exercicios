maior = menor = cont = 0
h = list()
dados = list()

while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))
    if len(h) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    h.append(dados[:])
    dados.clear()
    resp = ' '
    cont += 1
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'foram inscritas {cont} pessoas')
print(f'o maior peso é {maior} peso de ', end='')
for p in h:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'o menor peso é {menor} peso de ', end='')
for p in h:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')




