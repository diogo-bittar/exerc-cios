"""
LAÇO DE REPS --> WHILE
numero = int(input("Informe um número: "))

while numero < 1000:
    print("\t" + str(numero))
    numero = numero+1
print(numero)"""

#----------------------------------

""" LAÇO DE REPS --> FOR 

#PEDIR AO USUÁRIO UM NÚMERO
tabuada = int(input("Qual número você deseja saber a tabuada?: "))

print(f"Tabuada do número:", tabuada)

#LAÇO PARA EXECUTAR E MULTIPLICAR
for valor in range(1,11, 1):
    #EXIBIR A TABUADA 
    print(str(tabuada)+ " x " + str(valor) + " = " + str((tabuada*valor)))
"""
#-------------------------------------
""" VARIÁVEIS E LISTAS """

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
    equipamento.append(input("Equipamento: "))
    valor.append(float(input("Valor: ")))
    serial.append(int(input("Número serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite \"SIM\" para continuar: ").upper()

#EXIBIÇÃO
for indice in range(0, len(equipamento)): #Len é usado para retornar o número de itens (o comprimento) de um objeto
    print("\nEQUIPAMENTO: ", (indice+1))
    print("Nome: ", (equipamento[indice]))
    print("Valor: ", (valor[indice]))
    print("Serial: ", (serial[indice]))
    print("Departamento: ", (departamento[indice]))
