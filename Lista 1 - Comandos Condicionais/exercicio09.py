print("Bem-vindos ao Jimmy Jab!")
participante1 = input()
participante2 = input()
participante3 = input()
participante4 = input()

infiltrados = (participante1 == "Terry" or participante1 == "Holt" or participante2 == "Terry" or participante2 == "Holt" or participante3 == "Terry" or participante3 == "Holt" or participante4 == "Terry" or participante4 == "Holt")

if not infiltrados:
    print("Nosso primeiro evento é...\nA Bocatona!")

    scully_bocatona = (participante1 == "Scully" or participante2 == "Scully" or participante3 == "Scully" or participante4 == "Scully")
    if scully_bocatona:
        print("Scully leva a melhor, não tem como competir com ele.")
        perdedor_bocatona = input()
    else:
        vencedor_bocatona = input()
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")
        perdedor_bocatona = input()
    print(f"{perdedor_bocatona} não avançou para a próxima fase!")

    print("O segundo evento é A corrida volumosa!")

    if perdedor_bocatona == participante1:
        tempo2 = int(input())
        tempo3 = int(input())
        tempo4 = int(input())

        tempo_minimo = min(tempo2, tempo3, tempo4)
        tempo_maximo = max(tempo2, tempo3, tempo4)

        if tempo_minimo == tempo2:
            vencedor_corrida = participante2
        elif tempo_minimo == tempo3:
            vencedor_corrida = participante3
        else:
            vencedor_corrida = participante4

        if tempo_maximo == tempo2:
            perdedor_corrida = participante2
        elif tempo_maximo == tempo3:
            perdedor_corrida = participante3
        else:
            perdedor_corrida = participante4

    elif perdedor_bocatona == participante2:
        tempo1 = int(input())
        tempo3 = int(input())
        tempo4 = int(input())

        tempo_minimo = min(tempo1, tempo3, tempo4)
        tempo_maximo = max(tempo1, tempo3, tempo4)

        if tempo_minimo == tempo1:
            vencedor_corrida = participante1
        elif tempo_minimo == tempo3:
            vencedor_corrida = participante3
        else:
            vencedor_corrida = participante4

        if tempo_maximo == tempo1:
            perdedor_corrida = participante1
        elif tempo_maximo == tempo3:
            perdedor_corrida = participante3
        else:
            perdedor_corrida = participante4

    elif perdedor_bocatona == participante3:
        tempo1 = int(input())
        tempo2 = int(input())
        tempo4 = int(input())

        tempo_minimo = min(tempo1, tempo2, tempo4)
        tempo_maximo = max(tempo1, tempo2, tempo4)

        if tempo_minimo == tempo1:
            vencedor_corrida = participante1
        elif tempo_minimo == tempo2:
            vencedor_corrida = participante2
        else:
            vencedor_corrida = participante4

        if tempo_maximo == tempo1:
            perdedor_corrida = participante1
        elif tempo_maximo == tempo2:
            perdedor_corrida = participante2
        else:
            perdedor_corrida = participante4

    else:
        tempo1 = int(input())
        tempo2 = int(input())
        tempo3 = int(input())

        tempo_minimo = min(tempo1, tempo2, tempo3)
        tempo_maximo = max(tempo1, tempo2, tempo3)

        if tempo_minimo == tempo1:
            vencedor_corrida = participante1
        elif tempo_minimo == tempo2:
            vencedor_corrida = participante2
        else:
            vencedor_corrida = participante3

        if tempo_maximo == tempo1:
            perdedor_corrida = participante1
        elif tempo_maximo == tempo2:
            perdedor_corrida = participante2
        else:
            perdedor_corrida = participante3

    print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
    print(f"{perdedor_corrida} não avançou para a próxima fase!")

    finalista_participante1 = (participante1 != perdedor_bocatona and participante1 != perdedor_corrida)
    finalista_participante2 = (participante2 != perdedor_bocatona and participante2 != perdedor_corrida)
    finalista_participante3 = (participante3 != perdedor_bocatona and participante3 != perdedor_corrida)
    finalista_participante4 = (participante4 != perdedor_bocatona and participante4 != perdedor_corrida)

    if finalista_participante1:
        finalista1 = participante1
        if finalista_participante2:
            finalista2 = participante2
        elif finalista_participante3:
            finalista2 = participante3
        else:
            finalista2 = participante4
    elif finalista_participante2:
        finalista1 = participante2
        if finalista_participante3:
            finalista2 = participante3
        else:
            finalista2 = participante4
    else:
        finalista1 = participante3
        finalista2 = participante4

    if (finalista1 == "Amy" and finalista2 == "Jake") or (finalista1 == "Jake" and finalista2 == "Amy"):
        print("Jake ficou com o 2º lugar!\nAmy VENCEU O JIMMY JABS!")
    else:
        primeiro_lugar = input()
        if primeiro_lugar == finalista1:
            segundo_lugar = finalista2
        else:
            segundo_lugar = finalista1
        print(f"{segundo_lugar} ficou com o 2º lugar!\n{primeiro_lugar} VENCEU O JIMMY JABS!")
else:
    print("Jimmy Jab CANCELADO!")