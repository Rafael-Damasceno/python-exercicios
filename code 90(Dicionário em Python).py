aluno = {}
for c in range(0, 1):
    aluno['nome'] = str(input('nome do aluno: '))
    aluno['media'] = float(input('media do aluno: '))
    if 5 <= aluno['media'] < 7:
        aluno['situação'] = 'recuperação'
    elif aluno['media'] >= 7:
        aluno['situação'] = 'aprovado'
    else:
        aluno['situação'] = 'reprovado'
print('-=-' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')

