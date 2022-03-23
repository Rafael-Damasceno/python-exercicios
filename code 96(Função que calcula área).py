def area(l, c):
    m = l * c
    print(f'a area de um terreno {l} x {c} é de {m:.2f}')
def linha(txt):
    print('-=' * 20)
    print(txt)
    print('-=' * 20)


#codigo principal
linha('{:>30}'.format('construindo terreno'))
l = float(input('largura (m): '))
c = float(input('comprimento (m): '))
area(l, c)
