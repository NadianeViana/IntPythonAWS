#Calcular e Mostrar a área e o perímetro de um retângulo. Usuário informará largura e altura.
larguraR = float(input("Inserir a largura do retângulo: "))
comprimentoR = int(input("Inserir o comprimento: "))


#Guardar o resultado
areaR = larguraR * comprimentoR
perimetroR = larguraR + larguraR + comprimentoR + comprimentoR


#Exibir resultado
print("A área do retângulo é: ", areaR)
print("O perímetro do retângulo é: ", perimetroR)
