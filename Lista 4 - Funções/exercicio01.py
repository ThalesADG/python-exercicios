def ataques(tipo, saude):
    if tipo == "Você não tem o que é necessário para escalar.":
        saude -= 20
        print("Eu nunca vou conseguir chegar ao topo :(")
    else:
        saude -= 50
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
    return saude

def reacoes(tipo, saude):
    if tipo == "Calma Badeline, nós vamos conseguir.":
        saude += 25
    elif tipo == "Eu sei que somos capazes! Vamos em frente!":
        respiracoes = int(input())
        saude += respiracoes * 10
    else:
        saude += 60
    return saude

vida = 100
while vida < 150 and vida > 0:
    ataque = input()
    vida = ataques(ataque, vida)
    if vida > 0:
        reacao = input()
        vida = reacoes(reacao, vida)

if vida >= 150:
    print("Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.")
else:
    print("Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.")
