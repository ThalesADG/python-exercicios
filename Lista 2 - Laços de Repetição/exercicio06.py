n = int(input())

nome_ana = "Ana"
ana_venceu = False
ana_tentativa_da_vitoria = 0
ana_ultima_casa = 0
tentativa_atual = 0

for i in range(n):
    tentativa_atual = i + 1
    resultado_da_tentativa = int(input())

    if resultado_da_tentativa == 5:
        if not ana_venceu:
            ana_venceu = True
            ana_tentativa_da_vitoria = tentativa_atual
    
    ana_ultima_casa = resultado_da_tentativa


nome_adrieli = "Adrieli"
adrieli_venceu = False
adrieli_tentativa_da_vitoria = 0
adrieli_ultima_casa = 0
tentativa_atual = 0

for i in range(n):
    tentativa_atual = i + 1
    resultado_da_tentativa = int(input())

    if resultado_da_tentativa == 5:
        if not adrieli_venceu:
            adrieli_venceu = True
            adrieli_tentativa_da_vitoria = tentativa_atual

    adrieli_ultima_casa = resultado_da_tentativa


nome_joab = "Joab"
joab_venceu = False
joab_tentativa_da_vitoria = 0
joab_ultima_casa = 0
tentativa_atual = 0

for i in range(n):
    tentativa_atual = i + 1
    resultado_da_tentativa = int(input())

    if resultado_da_tentativa == 5:
        if not joab_venceu:
            joab_venceu = True
            joab_tentativa_da_vitoria = tentativa_atual

    joab_ultima_casa = resultado_da_tentativa


nome_duda = "Duda"
duda_venceu = False
duda_tentativa_da_vitoria = 0
duda_ultima_casa = 0
tentativa_atual = 0

for i in range(n):
    tentativa_atual = i + 1
    resultado_da_tentativa = int(input())

    if resultado_da_tentativa == 5:
        if not duda_venceu:
            duda_venceu = True
            duda_tentativa_da_vitoria = tentativa_atual

    duda_ultima_casa = resultado_da_tentativa



print(f"{nome_ana} tentou {n} vezes e completou a última casa {ana_ultima_casa}")
if ana_venceu:
    print(f"{nome_ana} completou a amarelinha!")
else:
    print(f"{nome_ana} não conseguiu completar a amarelinha!")

print(f"{nome_adrieli} tentou {n} vezes e completou a última casa {adrieli_ultima_casa}")
if adrieli_venceu:
    print(f"{nome_adrieli} completou a amarelinha!")
else:
    print(f"{nome_adrieli} não conseguiu completar a amarelinha!")

print(f"{nome_joab} tentou {n} vezes e completou a última casa {joab_ultima_casa}")
if joab_venceu:
    print(f"{nome_joab} completou a amarelinha!")
else:
    print(f"{nome_joab} não conseguiu completar a amarelinha!")

print(f"{nome_duda} tentou {n} vezes e completou a última casa {duda_ultima_casa}")
if duda_venceu:
    print(f"{nome_duda} completou a amarelinha!")
else:
    print(f"{nome_duda} não conseguiu completar a amarelinha!")


menor_tentativa = n + 1

if ana_venceu and ana_tentativa_da_vitoria < menor_tentativa:
    menor_tentativa = ana_tentativa_da_vitoria
if adrieli_venceu and adrieli_tentativa_da_vitoria < menor_tentativa:
    menor_tentativa = adrieli_tentativa_da_vitoria
if joab_venceu and joab_tentativa_da_vitoria < menor_tentativa:
    menor_tentativa = joab_tentativa_da_vitoria
if duda_venceu and duda_tentativa_da_vitoria < menor_tentativa:
    menor_tentativa = duda_tentativa_da_vitoria


vencedores_nomes = ""
numero_de_vencedores = 0

if ana_venceu and ana_tentativa_da_vitoria == menor_tentativa:
    numero_de_vencedores += 1
    vencedores_nomes += nome_ana + ", "

if adrieli_venceu and adrieli_tentativa_da_vitoria == menor_tentativa:
    numero_de_vencedores += 1
    vencedores_nomes += nome_adrieli + ", "

if joab_venceu and joab_tentativa_da_vitoria == menor_tentativa:
    numero_de_vencedores += 1
    vencedores_nomes += nome_joab + ", "

if duda_venceu and duda_tentativa_da_vitoria == menor_tentativa:
    numero_de_vencedores += 1
    vencedores_nomes += nome_duda + ", "


if numero_de_vencedores == 1:
    nome_vencedor = vencedores_nomes[:-2] 
    print(f"O vencedor é {nome_vencedor}!")
elif numero_de_vencedores > 1:
    nomes_empate = vencedores_nomes[:-2]
    print(f"Houve empate entre: {nomes_empate}")