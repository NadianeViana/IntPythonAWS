#Receber três valores informados pelo usuário e mostrar qual o valor menor entre eles.

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
    print("O menor valor é: ", valor1)
elif valor2 < valor1 and valor2 < valor3:
    print("O menor valor é: ", valor2)
elif valor3 < valor1 and valor3 < valor2:
    print("O menor valor é: ", valor3)
else:
    print("Os valores são os mesmos.")