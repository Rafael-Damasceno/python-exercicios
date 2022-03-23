from time import sleep
sexo = contador_feminino = contador_masculino = contador_idade = 0
while True:
    print('-=-' * 8)
    print('  CADASTRE UMA PESSOA')
    print('-=-' * 8)
    idade = int(input('digite sua idade: '))
    resp = ' '
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite seu sexo [m/f]: ')).upper().strip()[0]
    print('-=-' * 8)
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if sexo == 'M':
        contador_masculino += 1
    if sexo == 'F' and idade < 20:
        contador_feminino += 1
    if idade > 18:
        contador_idade += 1
    if resp == 'N':
        break
sleep(1)
print(f'{contador_idade} pessoas tem mais de 18 anos')
sleep(1)
print(f'foram cadrastados {contador_masculino} homens')
sleep(1)
print(f'{contador_feminino} mulheres tem menos de 20 anos')
