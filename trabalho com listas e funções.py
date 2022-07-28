lista = []
lista2 = [9, 5, 2, 1, 8]
def Separa_Digitos(numero):
    for n in numero:
        lista.append(int(n))
    if len(lista) == 1:
        lista.insert(0,(0))
        lista.insert(0, (0))
        lista.insert(0, (0))
        lista.insert(0, (0))
    elif len(lista) == 2:
        lista.insert(0, (0))
        lista.insert(0, (0))
        lista.insert(0, (0))
    elif len(lista) == 3:
        lista.insert(0, (0))
        lista.insert(0, (0))
    elif len(lista) == 4:
        lista.insert(0, (0))
    print('-=-'*15)
    print(f'lista na ordem direta {lista}')
    lista.reverse()
    print(f'lista na ordem inversa {lista}')
    print('-=-' * 25)
    lista.reverse()
def Digitos_Iguais(lista, lista2):
   lista3 = []
   for i in lista:
       for j in lista2:
           if(j==i):
               lista3.append(j)
               break
   print(f'Comparando o numero que voce digitou com a seguinte lista: {lista2}')
   print('-=-' * 25)
   print(f'Numero de digitos iguais: {len(lista3)}')
def Posicoes_Iguais(lista, lista2):
    lista4 = []
    if lista[0] == lista2[0]:
        lista4.append(1)
    if lista[1] == lista2[1]:
        lista4.append(1)
    if lista[2] == lista2[2]:
        lista4.append(1)
    if lista[3] == lista2[3]:
        lista4.append(1)
    if lista[4] == lista2[4]:
        lista4.append(1)
    print(f'numero de digitos em posições iguais é: {len(lista4)}')
    print('-=-' * 15)


#codigo principal
num = (input("digite um numero inteiro com ate 5 digitos: "))
Separa_Digitos(num)
Digitos_Iguais(lista, lista2)
Posicoes_Iguais(lista, lista2)



