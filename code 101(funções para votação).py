def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'como{idade} anos: Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: voto opcional'
    else:
        return f'com {idade} anos: Voto obrigatorio'


ano = int(input('informe o seu ano de nascimento: '))
print(voto(ano))

