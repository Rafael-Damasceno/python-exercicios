from time import sleep

def maior(*num):
    cont = maior = 0
    print('-=-' * 10)
    print('analisando os valores informados')
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior =  valor
        cont += 1
    print(f'foram informados {cont} valores ao todo.')
    print(f'o maior valor informado foi {maior}.')



#programa principal
maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
