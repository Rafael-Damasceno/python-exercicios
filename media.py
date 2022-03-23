# Faça um programa que aceite uma quantidade indeterminada de números e mostre a media aritmetica desses numeros#

num = int(input('digite um numero ou digite (999) para saber a media: '))
contador = 0
soma = 0

while num != 999:
    contador = contador + 1
    soma = soma + num
    num = int(input('digite um numero ou digite (999) para saber a media: '))

print("você digitou {} numeros".format(contador), end=' ')
media = soma / contador
print("e a média deles é igual a {:.2f}".format(media))
