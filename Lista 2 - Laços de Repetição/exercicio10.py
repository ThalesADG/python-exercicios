print("Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.")

qtd_rodadas = int(input())

for rodada_atual in range(1, qtd_rodadas + 1):
    print("Rodada " + str(rodada_atual) + "/" + str(qtd_rodadas) + ":")

    palavra_chave = input().lower()
    armadilha = input().lower()

    palavra_valida = False
    while palavra_valida == False:
        unicas_chave = ""
        for caractere in palavra_chave:
            if caractere not in unicas_chave:
                unicas_chave += caractere

        comuns = ""
        for caractere in armadilha:
            if caractere in unicas_chave and caractere not in comuns:
                comuns += caractere

        interseccao = len(comuns)

        if interseccao >= 3:
            print("A palavra fantasma possui " + str(interseccao) + " letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
            armadilha = input().lower()
        else:
            palavra_valida = True

    vidas_restantes = 6
    chutes = ""
    acertos = ""
    tentativas = 0
    jogando = True

    exibicao = ""
    for caractere in palavra_chave:
        exibicao += "_ "
    print("Palavra: " + exibicao[:-1]) 

    while jogando and vidas_restantes > 0:
        letra = input().lower()
        tentativas += 1

        if letra in chutes:
            print("Você já tentou a letra '" + letra + "'. Tente outra.")
            tentativas -= 1
        else:
            chutes += letra

            if letra in palavra_chave:
                print("Boa! A letra '" + letra + "' está na palavra.")
                acertos += letra
            elif letra in armadilha:
                print("CUIDADO! A letra '" + letra + "' é uma armadilha! Você perdeu 2 vidas.")
                vidas_restantes = vidas_restantes - 2
            else:
                print("Naao! A letra '" + letra + "' não está na palavra. Você perdeu 1 vida.")
                vidas_restantes = vidas_restantes - 1

            venceu = True
            for caractere in palavra_chave:
                if caractere not in acertos:
                    venceu = False

            if venceu:
                print("Parabéns, Adivinho! Você descobriu a palavra secreta: " + palavra_chave.capitalize() + ".")
                print("Total de tentativas: " + str(tentativas))
                jogando = False
            elif vidas_restantes > 0:
                print("=====================")

                exibicao = ""
                for caractere in palavra_chave:
                    if caractere in acertos:
                        exibicao += caractere + " "
                    else:
                        exibicao += "_ "
                print("Palavra: " + exibicao[:-1]) 

                print("Vidas restantes: " + str(vidas_restantes))

                letras_mostradas = ""
                for posicao in range(len(chutes)):
                    if posicao == 0:
                        letras_mostradas += chutes[posicao]
                    else:
                        letras_mostradas += ", " + chutes[posicao]
                print("Letras chutadas: " + letras_mostradas)

                print("=====================")

    if vidas_restantes <= 0:
        print("Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: " + palavra_chave.capitalize() + ".")