#Apresentar menu de opções para escolha do usuário e Opção para sair do menu

#menuOpc = int(input("Digite a Opção desejada se 1 - Criar. 2 - Atualizar. 3 - Eliminar. 4 - Sair."))

for _ in range(40):
    print("Menu de Opções: ")
    print("1 - Criar: ")
    print("2 - Atualizar: ")
    print("3 - Eliminar: ")
    print("4 - Sair: ")

    opcUser = input("Escolha a opção desejada: ")

    if opcUser == "1":
        print("Opção Selecionada 1 - Criar.")
    elif opcUser == "2":
         print("Opção Selecionada 2 - Atualizar.")
    elif opcUser == "3":
         print("Opção Selecionada 3 - Eliminar.")
    elif opcUser == "4":
        print("Opção Selecionada 4 - Sair.")
        break
    else:
        print("Opção Inválida!")
    