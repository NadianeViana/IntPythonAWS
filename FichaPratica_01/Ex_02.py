#Calcular imposto sobre o valor informado pelo usuário

salarioFuncBruto = int(input("Informe o valor do salário bruto: "))

if salarioFuncBruto <= 15000:
    imposto = 0.2
    print("O desconto salarial é de 20%")
else:
    imposto = 0.3
    print("O desconto salarial é de 30%")

descSalario = salarioFuncBruto * imposto
salarioFuncLiq = salarioFuncBruto - descSalario

print("O valor do desconto é: ", descSalario)
print("O valor líquido do seu salário a recebe é: ", salarioFuncLiq)

