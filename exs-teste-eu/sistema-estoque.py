""" Desenvolver um sistema de estoque """

#CRIAR a lista para armazenar o estoque
estoque = []

#Criar uma função para o cadastro
def informarProduto(estoque):
    nome = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade deste produto: "))
    valor = float(input("Informe o valor deste produto: "))
    produto = {
        "nome": nome,
        "quantidade":quantidade,
        "valor": valor
    }
    estoque.append(produto)
    print("Produto cadastrado com sucesso !")

#Listar produtos 
def listarProdutos(estoque):
    if len(estoque) == 0:
        print("Estoque vazio.")
    else: 
        for produto in estoque:
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: {produto['valor']:.2f}")
            print("-" * 20)

#Atualizar a quantidade
def atualizarQuantidade(estoque):
    busca = input("Qual produto você deseja atualizar?: ")
    encontrado = False

    for produto in estoque:
        if produto['nome'] == busca:
            nova_quantidade = int(input("Informe a nova quantidade: "))

            if nova_quantidade < 0:
                print("Quantidade inválida.")
            else:
                produto['quantidade'] = nova_quantidade
                print("Quantidade atualizada com sucesso !")

            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado. :(")

#Remover o produto
def removerProduto(estoque):
    busca = input("Qual produto você deseja remover?: ")
    encontrado = False

    for produto in estoque:
        if produto['nome'] == busca:
            estoque.remove(produto)
            print("Produto removido com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado.")