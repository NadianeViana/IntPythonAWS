#Calcular a duração de 5 músicas de um álbum musical após o usuário informar a temporização. Especificar cada min e seg.

faixa1min = int(input("Inserir os minutos da Faixa 1: "))
faixa1seg = int(input("Inserir os segundos da Faixa 1: "))
faixa2min = int(input("Inserir os minutos da Faixa 2: "))
faixa2seg = int(input("Inserir os segundos da Faixa 2: "))
faixa3min = int(input("Inserir os minutos da Faixa 3: "))
faixa3seg = int(input("Inserir os segundos da Faixa 3: "))
faixa4min = int(input("Inserir os minutos da Faixa 4: "))
faixa4seg = int(input("Inserir os segundos da Faixa 4: "))
faixa5min = int(input("Inserir os minutos da Faixa 5: "))
faixa5seg = int(input("Inserir os segundos da Faixa 5: "))


#Fazer o cálculo e conversão das horas, minutos e segundos.

faixaSegundos = faixa1seg + faixa2seg + faixa3seg + faixa4seg + faixa5seg
faixaMinutos = faixa1min + faixa2min + faixa3min + faixa4min + faixa5min

segundos=faixaSegundos%60
somaMinutos= faixaSegundos//60
faixaMinutos = faixaMinutos + somaMinutos
horas = faixaMinutos//60
minutos = faixaMinutos%60


#Exibir tempo total com divisão de horas, minutos e segundos

print("O tempo total do álbum é: ",horas,"h",minutos,"m",segundos,"s")