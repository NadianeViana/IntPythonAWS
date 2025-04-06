#Calcular a média aritmética de 3 valores passados pelo usuário. Além disso, calcular a média ponderada destes 3 valores,
#respectivamente por 20%, 30% e 50%.

firstvalue = int(input("Informe o primeiro valor: "))
secondvalue = int(input("Informe o segundo valor: "))
thirdvalue = int(input("Informe o terceiro valor: "))

#Execução das médias aritmética e pondera

somaDeValores = firstvalue + secondvalue + thirdvalue
mediaAritmeticaTotal = somaDeValores / 3
mediaPondFirst = firstvalue * 0.2
mediaPondSecond = secondvalue * 0.3
mediaPondThird = thirdvalue * 0.5
mediaPondTotal = mediaPondFirst + mediaPondSecond + mediaPondThird


#Exibição das médias para o usuário
print("A média aritmética dos 3 três valores solicitado é: ", mediaAritmeticaTotal)
print("O sistema usuou 20%, 30% e 50%, respectivamente, como base para média ponderada total e é: ", mediaPondTotal)