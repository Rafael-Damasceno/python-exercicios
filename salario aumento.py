salario = float(input("digite o salário do funcionario: "))
print('plano: a, b, c')
plano = str(input("digite seu plano: "))

v1 = ((salario * 0.1) + salario)
v2 = ((salario * 0.15) + salario)
v3 = ((salario * 0.2) + salario)

if (plano == "a"):
    print("seu aumento foi de {}".format(v1))
if (plano == "b"):
    print("seu aumento foi de {}".format(v2))
if (plano == "c"):
    print("seu aumento foi de {}".format(v3))
