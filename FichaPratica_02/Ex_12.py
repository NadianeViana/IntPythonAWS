#Ler dois números e imprimir múltiplos de 5

nmroInicial = int(input("Digitar o início do intetvalo: "))
nmroFinal = int(input("Digitar o final do intervalo: "))

i = nmroInicial

while i >= nmroInicial and i <= nmroFinal:
    if i % 5 == 0:
        print(i)
    
    i += 1
