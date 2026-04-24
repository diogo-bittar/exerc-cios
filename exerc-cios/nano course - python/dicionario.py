"""
Aula sobre dicionário -- INTRODUÇÃO

#Criação do nosso dicionário de login
usuarios = {}

#optar colocar no plural quando tiver muitas opções

#Adicionando informações nesse dicionário
usuarios = {
    "chaves" : ["Chaves do 8", "24/12/2017", "Recep_01"],
    "quico" : ["Quico das Flores", "20/12/2017", "Raiox_03"]
}

#Acrescentando mais uma informação de usuário 
usuarios['Florinda'] = ['Dona FLorinda', '24/12/2017', 'Raiox_01']
print(usuarios)

#Get --> Pegar
print('####---####')
print(usuarios.get('quico'))
print(usuarios['quico'])
"""
#-----------------------------------------------------------------
""" 
Aula sobre dicionário em pacotes -- AULA 2
"""

usuarios = {}

opcao = input("Selecione um opção\n"+
              "<I> - Inserir um usuário\n"+
              "<P> - Pesquisar um usuário\n"+
              "<E> - Excluir um usuário\n"+
              "<L> - Listar um usuário").upper()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = print