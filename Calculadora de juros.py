#EX 3 Calculadora de juros

while True:
    principal = int(input("Informe o valor principal do emprestimo (-1 para terminar): "))
    if principal == -1:
        break
    taxa = float(input("Informe a taxa de juros: "))
    dias = int(input("informe o prazo do emprestimo em dias: "))

    juros = principal * taxa * dias / 365

    print("o valor dos juros é de {:.2f}".format(juros))

