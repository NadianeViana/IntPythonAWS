#Introduzir o Saldo Médio. Se entrada, digite c. Se saída, digite d. 

saldoInicial = float(input("Informe o saldo médio: "))
operacao = float("Para entrada, digite c. Para saída, digite d. : ")
valorOperacao = float(input("Insira o montante desejado"))

if operacao == "c":
    saldoTotal = saldoInicial + valorOperacao
    print("O saldo total é:", saldoTotal)

else:
 saldoTotal = saldoInicial
    
if saldoTotal >= valorOperacao:
    saldoTotal = saldoInicial - valorOperacao
    print("O saldo total é:", saldoTotal)
else:
    print("Não tens saldo para isto.")