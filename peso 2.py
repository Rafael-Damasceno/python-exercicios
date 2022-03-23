# Faça um sistema que calcule e imprima o número e o peso do porco mais magro e o número e o peso do porco mais gordo #
maior = 0
nome_maior = ''
menor = 1000
nome_menor = ''
for c in range(0, 5):
    nome = str(input('digite o número do cracha: '))
    peso = float(input('digite o peso do porco: '))
    if peso == 1:
        maior = peso
    else:
        if peso > maior:
            maior = peso
            nome_maior = nome
    if peso == 1:
        menor = peso
    else:
        if peso < menor:
            menor = peso
            nome_menor = nome
print('O porco mais pesado é o {} e pesa {}kg'.format(nome_maior, maior))
print('O porco mais leve é o {} e pesa {}kg'.format(nome_menor, menor))
