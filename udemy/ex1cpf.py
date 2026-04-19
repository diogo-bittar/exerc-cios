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

cpf = '74682489070'
nove_digitos = cpf[:9]
cont_regressivo_1 = 10
resultado = 0

for digito_um in nove_digitos:
    resultado += int(digito_um) * cont_regressivo_1
    cont_regressivo -= 1

digito_um = (resultado * 10) % 11
digito_um = digito_um if digito_um <= 9 else 0
#----------------------------------------------------