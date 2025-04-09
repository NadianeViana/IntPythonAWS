#Três notas informadas pelo usuário. Calcular média ponderada. Média superior a 9.5 é aprovação

nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota: "))

prevMediaNota1 = nota1 * 0.25
prevMediaNota2 = nota2 * 0.35
prevMediaNota3 = nota3 * 0.4
somaNotasMed = prevMediaNota1 + prevMediaNota2 + prevMediaNota3

if somaNotasMed > 9.5:
    print("Parabéns, você foi aprovado!")
else:
    print("Infelizmente, não foste aprovador.")