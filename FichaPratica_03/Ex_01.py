#Calculadora Simples com Operações Aritméticas

varCalc = "s"

for i in range(100):
    nmrFirst = int(input("Insira o 1º valor: "))
    nmrSecond = int(input("Insira o 2º valor: "))
    OpcSelec = input("Insira a opção desejada: ")
    result = 0

    if OpcSelec == "+":
        result = nmrFirst + nmrSecond
        print("O resultado da soma é: ", result)
    elif OpcSelec == "-":
        result = nmrFirst - nmrSecond
        print("O resultado da subtração é: ", result)
    elif OpcSelec == "*":
        result = nmrFirst * nmrSecond
        print("O resultado da multiplicação é: ", result)
    elif OpcSelec == "/":
        result = nmrFirst / nmrSecond
        print("O resultado da divisão é: ", result)
    
    continueGo = input("Para continuar a Operação, digite: s para sair e c para Continuar.")

    if continueGo == "s":
        break
    #if continueGo == "c":