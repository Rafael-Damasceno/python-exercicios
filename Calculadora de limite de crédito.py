#EX 2 Calculadora de limite de crédito


conta = saldo = encargos = creditos = limite = comparacao = 0

while True:
    conta = int(input("Informe o numero da conta (-1 para terminar): "))
    if conta == -1:
        break
    saldo = float(input("Informe o saldo inicial: "))
    encargos = float(input("informe o total de encargos: "))
    creditos = float(input("informe o total de creditos: "))
    limite = float(input("informe o limite de creditos: "))
    comparacao = saldo + encargos - creditos

    if comparacao > limite:
        print("conta: {}".format(conta))
        print("limite de credito: {}".format(limite))
        print("saldo: {}".format(comparacao))
        print("limite de credito ultrapassado")


