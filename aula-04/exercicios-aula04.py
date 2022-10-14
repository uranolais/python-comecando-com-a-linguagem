#Atividade 01
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2 #Resultado: 1 3 7 9

#Atividade 02
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017
   #Resultado: "Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"
print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))