#Solicitar dois numeros ao usuario. O programa deve calcular +, -, * e /
numero1 = int(input("Insirir o primeiro valor: "))
numero2= int(input("Inserir o segundo valor: "))


#Guardar o resultado das quatro operaçoes
resultadoSoma= numero1 + numero2
resultadoSubtracao = numero1 - numero2
resultadoMultiplicacao = numero1 * numero2
resultadoDivisao = numero1 / numero2


#Exibir o resultado das operações

print("O resultado da Soma é: ", resultadoSoma)
print("O resultado da Subtração é: ", resultadoSubtracao)
print("O resultado da Multiplicação é: ", resultadoMultiplicacao)
print("O resultado da Divisão é: ", resultadoDivisao)