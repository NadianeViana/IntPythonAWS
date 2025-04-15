#Receber a quantidade de números e os números. Verificar ordem crescente.

qntNmeros = int(input("Insira a quantidade de números que deseja: "))
# nmrUsuario = int(input("Digite um número inteiro: "))

i = 0
numaGuardar = 0

flag = True

while i < qntNmeros:    
    nmrUsuario = int(input("Digite um número inteiro: "))    
    if nmrUsuario < numaGuardar :
        flag = False
    i += 1
    numaGuardar = nmrUsuario

if flag == False :
    print("Decrescente")
else:
    print("Crescente")