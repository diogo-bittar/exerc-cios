""" FUNÇÕES E MODULARIZAÇÃO """
#def -> vc atribui uma função 

def preencherInventario(lista): #Essa função fica responsável por pegar as informações
    resp = "S"
    while resp == "S":
        equipamento = [input("Informe o Equipamento: "),
                       float(input("Informe o valor: ")),
                       int(input("Informe o Serial: ")),
                       input("Informe o Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()
#
def exibirInventario(lista):
    for elemento in lista:
        print("Nome: ", elemento[0])      
        print("Valor: ", elemento[1])      
        print("Serial: ", elemento[2])      
        print("Departamento: ", elemento[3])
#
def localizarNome(lista):
    for elemento in lista:
        busca = input("\nDigite o nome do equipamento que deseja buscar: ")
        for elemento in lista:
            if busca == elemento[0]:
                print("Valor: ", elemento[1])
                print("Serial: ", elemento[2])
#
def depreciarPorNome(lista, porc):
    depreciacao = input("Informe o nome do equipamento que deseja depreciar: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print('Valor antigo: ', elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print('Novo valor: ', elemento[1])
#
def excluirPorSerial(lista):
    serial = int(input("Informe o serial do equipamento que será excluído: "))
    for elemento in lista:
        if elemento == serial:
            lista.remove(elemento)
    return "Item excluído com sucesso !"
#
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

