cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', ' oito', 'nove')
while True:
    núm = int(input('digite um número entre 0 e 9: '))
    if 0<= núm <= 9:
        break
    print('tente novamente, mas dessa vez ', end='')
print(f'Este é o número {cont[núm]}.')