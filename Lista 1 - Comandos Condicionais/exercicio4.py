sheldonArtigos = int(input())
leonardArtigos = int(input())
rajArtigos = int(input())
howardArtigos = int(input())

sheldonExperimentos = int(input())
leonardExperimentos = int(input())
rajExperimentos = int(input())
howardExperimentos = int(input())

sheldonPontuacao = sheldonArtigos * 2 + sheldonExperimentos * 3
leonardPontuacao = leonardArtigos * 2 + leonardExperimentos * 3
rajPontuacao = rajArtigos * 2 + rajExperimentos * 3
howardPontuacao = howardArtigos * 2 + howardExperimentos * 3

print(f"Pontuação final:\nSheldon: {sheldonPontuacao}\nLeonard: {leonardPontuacao}\nRaj: {rajPontuacao}\nHoward: {howardPontuacao}\n")

maiorPontuacao = max(sheldonPontuacao, leonardPontuacao, rajPontuacao, howardPontuacao)

if sheldonPontuacao == maiorPontuacao:
    cientSem = "Sheldon"
elif leonardPontuacao == maiorPontuacao:
    cientSem = "Leonard"
elif rajPontuacao == maiorPontuacao:
    cientSem = "Raj"
else:
    cientSem = "Howard"

print(f"O cientista da semana é: {cientSem}")

if cientSem == "Sheldon":
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif cientSem == "Leonard":
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif cientSem == "Raj":
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
else:
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")