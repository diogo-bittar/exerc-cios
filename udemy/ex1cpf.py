""" 
Exercício para calcular os últimos dígitos de um CPF --> VALIDAR

CPF: 746.824.890-70

Preciso coletar os 9 primeiros números e fazer a multiplicação de cada um (começo do 10)


Cálculo do 1o dígito do CPF
ex: 
    10  9   8   7   6   5   4   3   2   
*   7   4   6   8   2   4   8   9   0
------------------------------------------
    70  36  48  56  12  20  32  27  0 = 301

Após a multiplicação --> somar os resultados

= 301 

Multiplico o resultado por 10 --> 3010 

3010 % 11 = 7

Obeter o resto da divisão da conta anterior por 11

Se o resultado for maior que 9:
    resultado é 0
contrário disso:
    resultado se mantém

O 1o dígito é 7.
"""

#CÁLCULO DO 1o DÍGITO

#Replace --> serve para substituir valores por outro

#Também consigo importar uma função chamada RE para tirar tudo que eu quiser

import re

#Importar um método para sair do python
import sys 

"""cpf_enviado = '746.824.890-70' \
    .replace(".", "") \
    .replace(" ", "") \
    .replace("-", " ")"""

entrada = input('CPF[786.824.890-70]: ')
#Utilizando a função RE
cpf_enviado = re.sub(
    r'[^0-9]', #retirar tudo aquilo que não for um número. ^
    '',
    entrada
)

entrada_sequencial = entrada == entrada[0] * len(entrada) #verificando se o usuário enviou dados sequenciais 

if entrada_sequencial: #caso tenha enviado --> sair 
    sys.exit()

nove_digitos = cpf_enviado[:9]
cont_regressivo_1 = 10
resultado1 = 0

for digito in nove_digitos:
    resultado1 += int(digito) * cont_regressivo_1
    cont_regressivo_1 -= 1

digito_um = (resultado1 * 10) % 11
digito_um = digito_um if digito_um <= 9 else 0
#----------------------------------------------------
dez_digitos = nove_digitos + str(digito_um)
resultado2 = 0
cont_regressivo2 = 11
for digito in dez_digitos:
    resultado2 += int(digito) * cont_regressivo2
    cont_regressivo2 -= 1
digito_dois = resultado2 * 10 % 11
digito_dois = digito_dois if digito_dois <= 9 else 0 

cpf_gerado = f'{nove_digitos}{digito_um}{digito_dois}'

if cpf_enviado == cpf_gerado:
    print(f'O CPF {cpf_enviado} é válido.')
else:
    print('O CPF é inválido.')

#Dar uma revisada depois nesse exercício e tentar recriar do 0

