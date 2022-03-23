from random import randint
v = 0
while True: #repetição infinita
    jogador = int(input('diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar?[P/I] ')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. total de {total}', end=' ')
    print('deu par' if total % 2 == 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu!')
            v += 1
        else:
            print('voce perdeu!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER! voce venceu {v} vezes')

