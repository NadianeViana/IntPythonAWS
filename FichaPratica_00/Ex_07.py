#Calcular o preço de 3 produtos e ao final, dar desconto de 10% sobre o valor a pagar

produto1 = float(input("Por favor, infome o valor do primeiro produto: "))
produto2 = float(input("Por favor, informe o valor do segundo produto: "))
produto3 = float(input("Por favor, informe o valor do terceiro produto: "))

#Fazer o somatório da compra e aplicar o desconto

valorBruto = produto1 + produto2 + produto3
valorDoDesconto = valorBruto * 0.1
valorLiquido = valorBruto - valorDoDesconto



#Exibir o valor a pagar já deduzido o desconto

print("O valor a pagar é: ", valorLiquido)