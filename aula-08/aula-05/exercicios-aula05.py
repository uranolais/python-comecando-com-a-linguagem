#Atividade 01
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 1

for contador in range (1,11):
    print(contador)

#Atividade 02
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3

for contador in range(1,11,3):
    print(contador)

#Atividade 03
i = 1
while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break #A saída será de 1 a 4

#Atividade 04
for i in range(1,8):
    if(i == 5):
        continue
    print(i)#Pulamos apenas a iteração 5.

#Atividade 05
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))

#Atividade 06
print("R$ {:7.1f}".format(1000.12)) #R$  1000.1
print("R$ {:07.2f}".format(4.11)) #R$ 0004.11
