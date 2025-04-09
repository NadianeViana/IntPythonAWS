#Introduzir o Saldo Inicial

saldoInicial = float(input("Informe o saldo inicial: "))
valorOperacao = float(input("Insira o montante desejado: "))

valorAuxiliar = saldoInicial + valorOperacao

if valorAuxiliar < 0:
    print("Operação Inválida. Saldo Insuficiente. :", saldoInicial)
else:
    saldoInicial = valorAuxiliar
print("Saldo atual: ", saldoInicial)