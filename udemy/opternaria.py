""" 
Operação Ternária --> uma condição de uma linha 

<valor> if <condição> else <outro_valor>
"""

digito = 9 # > 9 = 0

# nv_digito = digito if digito <= 9 else 0 

nv_digito = 0 if digito > 9 else digito

print(nv_digito)