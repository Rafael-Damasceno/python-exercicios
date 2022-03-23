from datetime import datetime

candidato = {}
for c in range(0, 1):
    candidato['nome'] = str(input('nome do aluno: '))
    candidato['nascimento'] = int(input('ano de nascimento: '))
    candidato['idade'] = datetime.now().year - candidato['nascimento']
    candidato['carteira'] = int(input('carteira de trabalho (0 não tem): '))
    if candidato['carteira'] != 0:
        candidato['contrato'] = int(input('ano de contratação: '))
        candidato['salario'] = float(input('salario: '))
        candidato['aposentadoria'] = candidato['idade'] + ((candidato['contrato'] + 35) - datetime.now().year)
print('-=-' * 30)
for k, v in candidato.items():
    print(f'- {k} é igual a {v}')

