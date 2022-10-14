print("*"*32)
print("Bem vindo no jogo de advinhação")
print("*"*32)

numero_secreto = 42

chute_str = input("Digite o seu número: ")
chute = int(chute_str)

print("Você digitou", chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")
         
print("Fim de Jogo")