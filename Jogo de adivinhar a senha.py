from random import randint
l1 = []
l2 = []
palpite = 0 # contador de tentativas
def sorteio(s,k):
    if s != ' ':
        for k in range(0, k):
            r = randint(0, 9)
            l1.append(r)
def Separa_Digitos(numero):
    for n in numero:
        l2.append(int(n))
    if len(l1) == 2:
        if len(l2) == 1:
            l2.insert(0, (0))

    if len(l1) == 3:
        if len(l2) == 1:
            l2.insert(0, (0))
            l2.insert(0, (0))
        if len(l2) == 2:
            l2.insert(0, (0))

    if len(l1) == 4:
        if len(l2) == 1:
            l2.insert(0, (0))
            l2.insert(0, (0))
            l2.insert(0, (0))
        if len(l2) == 2:
            l2.insert(0, (0))
            l2.insert(0, (0))
        if len(l2) == 3:
            l2.insert(0, (0))
def iguais(l1, l2):
    lb = []
    for i in l1:
        for j in l2:
            if (j == i):
                lb.append(j)
                break
    print(f'numeros de digitos corretos: {len(lb)}')
def Posicoes_Iguais(l1, l2):
    lp = []
    if len(l1) == 5:
        if l1[0] == l2[0]:
            lp.append(1)
        if l1[1] == l2[1]:
            lp.append(1)
        if l1[2] == l2[2]:
            lp.append(1)
        if l1[3] == l2[3]:
            lp.append(1)
        if l1[4] == l2[4]:
            lp.append(1)
    if len(l1) == 4:
        if l1[0] == l2[0]:
            lp.append(1)
        if l1[1] == l2[1]:
            lp.append(1)
        if l1[2] == l2[2]:
            lp.append(1)
        if l1[3] == l2[3]:
            lp.append(1)
    if len(l1) == 3:
        if l1[0] == l2[0]:
            lp.append(1)
        if l1[1] == l2[1]:
            lp.append(1)
        if l1[2] == l2[2]:
            lp.append(1)
    if len(l1) == 2:
        if l1[0] == l2[0]:
            lp.append(1)
        if l1[1] == l2[1]:
            lp.append(1)
    print(f'numero de digitos em posições iguais é: {len(lp)}')

print('-=-'*30)
titulo = 'BEM VINDO AO JOGO ADIVINHE A SENHA\n'
regras = 'nesse jogo voce tera 5 tentativas para acerta uma senha de 2 ate 5 digitos '
regras2 = 'voce definará a quantidades de digitos que deseja acertar '
print(titulo.center(80))
print(regras.center(80))
print(regras2.center(80))
print('-=-'*30)

q = int(input('QUANTOS DIGITOS VOCE DESEJA ACERTAR?\n'
              'digite 2, 3, 4 ou 5: '))
while q < 2 or q > 5:
    print('NUMERO INVALIDO')
    q = int(input('digite 2, 3, 4 ou 5: '))

semente = float(input('digite a semente para inicia os numeros aleatorios: '))
sorteio(semente, q)     #função para sortear os numeros

acertou = False #para criar um loop
while not acertou:
    t1 = (input('TENTATIVA NUMERO 1: '))
    Separa_Digitos(t1)      #função para transformar em lista
    iguais(l1, l2)          #função para ver se as listas tem valores iguais
    Posicoes_Iguais(l1, l2) #função para posições iguais
    palpite += 1
    if (l1 == l2):
        print('-=-' * 30)
        print(f'parabens, voce acertou em {palpite} tentativa!')
        break

    t2 = (input('TENTATIVA NUMERO 2: '))
    l2.clear()
    Separa_Digitos(t2)  # função para transformar em lista
    iguais(l1, l2)  # função para ver se as listas tem valores iguais
    Posicoes_Iguais(l1, l2)  # função para posições iguais
    palpite += 1
    if (l1 == l2):
        print('-=-' * 30)
        print(f'parabens, voce acertou em {palpite} tentativa!')
        break

    t3 = (input('TENTATIVA NUMERO 3: '))
    l2.clear()
    Separa_Digitos(t3)  # função para transformar em lista
    iguais(l1, l2)  # função para ver se as listas tem valores iguais
    Posicoes_Iguais(l1, l2)  # função para posições iguais
    palpite += 1
    if (l1 == l2):
        print('-=-' * 30)
        print(f'parabens, voce acertou em {palpite} tentativa!')
        break

    t4 = (input('TENTATIVA NUMERO 4: '))
    l2.clear()
    Separa_Digitos(t4)  # função para transformar em lista
    iguais(l1, l2)  # função para ver se as listas tem valores iguais
    Posicoes_Iguais(l1, l2)  # função para posições iguais
    palpite += 1
    if (l1 == l2):
        print('-=-' * 30)
        print(f'parabens, voce acertou em {palpite} tentativa!')
        break

    t5 = (input('TENTATIVA NUMERO 5: '))
    l2.clear()
    Separa_Digitos(t5)  # função para transformar em lista
    iguais(l1, l2)  # função para ver se as listas tem valores iguais
    Posicoes_Iguais(l1, l2)  # função para posições iguais
    palpite += 1
    if (l1 == l2):
        print('-=-' * 30)
        print(f'parabens, voce acertou em {palpite} tentativa!')
        break
    print('-=-' * 30)
    print('que pena, voce errou!')
    if len(l1) == 5:
        print(f'a senha certa seria: {l1[0]}{l1[1]}{l1[2]}{l1[3]}{l1[4]}')
        break
    if len(l1) == 4:
        print(f'a senha certa seria: {l1[0]}{l1[1]}{l1[2]}{l1[3]}')
        break
    if len(l1) == 3:
        print(f'a senha certa seria: {l1[0]}{l1[1]}{l1[2]}')
        break
    if len(l1) == 2:
        print(f'a senha certa seria: {l1[0]}{l1[1]}')
        break
