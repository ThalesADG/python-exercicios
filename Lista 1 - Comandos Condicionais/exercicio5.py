xTed = int(input())
yTed = int(input())
xGc = int(input())
yGc = int(input())
amigo = input()

distOrig = ((xGc - xTed) ** 2 + (yGc - yTed) ** 2) ** 0.5

if amigo == "Barney":
    distFin = round(distOrig + 10)
elif amigo == "Marshall":
    distFin = round(distOrig - 5)
elif amigo == "Lily":
    distFin = round(distOrig - 10)
else:
    distFin = round(distOrig + 5)

print(f"Pelos meus cálculos a distância final encontrada foi {distFin}!")

if distFin <= 50:
    if amigo == "Barney":
        print("Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário que eu poderia até ter pego ele pra mim! Desafio aceito!")
    elif amigo == "Marshall":
        print("Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!")
    elif amigo == "Lily":
        print("Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. O guarda-chuva está aqui, e nem nos cansamos muito!")
    else:
        print("Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. O guarda-chuva está bem aqui, Ted. Onde está o mistério?")
else:
    if amigo == "Barney":
        print("Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho para uma noite lendária! Challenge accepted, vista seu terno!")
    elif amigo == "Marshall":
        print("Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa. Vamos tentar de novo amanhã.")
    elif amigo == "Lily":
        print("Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! Fiquei com fome de tanta caminhada.")
    else:
        print("Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato.")