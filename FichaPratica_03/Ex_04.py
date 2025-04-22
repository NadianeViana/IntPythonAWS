#Verificador de números primos

opcUser = int(input("Insire um número para análise: "))

if opcUser <= 1:
    print("Não é primo!")
else:
    opcUserDiv = 0

    for i in range(1, opcUser + 1):
        if opcUser % i == 0:
            opcUserDiv += 1
    if opcUserDiv == 2:
            print("É primo!")
    else:
            print("Não é primo!")