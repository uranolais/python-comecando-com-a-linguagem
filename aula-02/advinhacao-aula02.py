print("*"*32)
print("Bem vindo no jogo de advinhação")
print("*"*32)

numero_secreto = 42

chute = int(input("Digite o seu número: ")) 
#Necessário fazer o casting, visto que por padrão a variável criada durante um input é do tipo string

print("Você digitou", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim de Jogo!")