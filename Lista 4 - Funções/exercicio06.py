def poder_golpe(nome_golpe):
    magico_leve = ["Zio", "Garu", "Agi", "Bufu"]
    magico_medio = ["Zionga", "Garula", "Agilao", "Bufula"]
    fisico_leve = ["Corte", "Perfuração", "Pancada"]

    i = 0
    while i < len(magico_leve):
        if nome_golpe == magico_leve[i]:
            return 3
        i = i + 1

    i = 0
    while i < len(magico_medio):
        if nome_golpe == magico_medio[i]:
            return 5
        i = i + 1

    i = 0
    while i < len(fisico_leve):
        if nome_golpe == fisico_leve[i]:
            return 4
        i = i + 1

    return 0


def calcular_dano(poder_base, atk_usuario):
    return int(((poder_base * 15) ** 0.5) * (atk_usuario / 2.0))


def lista_ordenada_crescente(v):
    i = 1
    ok = 1
    while i < len(v):
        if v[i] < v[i - 1]:
            ok = 0
        i = i + 1
    return ok


def lista_ordenada_decrescente(v):
    i = 1
    ok = 1
    while i < len(v):
        if v[i] > v[i - 1]:
            ok = 0
        i = i + 1
    return ok


def bubble_swaps(v, asc):
    a = v[:]
    n = len(a)
    trocas = 0
    fim = n - 1
    trocou = 1
    while trocou == 1:
        trocou = 0
        i = 0
        while i < fim:
            cond = 0
            if asc == 1:
                if a[i] > a[i + 1]:
                    cond = 1
            else:
                if a[i] < a[i + 1]:
                    cond = 1
            if cond == 1:
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                trocas = trocas + 1
                trocou = 1
            i = i + 1
        fim = fim - 1
    return trocas


def resultado_bubblesort(v):
    if lista_ordenada_crescente(v) == 1 or lista_ordenada_decrescente(v) == 1:
        return "fraqueza"
    t1 = bubble_swaps(v, 1)
    t2 = bubble_swaps(v, 0)
    m = t1
    if t2 < m:
        m = t2
    if m <= 5:
        return "acerto"
    return "erro"


def primeiro_alvo_ativo(sombras):
    i = 0
    while i < len(sombras):
        if sombras[i][4] != "Derrotado" and sombras[i][4] != "Derrubado":
            return i
        i = i + 1
    return -1


def existe_vivo(sombras):
    i = 0
    while i < len(sombras):
        if sombras[i][4] != "Derrotado":
            return 1
        i = i + 1
    return 0


def todos_vivos_derrubados(sombras):
    i = 0
    algum = 0
    todos = 1
    while i < len(sombras):
        if sombras[i][4] != "Derrotado":
            algum = 1
            if sombras[i][4] != "Derrubado":
                todos = 0
        i = i + 1
    if algum == 1 and todos == 1:
        return 1
    return 0


def encontrar_proxima_sombra_para_agir(pointer, sombras):
    if len(sombras) == 0:
        return -1
    cont = 0
    pos = pointer
    achou = -1
    while cont < len(sombras) and achou == -1:
        if sombras[pos][4] != "Derrotado":
            achou = pos
        else:
            pos = pos + 1
            if pos >= len(sombras):
                pos = 0
        cont = cont + 1
    return achou


def imprimir_relatorio(turno, hp_makoto, sombras):
    print(f"TURNO {turno}:")
    print(f"HP Makoto: {hp_makoto} / 300")
    i = 0
    while i < len(sombras):
        if sombras[i][4] != "Derrotado":
            print(f"HP {sombras[i][0]}: {sombras[i][1]} pontos de vida restantes")
        i = i + 1


def ler_entrada():
    return input()


def turno_sombra(makoto_hp, sombras, j):
    if sombras[j][4] == "Derrubado":
        sombras[j][4] = "Ativo"
    poder = poder_golpe(sombras[j][3])
    dano = calcular_dano(poder, sombras[j][2])
    makoto_hp = makoto_hp - dano
    print(f"Mitsuru: Makoto foi atacado por {sombras[j][0]} e recebeu {dano} de dano!")
    prox = j + 1
    if prox >= len(sombras):
        prox = 0
    morreu = 0
    if makoto_hp <= 0:
        morreu = 1
    return [makoto_hp, prox, morreu]


def turno_makoto(makoto_hp, makoto_mp, persona_nome, persona_atk, persona_golpe, persona_custo, sombras, usos_yukari, usos_junpei):
    print("Makoto: O que fazer...")
    acao_executada = 0
    mais_um = 0
    fim_batalha = 0
    while acao_executada == 0:
        entrada = ler_entrada()
        cmd = entrada.lower()

        if cmd == "yukari":
            if usos_yukari > 0:
                print("Yukari: Aguenta ai, líder!")
                print("Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado")
                makoto_hp = makoto_hp + 100
                if makoto_hp > 300:
                    makoto_hp = 300
                usos_yukari = usos_yukari - 1
                acao_executada = 1
            else:
                print("Yukari: Estou exausta, foi mal!")

        elif cmd == "junpei":
            if usos_junpei > 0:
                alvo = primeiro_alvo_ativo(sombras)
                if alvo != -1:
                    print("Junpei: HOOOOOME RUUUUN!!")
                    print(f"Mitsuru: Acerto CRÍTICO de Junpei! {sombras[alvo][0]} sofreu 100 de dano!")
                    sombras[alvo][1] = sombras[alvo][1] - 100
                    if sombras[alvo][1] <= 0:
                        sombras[alvo][1] = 0
                        sombras[alvo][4] = "Derrotado"
                        print(f"Mitsuru: {sombras[alvo][0]} foi derrotado!")
                    else:
                        sombras[alvo][4] = "Derrubado"
                    usos_junpei = usos_junpei - 1

                    if existe_vivo(sombras) == 0:
                        mais_um = 0
                    elif todos_vivos_derrubados(sombras) == 1:
                        print("Mitsuru: Todos os inimigos cairam! Avancem com tudo!")
                        print("MASS DESTRUCTION!")
                        fim_batalha = 1
                        mais_um = 0
                    else:
                        mais_um = 1
                        print("MAIS UM!")
                        print("Mitsuru: Você acertou uma fraqueza! Continue no ataque!")
                    acao_executada = 1
                else:
                    acao_executada = 1
            else:
                print("Junpei: Cara, tô cansado!")

        elif cmd == "atacar":
            alvo = primeiro_alvo_ativo(sombras)
            if alvo != -1:
                dano = calcular_dano(2, persona_atk)
                sombras[alvo][1] = sombras[alvo][1] - dano
                print(f"Mitsuru: Makoto acertou {sombras[alvo][0]} causando {dano} de dano!")
                if sombras[alvo][1] <= 0:
                    sombras[alvo][1] = 0
                    sombras[alvo][4] = "Derrotado"
                    print(f"Mitsuru: {sombras[alvo][0]} foi derrotado!")
                acao_executada = 1
            else:
                acao_executada = 1

        elif cmd == "persona":
            if makoto_mp >= persona_custo:
                lista_str = ler_entrada()
                partes = lista_str.split()
                valores = []
                i = 0
                while i < len(partes) and len(valores) < 6:
                    s = partes[i]
                    sinal = 1
                    p = 0
                    if len(s) > 0 and s[0] == '-':
                        sinal = -1
                        p = 1
                    num = 0
                    while p < len(s):
                        ch = s[p]
                        dig = int(ch)
                        num = (num * 10) + dig
                        p = p + 1
                    valores.append(sinal * num)
                    i = i + 1
                while len(valores) < 6:
                    valores.append(0)

                resultado = resultado_bubblesort(valores)
                makoto_mp = makoto_mp - persona_custo

                if resultado == "erro":
                    print("Makoto: O quê?!")
                    print("Mitsuru: Mais foco, Makoto!")
                    acao_executada = 1

                else:
                    alvo = primeiro_alvo_ativo(sombras)
                    if alvo != -1:
                        base = poder_golpe(persona_golpe)
                        if resultado == "fraqueza":
                            dano = int(((base * 15) ** 0.5) * (persona_atk / 2.0) * 1.5)
                        else:
                            dano = calcular_dano(base, persona_atk)

                        if resultado == "fraqueza":
                            print(f"Makoto: Venha {persona_nome}!")
                        else:
                            print("Makoto: Persona!")

                        sombras[alvo][1] = sombras[alvo][1] - dano
                        print(f"Mitsuru: Makoto acertou {sombras[alvo][0]} causando {dano} de dano!")
                        morreu = 0
                        if sombras[alvo][1] <= 0:
                            sombras[alvo][1] = 0
                            sombras[alvo][4] = "Derrotado"
                            morreu = 1
                            print(f"Mitsuru: {sombras[alvo][0]} foi derrotado!")
                        else:
                            if resultado == "fraqueza":
                                sombras[alvo][4] = "Derrubado"

                        if resultado == "fraqueza":
                            if existe_vivo(sombras) == 0:
                                mais_um = 0
                            elif todos_vivos_derrubados(sombras) == 1:
                                print("Mitsuru: Todos os inimigos cairam! Avancem com tudo!")
                                print("MASS DESTRUCTION!")
                                fim_batalha = 1
                                mais_um = 0
                            else:
                                mais_um = 1
                                print("MAIS UM!")
                                print("Mitsuru: Você acertou uma fraqueza! Continue no ataque!")
                        acao_executada = 1
                    else:
                        acao_executada = 1
            else:
                print("Makoto: Estou cansado...")

        else:
            a = 0

    return [makoto_hp, makoto_mp, sombras, usos_yukari, usos_junpei, mais_um, fim_batalha]


def combate(persona_info, hp, mp):
    persona_nome = persona_info[0]
    persona_atk = persona_info[1]
    persona_golpe = persona_info[2]
    persona_custo = persona_info[3]

    num_sombras = int(ler_entrada())

    sombras = []
    i = 0
    while i < num_sombras:
        linha = ler_entrada()
        partes = linha.split(" - ")
        nome = partes[0].strip()
        vida = int(partes[1].strip())
        ataque = int(partes[2].strip())
        golpe = partes[3].strip()
        sombras.append([nome, vida, ataque, golpe, "Ativo"])
        i = i + 1

    print("Mitsuru: Inimigos detectados, se preparem!")

    usos_yukari = 2
    usos_junpei = 1
    turno = 1
    pointer_sombra = 0

    acabou = 0
    morreu = 0

    while acabou == 0 and morreu == 0:
        t = turno_makoto(hp, mp, persona_nome, persona_atk, persona_golpe, persona_custo, sombras, usos_yukari, usos_junpei)
        hp = t[0]
        mp = t[1]
        sombras = t[2]
        usos_yukari = t[3]
        usos_junpei = t[4]
        mais_um = t[5]
        fim_batalha = t[6]

        if fim_batalha == 1 or existe_vivo(sombras) == 0:
            print("Mitsuru: Muito bem! Continuem a exploração.")
            hp = hp + 50
            if hp > 300:
                hp = 300
            mp = mp + 15
            if mp > 70:
                mp = 70
            return [hp, mp, 1, 0]

        if mais_um == 1:
            imprimir_relatorio(turno, hp, sombras)
            turno = turno + 1
        else:
            j = encontrar_proxima_sombra_para_agir(pointer_sombra, sombras)
            if j == -1:
                print("Mitsuru: Muito bem! Continuem a exploração.")
                hp = hp + 50
                if hp > 300:
                    hp = 300
                mp = mp + 15
                if mp > 70:
                    mp = 70
                return [hp, mp, 1, 0]
            res = turno_sombra(hp, sombras, j)
            hp = res[0]
            pointer_sombra = res[1]
            morreu = res[2]
            if morreu == 1:
                print("Makoto: Argh...")
                print("Mitsuru: Líder? Aconteceu algo? Responda!")
                return [hp, mp, 0, 1]
            imprimir_relatorio(turno, hp, sombras)
            turno = turno + 1

    return [hp, mp, 0, 0]


print("Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.")

hp = 300
mp = 70
andares = 0
morreu = 0

while morreu == 0:
    linha_persona = ler_entrada()
    
    partes = linha_persona.split(" - ")
    if len(partes) >= 4:
        persona_nome = partes[0].strip()
        persona_atk = int(partes[1].strip())
        persona_golpe = partes[2].strip()
        persona_custo = int(partes[3].strip())
        print(f"{persona_nome}: Eu sou tu e tu és eu...")

        ret = combate([persona_nome, persona_atk, persona_golpe, persona_custo], hp, mp)
        hp = ret[0]
        mp = ret[1]
        andares = andares + ret[2]
        morreu = ret[3]

if morreu == 1:
    print()
    print("FIM DE JOGO")
    print(f"Andares explorados: {andares}")
    