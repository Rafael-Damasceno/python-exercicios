n = int(input("Digite o valor de n: "))
fat = 1
i = 2
while i <= n:
    fat *= i
    i = i + 1

print('O valor de {}! é {}'.format(n, fat))

