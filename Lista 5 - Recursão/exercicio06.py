ENERGIA_INICIAL = 100.0
HORARIOS = [0, 1, 2, 3, 4, 5]
OPCOES_BINARIAS = [False, True]
TOLERANCIA = 1e-9

MENSAGEM_ENTRADA_INVALIDA = '"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."'
MENSAGEM_SEM_ANIMATRONIC = '"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."'
MENSAGEM_SEM_SOBREVIVENCIA = '"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"'
MENSAGEM_VITORIA = '"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia}% de energia. Eu sabia que você conseguiria."'
MENSAGEM_ITS_ME = '"IT\'S ME"'


def aproximadamente_igual(valor_a, valor_b):
    return abs(valor_a - valor_b) <= TOLERANCIA


def formatar_estado(ativo):
    return "SIM" if ativo else "NÃO"


def eh_token_numerico(texto):
    if not texto:
        return False
    indice = 0
    while indice < len(texto):
        caractere = texto[indice]
        if caractere < "0" or caractere > "9":
            return False
        indice += 1
    return True


def simular_hora(horario, energia_atual, estado, dificuldades, golden_presente):
    bonnie, chica, freddy, foxy = dificuldades
    pe, pd, luzes, camera = estado

    consumo = 1.0
    if pe:
        consumo += 7.0
    if pd:
        consumo += 7.0
    if luzes:
        consumo += 5.0
    if camera:
        consumo += 9.0

    if bonnie > 0 and horario in [0, 3]:
        pode_barrar = pe or (luzes and not camera)
        if not pode_barrar:
            return [False, 0.0]
        consumo += 3.0 + bonnie * 0.25

    if chica > 0 and horario in [1, 4]:
        pode_barrar = pd or camera
        if not pode_barrar:
            return [False, 0.0]
        consumo += 2.0 + chica * 0.35

    if foxy > 0 and horario == 4 and energia_atual > ENERGIA_INICIAL / 2:
        if not pe:
            return [False, 0.0]
        consumo += 5.0 + foxy * 0.15

    if freddy > 0 and horario == 5:
        pode_barrar = (pe and pd) or camera
        if not pode_barrar:
            return [False, 0.0]
        consumo += 3.0 + freddy * 0.35

    if golden_presente and horario == 5:
        if not camera:
            return [False, 0.0]
        consumo += 10.0 + freddy * 1.95

    energia_restante = energia_atual - consumo
    if energia_restante <= 0.0:
        return [False, 0.0]
    return [True, energia_restante]


def explorar_recursivamente(indice_horario, energia_atual, sequencia_decisoes, dificuldades, golden_presente):
    if indice_horario == len(HORARIOS):
        return [True, energia_atual, sequencia_decisoes]

    horario = HORARIOS[indice_horario]
    candidatos = []
    for pe in OPCOES_BINARIAS:
        for pd in OPCOES_BINARIAS:
            for luzes in OPCOES_BINARIAS:
                for camera in OPCOES_BINARIAS:
                    estado = [pe, pd, luzes, camera]
                    valido, energia_restante = simular_hora(horario, energia_atual, estado, dificuldades, golden_presente)
                    if valido:
                        candidatos.append([energia_restante, estado])

    if not candidatos:
        return [False, 0.0, []]

    maior_energia = max(item[0] for item in candidatos)
    melhores_candidatos = []
    for item in candidatos:
        if aproximadamente_igual(item[0], maior_energia):
            melhores_candidatos.append(item)

    for energia_hora, estado in melhores_candidatos:
        sucesso, energia_final, sequencia_final = explorar_recursivamente(
            indice_horario + 1, energia_hora, sequencia_decisoes + [estado], dificuldades, golden_presente
        )
        if sucesso:
            return [True, energia_final, sequencia_final]

    return [False, 0.0, []]


def aciona_digitos_especiais(valores):
    digitos = "".join(str(abs(valor)) for valor in valores)
    possui_1987 = True
    for caractere in "1987":
        if caractere not in digitos:
            possui_1987 = False
    return possui_1987 and "0" in digitos


def main():
    entrada = input().strip()
    if not entrada:
        print(MENSAGEM_ENTRADA_INVALIDA)
        return

    partes = entrada.split()
    if len(partes) != 4:
        print(MENSAGEM_ENTRADA_INVALIDA)
        return

    possui_nao_digito = False
    for trecho in partes:
        if not eh_token_numerico(trecho):
            possui_nao_digito = True
    if possui_nao_digito:
        print(MENSAGEM_ENTRADA_INVALIDA)
        return

    dificuldades = [int(trecho) for trecho in partes]
    fora_do_intervalo = False
    for dificuldade in dificuldades:
        if dificuldade < 0 or dificuldade > 20:
            fora_do_intervalo = True
    if fora_do_intervalo:
        print(MENSAGEM_ENTRADA_INVALIDA)
        return

    if aciona_digitos_especiais(dificuldades):
        print(MENSAGEM_ITS_ME)
        return

    todos_zero = True
    for dificuldade in dificuldades:
        if dificuldade != 0:
            todos_zero = False
    if todos_zero:
        print(MENSAGEM_SEM_ANIMATRONIC)
        return

    golden_presente = sorted(dificuldades) == [1, 7, 8, 9]

    sucesso, energia_final, sequencia_decisoes = explorar_recursivamente(
        0, ENERGIA_INICIAL, [], dificuldades[:], golden_presente
    )

    if not sucesso:
        print(MENSAGEM_SEM_SOBREVIVENCIA)
        return

    energia_formatada = f"{energia_final:.2f}"
    print(MENSAGEM_VITORIA.format(energia=energia_formatada))

    indice = 0
    while indice < len(sequencia_decisoes):
        horario = HORARIOS[indice]
        estado = sequencia_decisoes[indice]
        pe, pd, luzes, camera = estado
        print(
            f"{horario:02d}:00 AM -> PE: {formatar_estado(pe)} | PD: {formatar_estado(pd)} "
            f"| LZ: {formatar_estado(luzes)} | CAM: {formatar_estado(camera)}"
        )
        indice += 1


main()
