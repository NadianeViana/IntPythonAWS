nmroUsuario = int(input("Insira um número maior que 2: "))

nmroUsuario = 1

#Condição assertiva para número maior que 2
if nmroUsuario > 2:
    cont = 2
    while cont <= nmroUsuario:
        print(cont)
        cont += 2
        