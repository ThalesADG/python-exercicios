print("--- Simulador de Cancelamento ---\n")

n = int(input())

artistas_e_seguidores =[]

for i in range(n):
    nome, seguidores = input().split('-')
    artistas_e_seguidores.append([nome.strip(), int(seguidores.strip())])

for i in range(n):
    print(f"A subcelebridade da vez é: {artistas_e_seguidores[i][0]}")
    acontecimento = int(input())
    artistas_e_seguidores[i].append(acontecimento)

    if acontecimento == 1:
        print(f"{artistas_e_seguidores[i][0]} perdeu 10% dos seguidores!")
        artistas_e_seguidores[i][1] = int(artistas_e_seguidores[i][1] * 0.9)
    elif acontecimento == 2:
        print(f"{artistas_e_seguidores[i][0]} ganhou 5% de seguidores!")
        artistas_e_seguidores[i][1] = int(artistas_e_seguidores[i][1] * 1.05)
    elif acontecimento == 3:
        print(f"{artistas_e_seguidores[i][0]} perdeu 15% dos seguidores!")
        artistas_e_seguidores[i][1] = int(artistas_e_seguidores[i][1] * 0.85)
    else:
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

for i in range(len(artistas_e_seguidores) - 1):
    for j in range(len(artistas_e_seguidores) - 1 - i):
        if artistas_e_seguidores[j][1] < artistas_e_seguidores[j + 1][1]:
            artistas_e_seguidores[j], artistas_e_seguidores[j + 1] = artistas_e_seguidores[j + 1], artistas_e_seguidores[j]

print("\n--- RANKING FINAL DE SEGUIDORES ---")

top = min(3, len(artistas_e_seguidores))

for i in range(top):
    nome = artistas_e_seguidores[i][0]
    seguidores = artistas_e_seguidores[i][1]
    print(f"{i+1}º Lugar: {nome} com {seguidores} seguidores.")