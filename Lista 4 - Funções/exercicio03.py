print("Hora de Lutar contra a Historia!")
print()

vida_fatalis = 1800
vida_gs = 200
vida_gi = 200
vida_fa = 200

def ataque_greatsword(acao, vida_inimigo):
    dano = 0
    if acao == "Golpe Carregado":
        dano = 165
    elif acao == "Corte Largo":
        dano = 120
    elif acao == "Divisor de Mundos":
        dano = 200
    return vida_inimigo - dano

def ataque_fuzil_arco(acao, vida_inimigo):
    if acao == "Tiro Carregado":
        vida_inimigo -= 90
    elif acao == "Bala de Penetração":
        vida_inimigo -= 120
    elif acao == "Tiro Devastador":
        vida_inimigo -= 150
    return vida_inimigo

def ataque_glaive_inseto(acao, vida_inimigo, vida_caçador):
    if acao == "Corte Aéreo":
        vida_inimigo -= 100
    elif acao == "Descida Carregada":
        vida_inimigo -= 120
    elif acao == "Kinseto":
        cor = input()
        if cor == "Vermelho":
            vida_inimigo -= 40
        elif cor == "Amarelo":
            vida_inimigo -= 15
        elif cor == "Verde":
            vida_caçador += 40
    return vida_inimigo, vida_caçador

def ataque_fatalis(acao, v1, v2, v3, s1="Desprotegido", s2="Desprotegido", s3="Desprotegido"):
    if acao == "Ataque com Cauda":
        if v1 > 0: v1 -= 55
        if v2 > 0: v2 -= 55
        if v3 > 0: v3 -= 55
    elif acao == "Bola de Fogo":
        if v1 > 0: v1 -= 65
        if v2 > 0: v2 -= 65
        if v3 > 0: v3 -= 65
    elif acao == "Mar de Chamas Negras":
        if v1 > 0 and s1 == "Desprotegido": v1 = 0
        if v2 > 0 and s2 == "Desprotegido": v2 = 0
        if v3 > 0 and s3 == "Desprotegido": v3 = 0
    return v1, v2, v3

for rodada in range(4):
    if vida_gs > 0 and vida_fatalis > 0:
        acao1 = input()
        vida_fatalis = ataque_greatsword(acao1, vida_fatalis)

    if vida_gi > 0 and vida_fatalis > 0:
        acao2 = input()
        vida_fatalis, vida_gi = ataque_glaive_inseto(acao2, vida_fatalis, vida_gi)

    if vida_fa > 0 and vida_fatalis > 0:
        acao3 = input()
        vida_fatalis = ataque_fuzil_arco(acao3, vida_fatalis)

    if vida_fatalis > 0 and (vida_gs > 0 or vida_gi > 0 or vida_fa > 0):
        acao_fatalis = input()

        if acao_fatalis == "Mar de Chamas Negras":
            s1 = input()
            s2 = input()
            s3 = input()
            vida_gs, vida_gi, vida_fa = ataque_fatalis(
                acao_fatalis, vida_gs, vida_gi, vida_fa, s1, s2, s3
            )
        else:
            vida_gs, vida_gi, vida_fa = ataque_fatalis(acao_fatalis, vida_gs, vida_gi, vida_fa)

if vida_fatalis > 0:
    print("O Fatalis conseguiu sobreviver ao combate...")
    print("O mundo corre perigo!")
else:
    print("Eu não acredito, vocês conseguiram!")
    print("Obrigado caçadores! O mundo está salvo.")
