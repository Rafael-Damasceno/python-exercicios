g = list()
p = dict()
soma = media = 0
while True:
    p.clear()
    p['nome'] = str(input('nome: '))
    while True:
        p['sexo'] = str(input('sexo: [m/f] ')).upper()[0]
        if p['sexo'] in 'MF':
            break
        print('ERRO!por favor, digite apenas M ou F.')
    p['idade'] = int(input('idade: '))
    soma += p['idade']
    g.append(p.copy())
    while True:
        resp = str(input('quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=-' * 30)
print(f'a) todo temos {len(g)} pessoas cadastradas.')
media = soma / len(g)
print(f'b) a media de idade é de {media:5.2f} anos.')
print(f'c) as mulheres cadastradas foram', end='')
for c in g:
    if c['sexo'] in 'Ff':
        print(f'{c["nome"]}', end='')
print()
print('d) lista das pessoas que estão acima da media: ')
for c in g:
    if c['idade'] >= media:
        print('     ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

