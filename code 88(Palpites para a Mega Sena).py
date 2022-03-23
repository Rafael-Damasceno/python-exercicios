from random import randint
q = int(input('quantos jogos voce quer que eu sorteio: '))

print('-=' * 3, f'sorteando {q} jogos', '-=' * 3)
for q in range(0, q):
    list1 = [randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6)]
    print(f'jogo {q+1}: {list1}')
