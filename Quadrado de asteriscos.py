#EX: 6 Quadrado de asteriscos

lado = int(input("Digite o lado do quadrado: "))
if lado > 1 and lado < 20:
    for c in range(lado):
        print('*'*lado)
