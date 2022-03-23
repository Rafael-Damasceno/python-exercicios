print('\033[;0;34m-=-\033[m' * 5)
print('GERADOR DE PA')
print('\033[;0;34m-=-\033[m' * 5)

primeiro = int(input('digite o primeiro termo: '))
razão = int(input('digite a razão: '))
termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('mais quantos termos serão mostrados? '))
print('fim')
print('foram mostrados {} termos'.format(total))

