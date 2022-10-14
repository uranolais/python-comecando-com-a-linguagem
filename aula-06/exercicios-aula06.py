#Atividade 01
import random

aleatorio = random.randrange(10)#0 a 9
print(aleatorio)

#Atividade 02
#Numero inteiro de 0 a 100, incluindo 100
int(random.random() * 101)
round(random.random() * 100)
random.randrange(0,101)

#Atividade 03

sorteado = random.randrange(0,4)

print(sorteado)

if sorteado == 1:
    print( "Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires") 
    '''O sorteio foi injusto, afinal os possíveis números retornados são 0, 1, 2 e 3 , 
    e como o Paulo e a Juliana estão associadas a apenas um número cada sobram ainda
     outros dois para Tamires poder ganhar.'''

