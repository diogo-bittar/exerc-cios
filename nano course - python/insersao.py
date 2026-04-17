""" Inserção e busca de dados """

#CRIAR A LISTA DO QUE EU QUERO
equipamento = []
valor = []
serial = []
departamento = []

#A RESPOSTA DEVE SER = SIM
resposta = "SIM"

#WHILE 
while resposta == "SIM":
    #APPEND SERVE PARA INSERIR DENTRO DA LISTA ! 
    equipamento.append(input("Insira o Equipamento: "))
    valor.append(float(input("Insira o Valor: ")))
    serial.append(int(input("Insira o Número serial: ")))
    departamento.append(input("Insira o Departamento: "))
    resposta = input("Digite \"SIM\" para continuar: ").upper()

#EXIBIÇÃO
for indice in range(0, len(equipamento)): #Len é usado para retornar o número de itens (o comprimento) de um objeto
    print("\nEQUIPAMENTO: ", (indice+1))
    print("Nome: ", (equipamento[indice]))
    print("Valor: ", (valor[indice]))
    print("Serial: ", (serial[indice]))
    print("Departamento: ", (departamento[indice]))

#Parte da busca de equipamento após saída do WHILE
busca = input("\nDigite o nome do equipamento que você deseja buscar: ")

#Agora eu crio um laço com o FOR e jogo um IF 
for i in range(0,len(equipamento)):
    if busca == equipamento[indice]: #Caso a BUSCA for igual a Equipamento
        print("Valor: ", valor[indice]) #Exibo o valor e o serial do equipamento
        print("Serial: ", serial[indice])
        break