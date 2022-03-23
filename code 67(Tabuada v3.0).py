num = 0
while True:
    num = int(input('digite um numero para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c:2} = {num*c}')
print('fim do programa')