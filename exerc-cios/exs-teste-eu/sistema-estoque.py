""" Sistema de Estoque """

estoque = []

# ---------------- CADASTRAR ----------------
def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    try:
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor: "))
    except:
        print("Erro: digite números válidos.")
        return

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "valor": valor
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso.")

# ---------------- LISTAR ----------------
def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
        return

    for produto in estoque:
        print(f"\nProduto: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Valor: R$ {produto['valor']:.2f}")
        print("-" * 20)

# ---------------- BUSCAR ----------------
def buscar_produto():
    busca = input("Digite o nome do produto: ").strip().lower()

    for produto in estoque:
        if produto['nome'].lower() == busca:
            print(f"\nProduto encontrado:")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Valor: R$ {produto['valor']:.2f}")
            return

    print("Produto não encontrado.")

# ---------------- ATUALIZAR ----------------
def atualizar_quantidade():
    listar_produtos()
    busca = input("Produto para atualizar: ").strip().lower()

    for produto in estoque:
        if produto['nome'].lower() == busca:
            try:
                nova_qtd = int(input("Nova quantidade: "))
            except:
                print("Erro: valor inválido.")
                return

            if nova_qtd < 0:
                print("Quantidade não pode ser negativa.")
            else:
                produto['quantidade'] = nova_qtd
                print("Quantidade atualizada.")
            return

    print("Produto não encontrado.")

# ---------------- REMOVER ----------------
def remover_produto():
    listar_produtos()
    busca = input("Produto para remover: ").strip().lower()

    for produto in estoque:
        if produto['nome'].lower() == busca:
            estoque.remove(produto)
            print("Produto removido.")
            return

    print("Produto não encontrado.")

# ---------------- VALOR TOTAL ----------------
def valor_total():
    total = 0

    for produto in estoque:
        total += produto['quantidade'] * produto['valor']

    print(f"Valor total do estoque: R$ {total:.2f}")

# ---------------- MENU ----------------
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar quantidade")
        print("5 - Remover produto")
        print("6 - Valor total")
        print("7 - Sair")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                cadastrar_produto()
            case "2":
                listar_produtos()
            case "3":
                buscar_produto()
            case "4":
                atualizar_quantidade()
            case "5":
                remover_produto()
            case "6":
                valor_total()
            case "7":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

# EXECUTAR
menu()