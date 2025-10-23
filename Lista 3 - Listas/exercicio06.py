print("Senhoras e senhores, o desfile de gala do CIn vai começar!")

qtd_pessoas = int(input())
marca = input()

parcerias = [
    ["Tha Beauty", "Thais Linares"],
    ["DeGuê?", "Davi Brito"],
    ["Diva Depressão", "Edu e Fih"]
]

chefes = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", "Elisson Oliveira",
          "Filipe Moreira", "Gabriela Alves", "Joab Henrique", "Maria Fernanda",
          "Miriam Gonzaga", "Sofia Remindes"]
chefes.sort()

patrocinador = ""
for par in parcerias:
    if marca == par[0]:
        patrocinador = par[1]

entradas = []
for i in range(qtd_pessoas):
    nome = input()
    entradas.append(nome)

passarela = []
intrusos = []
invasoes = 0

for i in range(len(entradas)):
    nome_atual = entradas[i]

    if nome_atual in chefes:
        passarela.append(nome_atual)
        print(f"Desfilante de n° {len(passarela)}: {nome_atual}!")

    elif nome_atual == patrocinador:
        print("Invasão tolerada por motivos de patrocínio!")
        passarela.append(nome_atual)
        print(f"Desfilante de n° {len(passarela)}: {nome_atual}!")

    else:
        print(f"{nome_atual} invadiu a passarela! Segurem ele(a), produção!")
        intrusos.append(nome_atual)
        invasoes += 1

        substituto = ""
        indice = 0
        achou = False

        while indice < len(chefes):
            chefe_atual = chefes[indice]
            if chefe_atual not in passarela and chefe_atual not in entradas and not achou:
                substituto = chefe_atual
                achou = True
            indice += 1

        if achou:
            passarela.append(substituto)
            print(f"Desfilante de n° {len(passarela)}: {substituto}!")
        else:
            passarela.append(nome_atual)
            print(f"Desfilante de n° {len(passarela)}: {nome_atual}?! Pelo visto não havia como substituir...")

        if invasoes == 3:
            print("Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!")
            passarela.append("Core")
            print(f"Desfilante de n° {len(passarela)}: Core!")

tem_especiais = False
for i in range(len(intrusos)):
    if intrusos[i] == "Gretchen" or intrusos[i] == "Tulla Luana" or intrusos[i] == "Inês Brasil":
        tem_especiais = True

if tem_especiais:
    print("Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")

for i in range(len(intrusos)):
    if intrusos[i] == "Gretchen":
        print("\"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!\"")
    elif intrusos[i] == "Tulla Luana":
        print("\"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso.\"")
    elif intrusos[i] == "Inês Brasil":
        print("\"É aquele ditado... Vamo fazer o quê?\"")
