jogador = {}
partidas = []
jogador['nome'] = str(input('nome do jogador: '))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]} gols')
