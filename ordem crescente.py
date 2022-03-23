lista = []
for c in range(0, 3):
    n = int(input('digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'os números digitados em ordem crescente foram:{lista}')
