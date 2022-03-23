print('\033[;0;34m-=-\033[m' * 5)
print('GERADOR DE PA')
print('\033[;0;34m-=-\033[m' * 5)

p = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
termo = p
cont = 1  #contador
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += r   #termo mais a razão
    cont += 1
print('pausa')
