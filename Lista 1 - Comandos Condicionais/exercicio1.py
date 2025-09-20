comp1 = input()
pasteis1 = int(input())

comp2 = input()
pasteis2 = int(input())

comp3 = input()
pasteis3 = int(input())

if comp1 == "Lineu" or comp2 == "Lineu" or comp3 == "Lineu":
    print("Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")
else:
    if pasteis1 > pasteis2 and pasteis1 > pasteis3:
        campeao = comp1
        pasteisCamp = pasteis1
    elif pasteis2 > pasteis1 and pasteis2 > pasteis3:
        campeao = comp2
        pasteisCamp = pasteis2
    else:
        campeao = comp3
        pasteisCamp = pasteis3

    print(f"A(O) campeã(o) é {campeao}, com {pasteisCamp} pastéis consumidos!")

    if campeao != "Floriano" and (comp1 == "Floriano" or comp2 == "Floriano" or comp3 == "Floriano"):
        print(f"Anos comendo pastel e perdeu justo para {campeao}, lastimável, Sr. Flor!")

    if campeao == "Agostinho":
        if pasteisCamp > 100:
            print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
        elif 50 < pasteisCamp <= 100:
            print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")
