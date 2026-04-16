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
""" VARIÁVEIS E LISTAS 

#CRIAR A LISTA DO QUE EU QUERO
inventario = []

#A RESPOSTA DEVE SER = SIM
resposta = "SIM"

#WHILE 
while resposta == "SIM":
    #APPEND SERVE PARA INSERIR DENTRO DA LISTA ! 
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"SIM\" para continuar: ").upper()

for elemento in inventario:
    print(elemento)
"""