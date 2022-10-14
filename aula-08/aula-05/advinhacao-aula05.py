print("*"*32)
print("Bem vindo no jogo de advinhação")
print("*"*32)

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}:".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or chute>100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto 
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
    
         
print("Fim de Jogo")