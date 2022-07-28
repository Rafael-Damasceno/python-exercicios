#EX: 1 Consumo de gasolina

total = contador = consumo_atual = 0
litros = float(input("Informe quantos litros abasteceu (-1 para terminar): "))

if litros != -1:
    km = float(input("Informe quantos km dirigiu: "))
    consumo_atual = (km / litros)
    print("O consumo atual é de: {:.2f} km/l \n\n".format(consumo_atual))
    total = (total + consumo_atual)
    contador = (contador + 1)

while litros != -1:
    litros = float(input("Informe quantos litros abasteceu (-1 para terminar): "))
    if litros != -1:
        km = float(input("Informe quantos km dirigiu: "))
        consumo_atual = (km / litros)
        print("O consumo atual é de: {:.2f} km/l \n\n".format(consumo_atual))
        total = (total + consumo_atual)
        contador = (contador + 1)

if litros == -1:

    if contador != 0:
        consumo_geral = (total / contador)
        print("o consumo geral foi de: {:.2f} km/l\n".format(consumo_geral))


