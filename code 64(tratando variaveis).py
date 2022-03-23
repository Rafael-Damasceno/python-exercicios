n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('digite um numero ou digite [999] para saber a soma: '))
    soma += n
    cont += 1
print('você digitou {} numeros e a soma deles é {}'.format(cont-1, soma-999))







