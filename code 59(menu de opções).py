from time import sleep
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
opção = 0

while opção != 5:
    print('''   \033[;1;31m-=-=-=-=-=-=-=-=-\033[m
    [1] somar 
    [2] multiplicar 
    [3] maior 
    [4] novos numeros 
    [5] sair do programa
    \033[;1;31m-=-=-=-=-=-=-=-=-\033[m''')
    opção = int(input('>>> Qual é a sua opção? '))
    if opção == 1:
        s = n1+n2
        print('a soma é {}'.format(s))
    elif opção == 2:
        m = n1*n2
        print('a multiplicação é {}'.format(m))
    elif opção == 3:
        if n1 > n2:
            print('o maior é {}'.format(n1))
        else:
            print('o maior é {}'.format(n2))
    elif opção == 4:
        n1 = int(input('digite o primeiro numero: '))
        n2 = int(input('digite o segundo numero: '))
        opção = 0
    elif opção > 5:
        print('dados ivalidos, tente novamente')
    sleep(2)

print('obrigador pela participação')
