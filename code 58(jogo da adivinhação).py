from random import randint #gera os numeros
from time import sleep #coloca tempo

computador = randint(0, 10)
palpites = 0 # contador de palpites
print('\033[;1;31m-=-\033[m' * 18)
print('\033[;1;34mvou pensar em um numero de 0 a 10, tente adivinhar...\033[m')
print('\033[;31m-=-\033[m' * 18)

acertou = False
while not acertou:
    jogador= int(input("em que numero estou pensando? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[;1;31mMais!...\033[m')

            print('tente mais uma vez')
            sleep(1)
        elif jogador > computador:
            print('\033[;1;31mMenos!...\033[m')
            print('tente mais uma vez')
            sleep(1)
print('\033[;1;32mACERTOU\033[m com {} palpites'.format(palpites))


