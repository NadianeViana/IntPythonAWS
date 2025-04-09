#Pedir dois números ao usuário. Exibir e especificar qual é o menor e qual é o maior.

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

if valor1 > valor2:
    print(valor1 , valor2)
elif valor1 < valor2:
    print(valor2 , valor1)
else:
    print("O valores são iguais")