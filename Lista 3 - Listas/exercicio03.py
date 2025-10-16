GOLEIROS_ESPECIAIS = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"]

print("RECEBA! É hoje que eu me torno o melhor dos melhores.")

numero_sessoes = int(input())
habilidade_inicial = int(input())
sequencia_string = input()

if habilidade_inicial >= 16:
    print("O Pai tá estourado! RECEBA!")
elif habilidade_inicial >= 6:
    print("Não tem jeito, vou ser o melhor do mundo!")
else:
    print("A gente tem que começar de algum lugar, né? RECEBA!")

meta = (100 - habilidade_inicial) / numero_sessoes
print(f"Meta por Partida: {meta}")

lista_de_acoes = sequencia_string.split('-')
matriz_de_acoes = []
for i in range(0, len(lista_de_acoes), 2):
    matriz_de_acoes.append([lista_de_acoes[i], lista_de_acoes[i + 1]])

habilidade_atual = habilidade_inicial
partida_atual = 0
total_partidas = numero_sessoes

jogo_acabou = False

for partida in matriz_de_acoes:
    if not jogo_acabou:
        partida_atual += 1
        tipo_batida = partida[0]
        goleiro = partida[1]

        print(f"TIPO DE PARTIDA: {tipo_batida}")
        print(f"Nome do Goleiro: {goleiro}")

        if goleiro not in GOLEIROS_ESPECIAIS:
            habilidade_goleiro = int(input())

        matriz = eval(input())
        x = int(input())
        y = int(input())

        foi_gol = False
        pontos_ganhos = 0

        if matriz[x][y] == 1:
            foi_gol = True
            if goleiro == "Rokenedy":
                print("Aí não dá, impossível de fazer gol no maior do mundo.")
                foi_gol = False
            elif goleiro == "IShowSpeed":
                print("REBECA? Is that you?\nIspidi mai friand, recieve!")
                pontos_ganhos = meta * 1.5
            elif goleiro == "Sérgio Soares":
                print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
                if tipo_batida == "Batida de Pênalti":
                    pontos_ganhos = meta
                else:
                    foi_gol = False
            elif goleiro == "Neymar Jr":
                print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
                pontos_ganhos = meta / 2
            elif goleiro == "Gabriel Vasconcelos":
                print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
                pontos_ganhos = meta * 2
            elif habilidade_atual > habilidade_goleiro:
              pontos_ganhos = habilidade_atual - habilidade_goleiro

        if foi_gol:
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
        else:
            print("A jornada ainda não acabou!")
        
        habilidade_atual += pontos_ganhos

        if habilidade_atual > 100:
            print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")
            jogo_acabou = True
        else:
            if pontos_ganhos >= meta:
                print(f"VAMO! PARTIDA {partida_atual} DE {total_partidas}!")
            else:
                print(f"Dá pra recuperar depois! Vamo seguindo!")

if not jogo_acabou:
    if habilidade_atual == 100:
        print("O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")
    else:
        print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")