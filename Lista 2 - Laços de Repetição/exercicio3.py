doces = int(input())
jogador1 = input()
jogador2 = input()

arthur = jogador1 == "Arthur" or jogador2 == "Arthur"

if not arthur:
    print("Epa!!! E cadê o dono dos doces??")
else:
    print("A batalha vai começar!")
    vida_jogador1 = 10
    vida_jogador2 = 10
    vidas = True
    rodada = 1
    while vidas and doces > 0:
        doces_mod10 = doces % 10
        if not doces_mod10 and rodada == 1:
            print(f"Pra aquecer, essa primeira vale menos, só {doces_mod10} doces!")
            doces_rodadas = doces // 10
            doces_rodada_1 = doces_mod10
        else:
            doces_rodadas = doces / 10

        jogada1 = input()
        jogada2 = input()
       
        jogadas_iguais = jogada1 == jogada2
       
        if jogadas_iguais:
            print("Eita, jogaram a mesma coisa dessa vez.")
        else:
            if jogada1 == "papel":
                if jogada2 == "tesoura":
                    vida_jogador1 -= 3
                    vida_jogador2 += 1
                else:
                    vida_jogador1 += 2
                    vida_jogador2 -= 2
            elif jogada1 == "pedra":
                if jogada2 == "papel":
                    vida_jogador1 -= 2
                    vida_jogador2 += 2
                else:
                    vida_jogador2 -= 4
            else:
                if jogada2 == "pedra":
                    vida_jogador1 -= 4
                else:
                    vida_jogador1 += 1
                    vida_jogador2 -= 3

            print(f"Esse turno terminou com {jogador1} tendo {vida_jogador1} de vida e {jogador2} tendo {vida_jogador2}!")

        if vida_jogador1 <= 0 or vida_jogador2 <= 0:
            vidas = False