#Contador específico para cada contagem
i_0_25 = 0
i_26_50 = 0
i_51_75 = 0
i_76_100 = 0

while True:
    nmroIntervalo = int(input("Insira um número positivo e inteiro: "))
    if nmroIntervalo < 0 :
        break
    if 0 <= nmroIntervalo <= 25:
        i_0_25 += 1
    elif 26 <= nmroIntervalo <= 50:
        i_26_50 += 1
    elif 51 <= nmroIntervalo <= 75:
        i_51_75 += 1
    elif 76 <= nmroIntervalo <= 100:
        i_76_100 += 1

print("[0,25]", i_0_25)
print("[26,50]", i_26_50)
print("[51,75]", i_51_75)
print("[76,100]", i_76_100)