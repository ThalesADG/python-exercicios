def distancia_chebyshev(a, b):
    dr = abs(a[0] - b[0])
    dc = abs(a[1] - b[1])
    if dr > dc:
        return dr
    else:
        return dc


def acao_atirar(pos_sam, pos_neil, hp_neil, arma):
    d = distancia_chebyshev(pos_sam, pos_neil)
    dano = 0
    if arma == "Espingarda":
        if d <= 2:
            dano = 25
    elif arma == "Rifle":
        if d == 3:
            dano = 15
        else:
            dano = 5
    elif arma == "Metralhadora":
        if d >= 4:
            dano = 15
    novo_hp = hp_neil - dano
    acertou = False
    if dano > 0:
        acertou = True
    return novo_hp, acertou


def teleporte_neil(campo, pos_sam, pos_neil):
    maior_dist = -1
    nova_pos = [pos_neil[0], pos_neil[1]]
    i = 0
    while i < 6:
        j = 0
        while j < 6:
            if campo[i][j] != 'I':
                dist = distancia_chebyshev(pos_sam, [i, j])
                if dist >= maior_dist:
                    maior_dist = dist
                    nova_pos = [i, j]
            j = j + 1
        i = i + 1
    r = 0
    while r < 6:
        linha = []
        c = 0
        while c < 6:
            if r == pos_sam[0] and c == pos_sam[1]:
                linha.append('S')
            elif r == nova_pos[0] and c == nova_pos[1]:
                linha.append('N')
            else:
                linha.append(campo[r][c])
            c = c + 1
        print(" ".join(linha))
        r = r + 1
    return nova_pos


def mover_sam(campo, pos, direcao):
    r = pos[0]
    c = pos[1]
    nr = r
    nc = c
    if direcao == 'W':
        nr = r - 1
    elif direcao == 'A':
        nc = c - 1
    elif direcao == 'S':
        nr = r + 1
    elif direcao == 'D':
        nc = c + 1
    nova = [r, c]
    dentro = False
    if nr >= 0 and nr < 6 and nc >= 0 and nc < 6:
        dentro = True
    if dentro:
        if campo[nr][nc] != 'I':
            nova = [nr, nc]
    dano_fogo = 0
    if campo[nova[0]][nova[1]] == 'F':
        dano_fogo = 5
    return nova, dano_fogo


def trocar_arma(comando):
    arma_nova = "Rifle"
    if comando == "Espingarda":
        arma_nova = "Espingarda"
    elif comando == "Rifle":
        arma_nova = "Rifle"
    elif comando == "Metralhadora":
        arma_nova = "Metralhadora"
    print(f"Arma trocada para {arma_nova}.")
    return arma_nova


campo = []
sam = [0, 0]
neil = [0, 0]
i = 0
while i < 6:
    partes = input().split()
    linha = []
    j = 0
    while j < 6:
        cel = partes[j]
        if cel == 'S':
            sam = [i, j]
            linha.append('P')
        elif cel == 'N':
            neil = [i, j]
            linha.append('P')
        else:
            linha.append(cel)
        j = j + 1
    campo.append(linha)
    i = i + 1

print("Sam: Mas que lugar é esse aqui?")
print("Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!")
print()

vida_sam = 100
vida_neil = 100
arma = "Rifle"
acoes = 0
hits_neil = 0
dano_neil_total = 0
fogo_total = 0
aviso = False
fim = False

while not fim:
    comando = input()
    fez_acao = False
    if comando == 'W' or comando == 'A' or comando == 'S' or comando == 'D':
        nova_pos, dano_f = mover_sam(campo, sam, comando)
        sam = nova_pos
        if dano_f > 0:
            vida_sam = vida_sam - dano_f
            fogo_total = fogo_total + 1
        fez_acao = True
    elif comando == "Atirar":
        if campo[sam[0]][sam[1]] == 'F':
            vida_sam = vida_sam - 5
            fogo_total = fogo_total + 1
        novo_hp, atingiu = acao_atirar(sam, neil, vida_neil, arma)
        vida_neil = novo_hp
        if atingiu:
            hits_neil = hits_neil + 1
        fez_acao = True
    elif comando == "Espingarda" or comando == "Rifle" or comando == "Metralhadora":
        if campo[sam[0]][sam[1]] == 'F':
            vida_sam = vida_sam - 5
            fogo_total = fogo_total + 1
        arma = trocar_arma(comando)
        fez_acao = True

    if fez_acao and not fim:
        acoes = acoes + 1
        if vida_sam <= 0:
            fim = True
            print()
            print("MISSÃO FALHOU")
            print("==============")
            print("Sam foi derrotado.")
            print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")
        if vida_neil <= 0 and not fim:
            fim = True
            likes = 1000 - (dano_neil_total * 8) - (fogo_total * 10)
            print()
            print("MISSÃO COMPLETA! - Investigue a Anomalia")
            print("========================================")
            print(f"Likes recebidos: 👍 {likes}")
        if not fim:
            if acoes == 4:
                print(">>> Você recebe um disparo de Neil! <<<")
                vida_sam = vida_sam - 15
                dano_neil_total = dano_neil_total + 15
                acoes = 0
            if hits_neil == 3:
                neil = teleporte_neil(campo, sam, neil)
                hits_neil = 0
            if vida_sam <= 40 and not aviso:
                print("Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")
                aviso = True
            if vida_sam <= 0 and not fim:
                fim = True
                print()
                print("MISSÃO FALHOU")
                print("==============")
                print("Sam foi derrotado.")
                print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")
