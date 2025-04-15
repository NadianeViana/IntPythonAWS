#Receber número inteiro e calcular fatorial usando while.

nmroInt = int(input("Informe um número inteiro para fatorar: "))

result = 1
i = 1

while i <= nmroInt:
    result *= i
    i += 1
    print(result)