"""
Validação de login simples
"""

#Crio um dicionário para conter as informações
login = {
    "dege": "1234"
}

username = ""
senha = ""

#eXIBO O MENU 
print("\tBem-Vindo de volta !",
      "\n Selecione uma opção abaixo:",
      "\n1. USERNAME",
      "\n2. SENHA",
      "\n3. SAIR DO SISTEMA")

#Entrada de dados do usuário
menu = input("Digite aqui a opção selecionada. (1/2/3): ")

if menu == "1":
    username = input("Digite o seu username: ")
    
    if username in login:
        print(f"\nQue bom que você está de volta {username}!",
              "\nA seguir, informe  a sua senha.")
        
        senha = input("Digite o seu senha: ")
        
        if senha == login[username]:
            print("Login correto")
        else:
            print("Senha incorreta")
    else:
        print("Usuário não encontrado")