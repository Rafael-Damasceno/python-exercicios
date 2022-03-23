# Faça um programa que receba a idade e o peso de 3 pessoas e mostre #

peso_maior = 0
maior_idade = 0

for c in range(0, 3):
    idade = int(input('Digite a idade: '))
    peso = float(input('digite o peso: '))
    if peso >= 60:
        peso_maior += 1
    if 18 <= idade and peso >= 50:
        maior_idade += 1
print('Ao todo {} pessoas tem 60kg ou mais'.format(peso_maior))
print('Ao todo {} pessoas são maiores de idade e pesam mais de 50kg'.format(maior_idade))
