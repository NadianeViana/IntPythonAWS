#Calcular imposto sobre salário anual de acordo com o valor informado pelo usuário

salarioBruto = int(input("Por favor, informe o valor do Salário Bruto: "))

if salarioBruto <= 15000:
    imposto = 0.2
    print("O desconto sobre seu salário é de 20%")
elif salarioBruto < 20000:
    imposto = 0.3
    print("O desconto sobre seu salário é de 30%")
elif salarioBruto <= 25000:
    imposto = 0.35
    print("O desconto sobre seu salário é de 35%")
else:
    imposto = 0.4
    print("O desconto sobre seu salário é de 40%")

descSalario = salarioBruto * imposto
salarioLiqFunc = salarioBruto - descSalario

print("O valor do desconto sobre seu salário é: ", descSalario)
print("O valor líquido salarial a receber é: ", salarioLiqFunc)


