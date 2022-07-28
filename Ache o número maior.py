#EX 4 Ache o número maior

contador = maior = menor = 0

while contador < 10:
    numero = int(input('digite um numero: '))
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if contador == 10:
        break


print(f'o maior numero é {maior}, menor numero é {menor}')

