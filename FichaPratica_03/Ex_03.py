#Criar jogo

mnrJogador = int(input("Digite um número inteiro positivo de 0 a 100: "))


i = 0

for _ in range(12):
    i += 1
    palpiteJog =int(input("Adivinhe qual é o número correto: "))
    if palpiteJog < mnrJogador:
        print("O número secreto é maior!")
    elif palpiteJog > mnrJogador:
        print("O número secreto é menor!")
    else:
        print("Acertou, miserável!!!! Após a quantidade de tentativas: ", i, "O número secreto é: ", mnrJogador)
        break