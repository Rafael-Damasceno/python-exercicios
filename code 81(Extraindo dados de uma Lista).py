lista = []
while True:
    lista.append((int(input('digite um numero: '))))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('o numero 5 estar na lista')
else:
    print('o numero 5 não esta na lista')
