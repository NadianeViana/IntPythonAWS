#Dois valores, operação e resultado. Mostrar erro.

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
operacao = input("Usando +, -, * ou /, informe a Operação que deseja realizar: ")

if operacao == '+' :
    soma = valor1 + valor2
    print("O resultado da Soma é: ", soma)
elif operacao == '-' :
    subtracao = valor1 - valor2
    print("O resultado da subtração é: ")
elif operacao == "*" :
    multiplicacao = valor1 * valor2
    print("O resultado da Multiplicação é: ")
elif operacao == "/" :
    divisao = valor1 / valor2
    print("O resultado da Divisão é: ", divisao)
else:
    print("Inválido! VAI EXPLODIR!!!")