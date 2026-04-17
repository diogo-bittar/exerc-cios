""" Manipulação de lista """

#Criando uma lista e a sua depreciação de exclusão
inventario = []
resposta = "S"

#Criar um laço de repetição para alocar as informações na lista
while resposta == "S":
    equipamento = [input("Insira o Equipamento: "),
                float(input("Insira o Valor: ")),
                int(input("Insira o Número Serial: ")),
                input("Informe o Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \'S\' para continuar: ").upper()

#Crio um FOR quando sair do primerio laço
for elemento in inventario:
    #Entrou no FOR: exibo as informações
    print("Nome: ", elemento[0])
    print("Valor: ", elemento[1])
    print("Número Serial: ", elemento[2])
    print("Departamento: ", elemento[3])

#Busca e inserção dos produtos
busca = input("\nInforme o nome do equipamento que deseja buscar: ")

#Crio um outro laço com o FOR para o usuário buscar
for elemento in inventario:
    #Crio uma condição com IF
    if busca == elemento[0]: #Se for igual, exibo as informações abaixo
        print("Valor: ", elemento[1])
        print("Número do Serial: ", elemento[2])

#Depreciação 
depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario: 
    if depreciacao == elemento[0]:
        print("O valor anterior: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print(f"O valor atual: {elemento[1]:.2f}")

serial = int(input("Informe o Serial do equipamento que será excluído sistema: ")) #Peço o serial 
for elemento in inventario: #Dentro do inventário eu busco o elemento
    if elemento[2] == serial: #Se elemento 2 for igual ao serial, devo excluir o serial
        inventario.remove(elemento) #remoção

#Exibo na tela as mudanças 
for elemento in inventario:
    print("Nome: ", elemento[0])
    print("Valor: ", elemento[1])
    print("Número Serial: ", elemento[2])
    print("Departamento: ", elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print('O equipamento mais caro custa: ', max(valores))
    print('O equipamento mais barato custa: ', min(valores))
    print('A quantidade de equipamentos é de: ', len(inventario))