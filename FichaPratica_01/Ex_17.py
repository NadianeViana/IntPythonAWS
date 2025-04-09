#Calcular crédito especial com base no saldo do cliente

saldoCliente = float(input("Informe o saldo do cliente para análise de crédito: "))

if saldoCliente < 2000:
    print("Sem crédito.")
elif saldoCliente >=2000 and saldoCliente <4000:
    taxa = 0.2
    percCredClient = saldoCliente * taxa
    print("Crédito concecido: ", percCredClient)
elif saldoCliente >= 4000 and saldoCliente <= 6000:
    taxa = 0.3
    percCredClient = saldoCliente * taxa
    print("Crédito concecido: ", percCredClient)
else:
    taxa = 0.4
    percCredClient = saldoCliente * taxa
    print("Crédito concecido: ", percCredClient)