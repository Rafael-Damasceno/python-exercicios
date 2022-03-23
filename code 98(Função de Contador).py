from time import sleep
def l():
    print('-=-' * 10)
def contador(i, f, p):
    l()
    print(f'contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('fim')



#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
l()
print('agora é sua vez de personalizar a contagem')
ini = int(input('inicio: '))
fim = int(input('fim: '))
pas = int(input('passo: '))
contador(ini, fim, pas)





