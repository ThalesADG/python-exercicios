casos  = int(input())
dias = int(input())
assistencias = int(input())
operacoes = int(input())
operacao_especial = input()
if operacao_especial == "sim":
    tipo_operacao_especial = input()
localizacao = input()

localizacao_valida = (localizacao == "Manhattan" or localizacao == "Brooklyn")
CASOS_MINIMOS = 20
MEDIA_MINIMA = 0.5
ASSISTENCIAS_MINIMAS = 5
OPERACOES_MINIMAS = 20

PESO_CASOS = 2
PESO_ASSISTENCIAS = 1.5
PESO_OPERACOES = 0.5
pontuacao = (casos * PESO_CASOS) + (assistencias * PESO_ASSISTENCIAS) + (operacoes * PESO_OPERACOES)

if localizacao_valida:
    print("Pelo menos nos bairros corretos Jake está!")

    if casos >= CASOS_MINIMOS:
        print("Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")

        if casos / dias >= MEDIA_MINIMA:
            print("Parece que Jake é bem consistente na sua média diária de casos.")

            if assistencias >= ASSISTENCIAS_MINIMAS:
                print("Peralta ajudou bastante outros detetives, ele ainda está na competição!")

                if operacoes >= OPERACOES_MINIMAS:
                    print("Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")

                    if operacao_especial == "sim":
                        print("Minha nossa! Jake Peralta é realmente um detetive diferenciado.")

                        if tipo_operacao_especial == "Infiltração":
                            pontuacao *= 1.5
                        elif tipo_operacao_especial == "Escuta":
                            pontuacao *= 1.3
                        elif tipo_operacao_especial == "Invasão":
                            pontuacao *= 1.2
                        else:
                            pontuacao *= 1.1

                    else:
                        print("Para que operação especial quando se tem números, não é?")

                    if pontuacao >= 70:
                        print("Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?")
                    elif pontuacao >= 40:
                        print("Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.")
                    else:
                        print("Muito difícil de Jake ganhar o prêmio.")

                else:
                    print("Peralta precisa sair mais da delegacia, está faltando ação em campo!")

            else:
                print("Desclassificado! Jake precisa ajudar mais os companheiros.")

        else:
            print("A média diária de casos tá muito baixa, Peralta foi desclassificado.")

    else:
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")

else:
    print("Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")