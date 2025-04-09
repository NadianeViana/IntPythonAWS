#Exibirá a quantidade de pontos do piloto após usuário declarar a posição do mesmo.

posicaoAtualPilot = int(input("Posição atual do piloto: "))

if posicaoAtualPilot == 1:
    pontos = 10
    print("O total de pontos do piloto é: ", pontos)
elif posicaoAtualPilot == 2:
    pontos = 8
    print("O total de pontos do piloto é: ", pontos)
elif posicaoAtualPilot == 3:
    pontos = 6
    print("O total de pontos do piloto é: ", pontos)
elif posicaoAtualPilot == 4:
    pontos = 5
    print("O total de pontos do piloto é: ", pontos)
elif posicaoAtualPilot == 6:
    pontos = 3
    print("O total de pontos do piloto é: ", pontos)
elif posicaoAtualPilot == 7:
    pontos = 2
    print("O total de pontos do piloto é: ", pontos)
elif posicaoAtualPilot <= 8:
    pontos = 1
    print("O total de pontos do piloto é: ", pontos)
else:
    print("A posição atual do piloto é: ", posicaoAtualPilot)
    print("Não ganhaste pontos. Desculpe.")