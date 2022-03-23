from time import sleep

valor = carteira1 = c = o = venda = qf = q1 = q2 = 0
cont_compra = cont_venda = cont = cont_esp = 0
n1 = ' '
while True:
    print('VINO11, HCTR11, VILG11, XPML11 e BCFF11.')
    n1 = str(input('informe um fundo imobiliario: '))
    bal = n1
    if bal == 'VINO11':
        print('o valor dessa ação R$47.29')
    if bal == 'HCTR11':
        print('o valor dessa ação R$119.20')
    if bal == 'VILG11':
        print('o valor dessa ação R$99.40')
    if bal == 'XPML11':
        print('o valor dessa ação R$90.73')
    if bal == 'BCFF11':
        print('o valor dessa ação R$66.89')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('voce quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
while True:
    print('{:-^80}'.format('Sistema de gestão de Fundos imobiliários'))
    print('{:-^80}'.format('Escolhas uma das opções'))
    print(''' 
    [1] Informar uma compra.
    [2] Informar uma venda.
    [3] Mostrar P/VP.
    [4] Mostrar relatório completo com Imposto de renda devido. 
    [5] Informe -1 para sair do programa''')
    n = int(input('digite sua opção: '))
    if n < 0:
        break
    if n == 1:
        c = ' '
        while c not in '11':
            c = str(input('qual sua compra? ')).upper().strip()[5]
        j = float(input('qual o valor da compra? '))
        q1 = int(input('informe a quantidade: '))
        valor = (q1 * j)
        qf = (q1 - q2)
        print(f'a compra foi {valor}')
        carteira1 = valor
        cont_compra += 1
    if n == 2:
        v = ' '
        print('VINO11, HCTR11, VILG11, XPML11 e BCFF11')
        while v not in '11':
            v = str(input('qual ação voce quer vender: ')).upper().strip()[5]
        j2 = float(input('qual o valor da venda: '))
        q2 = int(input('informe a quantidade: '))
        venda = (q2 * j2)
        carteira1 = valor - venda
        qf = (q1 - q2)
        print(f'sua carteira ficou {carteira1}')
    if n == 3:
        vp = float(input('informe o valor patrimonial: '))
        nome = str(input('informe o nome do ativo: ')).upper()
        if nome == 'VINO11':
            o = 47.29
            calculo = (o / vp)
            print(f' o pv é {calculo} ')
        elif nome == 'HCTR11':
            o = 119.20
            calculo = (o / vp)
            print(f' o pv é {calculo} ')
        elif nome == 'VILG11':
            o = 99.40
            calculo = (o / vp)
            print(f' o pv é {calculo} ')
        elif nome == 'XPML11':
            o = 90.73
            calculo = (o / vp)
            print(f' o pv é {calculo} ')
        elif nome == 'BCFF11':
            o = 66.89
            calculo = (o / vp)
            print(f' o pv é {calculo} ')
    if n == 4:
        sleep(1)
        print(f'sua carteira existe essa quantidade de ações {cont_compra - cont_venda}')
        sleep(1)
        print(f'o valor total dessas ações é {carteira1}')
        sleep(1)
        print(f'e sua quantidade é {qf}')
