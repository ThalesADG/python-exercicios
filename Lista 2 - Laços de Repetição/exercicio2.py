PREDIO1 = "CFCH"
PREDIO2 = "CTG"
PREDIO3 = "CIN"

print("Vai começar o esconde-esconde UFPE 2025!")

nome1 = input()
nome2 = input()
nome3 = input()

for a in range(3):
    if a == 0:
        pontos1 = 0
        print(f"\nProntos ou não, lá vai {nome1}.")
        for b in range(3):
            if b == 0:
                print(f"Agora {nome1} procurará no {PREDIO1}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos1 += 1
                        print(f"{nome1} achou uma pessoa!")
                    else:
                        buscador = False
            elif b == 1:
                print(f"Agora {nome1} procurará no {PREDIO2}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos1 += 1
                        print(f"{nome1} achou uma pessoa!")
                    else:
                        buscador = False
            else:
                print(f"Agora {nome1} procurará no {PREDIO3}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos1 += 1
                        print(f"{nome1} achou uma pessoa!")
                    else:
                        buscador = False
    elif a== 1:
        pontos2 = 0
        print(f"\nProntos ou não, lá vai {nome2}.")
        for b in range(3):
            if b == 0:
                print(f"Agora {nome2} procurará no {PREDIO1}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos2 += 1
                        print(f"{nome2} achou uma pessoa!")
                    else:
                        buscador = False
            elif b == 1:
                print(f"Agora {nome2} procurará no {PREDIO2}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos2 += 1
                        print(f"{nome2} achou uma pessoa!")
                    else:
                        buscador = False
            else:
                print(f"Agora {nome2} procurará no {PREDIO3}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos2 += 1
                        print(f"{nome2} achou uma pessoa!")
                    else:
                        buscador = False
    else:
        pontos3 = 0
        print(f"\nProntos ou não, lá vai {nome3}.")
        for b in range(3):
            if b == 0:
                print(f"Agora {nome3} procurará no {PREDIO1}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos3 += 1
                        print(f"{nome3} achou uma pessoa!")
                    else:
                        buscador = False
            elif b == 1:
                print(f"Agora {nome3} procurará no {PREDIO2}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos3 += 1
                        print(f"{nome3} achou uma pessoa!")
                    else:
                        buscador = False
            else:
                print(f"Agora {nome3} procurará no {PREDIO3}.")
                buscador = True
                while buscador:
                    encontrou = input()
                    if encontrou == "Achou uma pessoa!":
                        pontos3 += 1
                        print(f"{nome3} achou uma pessoa!")
                    else:
                        buscador = False

pontos_vencedor = max(pontos1, pontos2, pontos3)
print()
if pontos_vencedor == 0:
    print("Ninguém foi encontrado, nenhum dos buscadores ganhou a disputa.")
elif pontos_vencedor == pontos1:
    print(f"{nome1} é o(a) melhor no esconde-esconde da UFPE!")
elif pontos_vencedor == pontos2:
    print(f"{nome2} é o(a) melhor no esconde-esconde da UFPE!")
else:
    print(f"{nome3} é o(a) melhor no esconde-esconde da UFPE!")