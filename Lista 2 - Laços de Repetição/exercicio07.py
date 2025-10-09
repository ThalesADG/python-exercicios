print("Começa agora o treinamento para grande final mundial de cabo de guerra!")

qnt_partidas = int(input())
while qnt_partidas % 2 == 0:
    print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    qnt_partidas = int(input())

print(f"Eles batalharão em {qnt_partidas} longas partidas.")

forca_arthur = int(input())
forca_joao = int(input())
resistencia_base = int(input())

pontuacao_arthur = 0
pontuacao_joao = 0

partida_atual = 1
jogo_continua = True
while partida_atual <= qnt_partidas and jogo_continua:
    print(f"Começa a {partida_atual}ª partida!")
    print(f"Placar geral: {pontuacao_arthur} X {pontuacao_joao}")

    resistencia_a = resistencia_base
    resistencia_j = resistencia_base

    while resistencia_a > 0 and resistencia_j > 0:
        numero_rodada = int(input())

        is_quadrado_perfeito = False
        if numero_rodada >= 0:
            raiz = numero_rodada ** 0.5
            if raiz == int(raiz):
                is_quadrado_perfeito = True

        is_primo = True
        if numero_rodada < 2:
            is_primo = False
        else:
            for divisor in range(2, numero_rodada):
                if numero_rodada % divisor == 0:
                    is_primo = False
        
        if is_quadrado_perfeito:
            print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
            resistencia_a += 1
            resistencia_j -= 1
        elif is_primo:
            print("O primo do primo é primo do primo? João puxa mais forte!")
            resistencia_j += 1
            resistencia_a -= 1
        else:
            if forca_arthur > forca_joao:
                print(f"Arthur é o mais forte! João não consegue segurar.")
                resistencia_a += 1
                resistencia_j -= 1
            else:
                print(f"João é o mais forte! Arthur não consegue segurar.")
                resistencia_j += 1
                resistencia_a -= 1
    
    if resistencia_a > resistencia_j:
        print("Arthur dá orgulho para Maceió e ganha a partida!")
        pontuacao_arthur += 1
    else:
        print("João usa seus talentos de mangueboy e leva essa para casa!")
        pontuacao_joao += 1

    partidas_restantes = qnt_partidas - partida_atual
    diferenca_de_pontos = abs(pontuacao_arthur - pontuacao_joao)

    if diferenca_de_pontos > partidas_restantes:
        jogo_continua = False

    partida_atual += 1

print()
print("Agora eles estão prontos para o mundial!")
print(f"Placar final: {pontuacao_arthur} X {pontuacao_joao}")

diferenca_final = abs(pontuacao_arthur - pontuacao_joao)

if pontuacao_arthur > pontuacao_joao:
    vencedor = "Arthur"
    perdedor = "João"
    if pontuacao_joao == 0:
        print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
    else:
        print(f"O ganhador foi {vencedor} com uma diferença de {diferenca_final} partidas.")
else:
    vencedor = "João"
    perdedor = "Arthur"
    if pontuacao_arthur == 0:
        print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
    else:
        print(f"O ganhador foi {vencedor} com uma diferença de {diferenca_final} partidas.")