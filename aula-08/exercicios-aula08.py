#Atividade 01
# arquivo a.py
print('executando a')
# arquivo b.py
print('executando b')
# principal.py
#imports
'''Quando importamos um módulo em Python, a primeira coisa que a nossa linguagem 
favorita fará é executar o conteúdo de cada módulo importado.'''

#Atividade 02
# arquivo a.py
def executa():
    print("Executando a")
# arquivo b.py
def executa():
    print("Executando b")
# principal.py
#imports

'''Como os códigos dos arquivo a.py e b.by foram definidos dentro de uma função, 
sendo assim, a importação de a e b por principal não executa automaticamente o 
código contido neles. Para isso, precisamos explicitar que queremos executar esses 
código em principal. '''
#a.executa()
#b.executa()

'''Mesmo um módulo solitário pode executar alguma funcionalidade
 quando executado isoladamente, basta adicionar um if no final 
 do código para verificar a variável __name__:
'''
def executa():
    print("Executando a")

if(__name__ == "__main__"):
    executa()
