#Deverá ler e armazenar dois números informados pelo usuário. Os valores deverão ter usa ordem trocada.

valor1 = int(input("Por favor, informe o primeiro valor: "))
valor2 = int(input("Por favor, informe o segundo valor: "))

#Troca da ordem dos números deverá ocorrer aqui.

#usei este código como referência antes de pesquisar
#valor3 = valor2
#valor2 = valor1
#valor1 = valor3

valor1, valor2 = valor2, valor1


#Mostra a mudança na ordem dos números.
print("O atual primeiro valor é: ", valor1)
print("O atual segundo valor é: ", valor2)