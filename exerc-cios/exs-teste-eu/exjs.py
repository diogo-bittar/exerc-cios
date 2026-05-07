while True:
    nome = input('Informe o seu nome por favor: ')
    if len(nome) < 3:
        print('O nome precisa ter mais de 2 caracteres.')
    elif not nome.replace(' ', '').isalpha():
        print('O nome deve conter apenas letras.')
    else:
        break