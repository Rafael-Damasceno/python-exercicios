n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'douze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
c = 0
while True:
    c = int(input('digite um numero entre 0 e 20: '))
    if 0 <= c <= 20:
        break
print(f'o numero é {n[c]}')

