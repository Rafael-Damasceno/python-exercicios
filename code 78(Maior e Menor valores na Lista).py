n1 = int(input('digite a posição 0: '))
n2 = int(input('digite a posição 1: '))
n3 = int(input('digite a posição 2: '))
n4 = int(input('digite a posição 3: '))
n5 = int(input('digite a posição 4: '))
lista = [n1, n2, n3, n4, n5]
print(lista)
m = max(lista)
n = min(lista)
print(f'o maior valor digitado foi {max(lista)} nas posiçoes ', end='')
for i, v in enumerate(lista):
    if v == m:
        print(f'{i}...', end='')
print()
print(f'o menor valor digitado foi {min(lista)} nas posiçoes ', end='')
for i, v in enumerate(lista):
    if v == n:
        print(f'{i}...', end='')
print()
