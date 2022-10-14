#Atividade 01
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:#Quando o usuário digitar 12, nenhuma condição será satisfeita! Portanto, não aparecerá nada
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")

#Atividade 02
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12 #Ao digitar 15, o valor das variáveis será false, false, true

#Atividade 03
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
else(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
else(usuario == "Nico"):#O código dava errado pois não se utiliza mais de um else, nem coloca condição no else
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")#Para funcionar, deve ser trocado os dois primeiros else por elif