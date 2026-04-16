#Puxando biblioteca do random
import random 

#INTRODUÇÃO DO JOGO
print("\t*************************")
print('\t BEM-VINDO AO GAME DEV !')
print("\t*************************")
print(" ")

#Lista do conteúdo do jogo
jogo = [
    {"personagem": "Mordecai", "vida": 100 ,"ataque": (20, 30)},
    {"personagem": "Rigby", "vida": 100, "ataque": (20, 30)}
]

#Exibição do menu de personagem
print("\tPERSONAGENS"
             "\n\t1. MORDECAI"
             "\n\t2.RIGBY")

#Escolha do personagem (com validação)
while True:
    personagem = input("Selecione o seu personagem (Mordecai/Rigby): ").upper()
    
    if personagem == "MORDECAI":
        jogador = jogo[0]
        inimigo = jogo[1]
        break
    elif personagem == "RIGBY":
        jogador = jogo[1]
        inimigo = jogo[0]
        break
    else:
        print('PERSONAGEM NÃO ENCONTRADO.')

#TURNOS (aleatório)
turno = random.randint(1, 2)

if turno % 2 == 1:
    print(f"\n{jogador['personagem']} começa atacando!")
else:
    print(f"\n{inimigo['personagem']} começa atacando!")

#JOGANDO
while jogador["vida"] > 0 and inimigo["vida"] > 0:
    
    if turno % 2 == 1:
        dano = random.randint(jogador["ataque"][0], jogador["ataque"][1]) #EU CHEGUEI ATÉ AQUI. DPS DISSO PEDI AJUDA
        inimigo["vida"] -= dano 
        print(f"{jogador['personagem']} causou {dano} de dano.\nVida de {inimigo['personagem']}: {max(inimigo['vida'], 0)}")
    else:
        dano = random.randint(inimigo["ataque"][0], inimigo["ataque"][1])
        jogador["vida"] -= dano 
        print(f"{inimigo['personagem']} causou {dano} de dano.\nVida de {jogador['personagem']}: {max(jogador['vida'], 0)}")
    
    turno += 1

#RESULTADO FINAL
if jogador["vida"] > 0:
    print(f"\n{jogador['personagem']} venceu!")
else:
    print(f"\n{inimigo['personagem']} venceu!")

#TENHO PONTOS A MELHORAR, NÃO PENSE QUE FIZ TUDO SOZINHO O CÓDIGO. :)