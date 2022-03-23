soma = 0
cont = 0
for c in range(1, 6):
    num = int(input("digite o {}° número: ".format(c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print("você informou {} números pares e o resultado da soma foi {}".format(cont, soma))