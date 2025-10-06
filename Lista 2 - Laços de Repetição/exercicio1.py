print("Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")

quantidade_participantes = int(input())

nome_inicial = input()
palavra_referencia = input()
palavra_anterior = palavra_referencia
palavra_final = palavra_referencia

quantidade_trocas = 0
nome_jogador_1 = ""
nome_jogador_2 = ""
palavra_errada = ""

for i in range(quantidade_participantes - 1):
    nome_participante = input()
    palavra_atual = input()

    if palavra_anterior != palavra_atual:
        print(f"Parece que {nome_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…")
        quantidade_trocas += 1
        palavra_errada = palavra_atual

        if quantidade_trocas == 1:
            nome_jogador_1 = nome_participante
        elif quantidade_trocas == 2:
            nome_jogador_2 = nome_participante

        if quantidade_trocas == 5:
            print(f"Caramba, que confusão! A palavra {palavra_referencia} já tá toda embaralhada e virou {palavra_atual}!")

    palavra_anterior = palavra_atual
    palavra_final = palavra_atual

if palavra_final == palavra_referencia:
    if quantidade_trocas == 0:
        print(f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_referencia}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.")
    else:
        print(f"Parece que ocorreram {quantidade_trocas} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_referencia} conseguiu chegar no fim do telefone sem fio.")
else:
    if quantidade_trocas == 1:
        print(f"Poxa, foi por pouco, só quem errou foi {nome_jogador_1} que disse {palavra_errada} ao invés de {palavra_referencia}…")
    elif quantidade_trocas == 2:
        print(f"Se não fosse pelos erros de {nome_jogador_1} e {nome_jogador_2} a palavra {palavra_referencia} poderia ter chegado até o fim, talvez eles devessem tentar de novo.")
    else:
        print(f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {palavra_referencia} acabou virando {palavra_final}. No total, ocorreram {quantidade_trocas} trocas.")
