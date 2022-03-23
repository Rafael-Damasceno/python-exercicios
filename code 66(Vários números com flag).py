cont = soma = 0
while True:
    n = int(input('digite um numero ou digite [999] para saber a soma: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'você digitou {cont} numeros e a soma deles é {soma}')

