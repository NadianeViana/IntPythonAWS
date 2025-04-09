#Menu indicado pelo usuário

menuInterativo = int(input("Escolha o serviço desejado. 1 - Criar. 2 - Atualizar. 3 - Eliminar. 4 - Sair."))

if menuInterativo == 1:
    print("Criar")
elif menuInterativo == 2:
    print("Atualizar")
elif menuInterativo == 3:
    print("Eliminar")
elif menuInterativo == 4:
    print("Sair")
else:
    print("Erro")