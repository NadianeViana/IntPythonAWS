soma = 0
cont = 0

#Condição de parada do ciclo
while True:
    nmroUsuario = int(input("Insira um número: "))
    if nmroUsuario == -1:
        break
    soma += nmroUsuario
    cont += 1
    if cont > 0:
        media = soma / cont
        print("Média = ", media)