#Solicitar um número ao usuário e especificar se é par ou ímpar

valorUsuário = int(input("Informe um número para análise: "))

if valorUsuário % 2 == 0:
    print("O número informado é PAR")
else:
    print("O número é IMPAR")