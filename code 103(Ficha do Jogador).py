def ficha(jog='<desconhecido>', gol=0):
    print(f'jogador {jog} fez {gol} gols no campeonato')


#codigo principal
n = str(input('nome do jogador: '))
g = str(input('numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
