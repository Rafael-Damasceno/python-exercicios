resposta = 'S'
contador = maior = soma = media = menor = 0

while resposta in 'Ss':
    numero = int(input('digite um numero: '))
    resposta = str(input('quer continuar [S/N]? '))
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = (soma/contador)
print(f'o maior numero é {maior}, menor numero é {menor} e a media é {media}')
