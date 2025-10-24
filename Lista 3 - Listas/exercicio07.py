print("Iniciando investigação... Zé Felipe está focado.")

quantidade_eventos = int(input())
lista_eventos = []

detetive_parou = False
nivel_suspeita = 0

for contador in range(quantidade_eventos):
    linha_input = input()
    partes = linha_input.split(" - ")

    codigo = partes[0].strip()

    if codigo == "VJM":
        detetive_parou = True
        nivel_suspeita = 100

    if not detetive_parou:
        nome_evento = partes[1].strip()
        inicio_str = partes[2].strip()
        fim_str = partes[3].strip()

        horas_inicio = inicio_str.split(":")
        minutos_inicio = int(horas_inicio[0]) * 60 + int(horas_inicio[1])

        horas_fim = fim_str.split(":")
        minutos_fim = int(horas_fim[0]) * 60 + int(horas_fim[1])

        lista_eventos.append([codigo, nome_evento, minutos_inicio, minutos_fim, inicio_str, fim_str])

if detetive_parou:
    print("\nTRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
else:
    print("\n--- Linha do Tempo dos Eventos ---")

    total = len(lista_eventos)
    for i in range(total):
        for j in range(0, total - i - 1):
            if lista_eventos[j][2] > lista_eventos[j+1][2]:
                lista_eventos[j], lista_eventos[j+1] = lista_eventos[j+1], lista_eventos[j]
            elif lista_eventos[j][2] == lista_eventos[j+1][2]:
                if lista_eventos[j][3] > lista_eventos[j+1][3]:
                    lista_eventos[j], lista_eventos[j+1] = lista_eventos[j+1], lista_eventos[j]

    for indice in range(len(lista_eventos)):
        cod = lista_eventos[indice][0]
        evento_nome = lista_eventos[indice][1]
        inicio_str = lista_eventos[indice][4]
        fim_str = lista_eventos[indice][5]

        if cod == "V":
            pessoa = "Virgínia"
        elif cod == "JM":
            pessoa = "Jogador Misterioso"
        elif cod == "ZF":
            pessoa = "Zé Felipe"
        else:
            pessoa = "Virginia e Jogador Misterioso"

        print(f"{inicio_str}-{fim_str}: {pessoa} - {evento_nome}")

    print("\n--- Resumo da Análise ---")

    encontros = 0
    alibis = 0
    nivel_suspeita = 0

    for a in range(len(lista_eventos)):
        for b in range(a + 1, len(lista_eventos)):
            ev_a = lista_eventos[a]
            ev_b = lista_eventos[b]

            if ev_a[1] == ev_b[1]:
                inicio_a, fim_a = ev_a[2], ev_a[3]
                inicio_b, fim_b = ev_b[2], ev_b[3]

                if inicio_a < fim_b and inicio_b < fim_a:
                    sigla_a = ev_a[0]
                    sigla_b = ev_b[0]

                    if (sigla_a == "V" and sigla_b == "JM") or (sigla_a == "JM" and sigla_b == "V"):
                        nivel_suspeita += 35
                        encontros += 1
                    elif (sigla_a == "V" and sigla_b == "ZF") or (sigla_a == "ZF" and sigla_b == "V"):
                        nivel_suspeita -= 20
                        alibis += 1
                        if nivel_suspeita < 0:
                            nivel_suspeita = 0

    print(f"Encontros Suspeitos: {encontros}")
    print(f"Álibis Confirmados: {alibis}")
    print()

    if nivel_suspeita >= 100:
        print("TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
    elif 70 <= nivel_suspeita <= 99:
        print(f"Nível de Suspeita: {nivel_suspeita} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.")
    elif 30 <= nivel_suspeita <= 69:
        print(f"Nível de Suspeita: {nivel_suspeita} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.")
    else:
        print(f"Nível de Suspeita: {nivel_suspeita} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.")
