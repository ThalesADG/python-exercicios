def bonus_tipo(tipo_ataque, tipo_defensor):
    multiplicador = 1.0

    if tipo_ataque == "fogo" and tipo_defensor == "grama":
        multiplicador = 2.0
    elif tipo_ataque == "agua" and tipo_defensor == "fogo":
        multiplicador = 2.0
    elif tipo_ataque == "grama" and tipo_defensor == "agua":
        multiplicador = 2.0
    elif tipo_ataque == "eletrico" and tipo_defensor == "agua":
        multiplicador = 2.0

    elif tipo_ataque == "fogo" and tipo_defensor == "agua":
        multiplicador = 0.5
    elif tipo_ataque == "agua" and tipo_defensor == "grama":
        multiplicador = 0.5
    elif tipo_ataque == "grama" and tipo_defensor == "fogo":
        multiplicador = 0.5
    elif tipo_ataque == "agua" and tipo_defensor == "eletrico":
        multiplicador = 0.5

    elif tipo_ataque == "normal":
        multiplicador = 1.0

    return multiplicador


def calcular_dano_final(atacante, defensor):
    poder = atacante[6]
    defesa = defensor[4]
    tipo_ataque = atacante[7]
    tipo_defensor = defensor[1]

    multiplicador = bonus_tipo(tipo_ataque, tipo_defensor)
    dano_base = poder - (defesa / 2)
    dano_final = int(dano_base * multiplicador)

    if dano_final < 1:
        dano_final = 1

    return dano_final, multiplicador


def quem_comeca(jogador, oponente):
    if jogador[8] >= oponente[8]:
        return "jogador"
    else:
        return "oponente"


def realizar_ataque(atacante, defensor, nome_atacante):
    print()
    print(f"{nome_atacante} usa {atacante[5]}!")

    dano, mult = calcular_dano_final(atacante, defensor)

    if mult == 2.0:
        print(f"{atacante[5]} é super efetivo!")
    elif mult == 0.5:
        print(f"{atacante[5]} não é muito efetivo...")

    defensor[3] = defensor[3] - dano

    if defensor[3] < 0:
        defensor[3] = 0

    print(f"Causou {dano} de dano. HP de {defensor[0]} agora é {defensor[3]}/{defensor[2]}.")

    if defensor[3] == 0:
        return True
    else:
        return False


def batalha_principal(time_jogador, time_oponente):
    print()
    print("====================")
    print("A BATALHA VAI COMEÇAR!")
    print("====================")

    derrotados_jog = 0
    derrotados_op = 0
    rodada = 1
    idx_jog = 0
    idx_op = 0

    while derrotados_jog < 4 and derrotados_op < 4:
        p_jog = time_jogador[idx_jog]
        p_op = time_oponente[idx_op]

        print()
        print(f"--- Rodada {rodada} ---")
        print(f"{p_jog[0]}, eu escolho você!")
        print(f"{p_op[0]}, vai!")
        print("--------------------")

        turno = 1

        while p_jog[3] > 0 and p_op[3] > 0:
            print()
            print(f"-- Turno {turno} --")

            primeiro = quem_comeca(p_jog, p_op)

            if primeiro == "jogador":
                oponente_caiu = realizar_ataque(p_jog, p_op, p_jog[0])
                if oponente_caiu == False:
                    jogador_caiu = realizar_ataque(p_op, p_jog, p_op[0] + " do oponente")
                else:
                    jogador_caiu = False
            else:
                jogador_caiu = realizar_ataque(p_op, p_jog, p_op[0] + " do oponente")
                if jogador_caiu == False:
                    oponente_caiu = realizar_ataque(p_jog, p_op, p_jog[0])
                else:
                    oponente_caiu = False

            turno = turno + 1

        print()

        if p_jog[3] == 0:
            print(f"{p_jog[0]} foi derrotado!")
            derrotados_jog = derrotados_jog + 1
            idx_jog = idx_jog + 1
        else:
            print(f"{p_op[0]} do oponente foi derrotado!")
            derrotados_op = derrotados_op + 1
            idx_op = idx_op + 1

        print()
        print("--------------------")
        print()
        print(f"Placar: {derrotados_op} X {derrotados_jog}")
        rodada = rodada + 1

    print()
    if derrotados_op == 4:
        print("========================================")
        print("Parabéns! Você venceu a batalha Pokémon!")
        print("========================================")
    else:
        print("========================================")
        print("Que pena! Você foi derrotado.")
        print("========================================")


def gerar_time_oponente(nome):
    if nome == "lorelei":
        return [
            ["Lapras", "agua", 220, 220, 50, "Raio de Gelo", 60, "agua", 60],
            ["Blastoise", "agua", 180, 180, 55, "Hidro Bomba", 65, "agua", 78],
            ["Victreebel", "grama", 160, 160, 40, "Folha Navalha", 55, "grama", 70],
            ["Ninetales", "fogo", 170, 170, 45, "Lança-chamas", 60, "fogo", 100],
        ]
    elif nome == "bruno":
        return [
            ["Charizard", "fogo", 190, 190, 40, "Presa de Fogo", 70, "fogo", 100],
            ["Arcanine", "fogo", 180, 180, 50, "Velocidade Extrema", 60, "fogo", 95],
            ["Kingler", "agua", 170, 170, 60, "Caranguejo Martelo", 65, "agua", 75],
            ["Jolteon", "eletrico", 150, 150, 35, "Choque do Trovão", 55, "eletrico", 130],
        ]
    elif nome == "agatha":
        return [
            ["Venusaur", "grama", 180, 180, 50, "Raio Solar", 70, "grama", 80],
            ["Vileplume", "grama", 160, 160, 45, "Pó do Sono", 50, "grama", 50],
            ["Raichu", "eletrico", 160, 160, 40, "Investida Trovão", 65, "eletrico", 110],
            ["Poliwrath", "agua", 190, 190, 55, "Soco Dinâmico", 60, "agua", 70],
        ]
    elif nome == "lance":
        return [
            ["Electabuzz", "eletrico", 180, 180, 45, "Soco de Trovão", 75, "eletrico", 105],
            ["Jolteon", "eletrico", 170, 170, 35, "Onda de Trovão", 60, "eletrico", 130],
            ["Exeggutor", "grama", 160, 160, 40, "Bomba de Semente", 65, "grama", 55],
            ["Magmar", "fogo", 175, 175, 40, "Giro de Fogo", 55, "fogo", 93],
        ]
    else:
        return []


def main():
    print("Hora de montar seu time Pokémon!")

    time_jogador = []
    contador = 0

    while contador < 4:
        dados = input().strip()
        partes = dados.split(" - ")
        nome = partes[0]
        tipo = partes[1]
        hp = int(partes[2])
        defesa = int(partes[3])
        ataque_nome = partes[4]
        poder = int(partes[5])
        tipo_ataque = partes[6]
        velocidade = int(partes[7])

        time_jogador.append([nome, tipo, hp, hp, defesa, ataque_nome, poder, tipo_ataque, velocidade])
        contador = contador + 1

    print()
    print("Qual membro da Elite Four você deseja enfrentar?")
    nome_oponente = input().lower()

    time_oponente = gerar_time_oponente(nome_oponente)
    batalha_principal(time_jogador, time_oponente)


main()
