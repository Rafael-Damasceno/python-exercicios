lista = []
while True:
    n = (int(input('digite um numero: ')))
    if n not in lista:
        lista.append(n)
        print('valor adicionado')
    else:
        print(f'o numero {n} ja existe na lista')
        print('deletei')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort()
print(lista)
