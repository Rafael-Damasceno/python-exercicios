#Ex: 7 Quadrado de asteriscos vazio

lado = int(input("Digite o lado do quadrado: "))
rect = ''
if lado > 1 and lado < 20:
	for i in range(lado):
		for j in range(lado):
			if(j == 0 or j == lado-1 or i == 0 or i == lado-1):
				rect += '*'
				continue
			rect += ' '
		rect += '\n'
print(rect)