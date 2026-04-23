"""
Aula sobre dicionário 
"""
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
print('###---###')
print(usuarios.get('quico'))