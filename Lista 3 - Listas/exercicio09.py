print("Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!")

jogadores = input().split(", ")

for i in range(len(jogadores)):
    jogadores[i] = jogadores[i].capitalize()

print(f"{jogadores[0]} e {jogadores[1]} disputarão entre si.")

numeros_dos_jogadores = []
for nome in jogadores:
    entrada = input().split()
    numeros = []
    for i in range(len(entrada)):
        numeros.append(int(entrada[i]))
    numeros_dos_jogadores.append(numeros)

pontuacoes = []
matrizes_calculadas = []
numeros_desempate = []

for i in range(len(jogadores)):
    numeros = numeros_dos_jogadores[i]
    numeros.sort()
    
    menores = numeros[0:3]
    maiores = numeros[len(numeros)-3 : len(numeros)]
    
    numeros_do_meio = numeros[3 : len(numeros)-3]
    
    restantes = numeros_do_meio[0:3]
    numero_desempate_jogador = numeros_do_meio[3]
    
    numeros_desempate.append(numero_desempate_jogador)

    consecutivos = []
    for j in range(3):
        consecutivos.append(restantes[j] + 1)

    matriz_para_imprimir = [maiores, menores, consecutivos]
    matrizes_calculadas.append(matriz_para_imprimir)

    det = (
        matriz_para_imprimir[0][0]*matriz_para_imprimir[1][1]*matriz_para_imprimir[2][2] +
        matriz_para_imprimir[0][1]*matriz_para_imprimir[1][2]*matriz_para_imprimir[2][0] +
        matriz_para_imprimir[0][2]*matriz_para_imprimir[1][0]*matriz_para_imprimir[2][1] -
        matriz_para_imprimir[0][2]*matriz_para_imprimir[1][1]*matriz_para_imprimir[2][0] -
        matriz_para_imprimir[0][0]*matriz_para_imprimir[1][2]*matriz_para_imprimir[2][1] -
        matriz_para_imprimir[0][1]*matriz_para_imprimir[1][0]*matriz_para_imprimir[2][2]
    )
    
    pontuacoes.append(det)

for i in range(len(jogadores)):
    matriz_jogador = matrizes_calculadas[i]
    linha_maiores = matriz_jogador[0]
    linha_menores = matriz_jogador[1]
    linha_consec = matriz_jogador[2]
    
    print(f"{linha_maiores[0]} {linha_maiores[1]} {linha_maiores[2]}")
    print(f"{linha_menores[0]} {linha_menores[1]} {linha_menores[2]}")
    print(f"{linha_consec[0]} {linha_consec[1]} {linha_consec[2]}")
    
    print(f"{jogadores[i]} está com pontuação {pontuacoes[i]} pontos.")

pontos_j0 = pontuacoes[0]
pontos_j1 = pontuacoes[1]
    
nome_ganhador = ""
houve_empate_final = False

if pontos_j0 == pontos_j1:
    print("RODADA DESEMPATE!!")
    desempate_j0 = numeros_desempate[0]
    desempate_j1 = numeros_desempate[1]
    
    if desempate_j0 > desempate_j1:
        nome_ganhador = jogadores[0]
        print(f"Contra todas as expectativas (inclusive as nossas), {jogadores[0]} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {jogadores[1]}. Melhor sorte no próximo flop!")
    elif desempate_j1 > desempate_j0:
        nome_ganhador = jogadores[1]
        print(f"Contra todas as expectativas (inclusive as nossas), {jogadores[1]} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {jogadores[0]}. Melhor sorte no próximo flop!")
    else:
        print("Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!")
        houve_empate_final = True
elif pontos_j0 > pontos_j1:
    nome_ganhador = jogadores[0]
else:
    nome_ganhador = jogadores[1]

if not houve_empate_final:
    print(f"Com talento duvidoso e esforço máximo, a vitória é de {nome_ganhador}!")