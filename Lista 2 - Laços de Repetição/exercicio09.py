print("INICIANDO SIMULAÇÃO...")

pontos_arthur = 0
pontos_samuel = 0

jogador1 = input()

while jogador1 != "Arthur" and jogador1 != "Samuel":
    print("Jogador inválido! Essa competição é apenas entre Arthur e Samuel!")
    jogador1 = input()

print(f"{jogador1} começa na corda!")

if jogador1 == "Arthur":
    jogador2 = "Samuel"
else:
    jogador2 = "Arthur"

qtd_rodadas = int(input())

for i in range(1, qtd_rodadas + 1):
    print(f"Começa a {i}ª rodada!")
    if i == qtd_rodadas:
        print("Última rodada! Valendo 2 pontos!")

    ritmo = int(input())
    aposta = int(input())

    print(f"{jogador2} aposta que {jogador1} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador1} será {ritmo}!")

    tropecos = 0
    pulos_atuais = 0
    quase_la_impresso = False

    while pulos_atuais < aposta and tropecos < 3:
        pulos_restantes = aposta - pulos_atuais

        soma_algarismos = 0
        for d in str(abs(pulos_restantes)):
            soma_algarismos += int(d)

        teste1 = 5 * soma_algarismos * soma_algarismos + 4
        teste2 = 5 * soma_algarismos * soma_algarismos - 4
        raiz1 = int(teste1 ** 0.5)
        raiz2 = int(teste2 ** 0.5)
        is_fibonacci = (raiz1 * raiz1 == teste1) or (raiz2 * raiz2 == teste2)

        if is_fibonacci:
            tropecos += 1
            print(f"O número da soma é {soma_algarismos}, que faz parte da sequência de Fibonacci!! {jogador1} tropeça!")
        elif pulos_restantes * 4 < aposta and not quase_la_impresso:
            print(f"{jogador1} está quase chegando ao apostado! Falta pouco!")
            quase_la_impresso = True
        else:
            print(f"{jogador1} pula com maestria! Faltam {pulos_restantes} pulos!")

        pulos_atuais += ritmo

    if tropecos == 3:
        print(f"E agora não tem jeito, {jogador1} cai de cara no chão!")

    if pulos_atuais >= aposta and tropecos < 3:
        pontos_da_rodada = 2 if i == qtd_rodadas else 1

        if jogador1 == "Arthur":
            pontos_arthur += pontos_da_rodada
        else:
            pontos_samuel += pontos_da_rodada

        if pulos_atuais == aposta:
            print(f"{jogador1} cumpriu o prometido e alcançou {aposta} pulos! Ponto merecidíssimo!")
        else:
            diferenca = pulos_atuais - aposta
            print(f"{jogador1} vai além, e supera a aposta em {diferenca} Ponto(s)! Deixou o {jogador2} no chinelo!")

    elif tropecos < 3:
        if pulos_atuais * 4 > aposta * 3:
            print(f"Quase lá! por pouco {jogador1} não alcançou o apostado!")
        elif pulos_atuais * 2 >= aposta:
            print(f"Nem muito perto, nem muito longe do apostado. Talvez {jogador1} teve apenas azar!")
        else:
            print(f"Nossa!! Parece que {jogador1} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!")
    elif tropecos == 3 and pulos_atuais < aposta:
        if pulos_atuais * 4 > aposta * 3:
            print(f"Quase lá! por pouco {jogador1} não alcançou o apostado!")
        elif pulos_atuais * 2 >= aposta:
            print(f"Nem muito perto, nem muito longe do apostado. Talvez {jogador1} teve apenas azar!")
        else:
            print(f"Nossa!! Parece que {jogador1} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!")

    jogador1, jogador2 = jogador2, jogador1

print("COMPUTANDO PREVISÃO FINAL...")

if pontos_arthur > pontos_samuel:
    print(f"Arthur venceu a competição com {pontos_arthur} ponto(s)! Trouxe orgulho para Maceió!")
elif pontos_samuel > pontos_arthur:
    print(f"Samuel venceu a competição com {pontos_samuel} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!")
elif pontos_arthur == pontos_samuel and pontos_arthur > 0:
    print(f"Houve um empate técnico! Ambos fizeram {pontos_arthur} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!")
else:
    print("Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo...")
