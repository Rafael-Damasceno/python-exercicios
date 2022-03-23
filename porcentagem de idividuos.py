# Faça um programa que determine e imprima a maior idade dos habitantes e a porcentagem #
# de indivíduos do sexo feminino cuja idade está acima de 18 anos inclusive e que tenham olhos verdes.#

from time import sleep
sexo = olhos = cabelo = contador = maior = 0
resp = 'S'
contador_feminino = contador_masculino = contador_especifico = porcentagem = total = 0
while resp in 'Ss':
    sexo = str(input('digite seu sexo [m/f]: '))
    olhos = str(input('qual a cor dos seus olhos [azuis, verdes, castanhos]? '))
    cabelo = str(input('qual é a cor dos seus cabelos [louros, castanhos, pretos]? '))
    idade = int(input('digite sua idade: '))
    resp = str(input('quer continuar [S/N]: ')).upper().strip()[0]
    contador += 1
    if contador == 1:
        maior = idade
    else:
        if idade > maior:
            maior = idade
    if sexo == 'm':
        contador_masculino += 1
    if sexo == 'f':
        contador_feminino += 1
    if sexo == 'f' and idade > 18 and olhos == 'verdes':
        contador_especifico += 1
total = contador_masculino + contador_feminino
porcentagem = ((contador_especifico * 100) / total)
sleep(1)
print('a maior idade é {}'.format(maior))
sleep(1)
print('a porcentagem de meninas maiores de 18 e com olhos verdes é {}'.format(porcentagem))
