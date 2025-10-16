numero_convidados = int(input())
convidados_aceitos = []
comidas_presentes = []

for i in range(numero_convidados):
    convidado = input()
    comida = input()
    preco = int(input())

    if convidado == "Maicon Kuster":
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    else:
        if comida in comidas_presentes:
            print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {convidado}")
        else:
            comidas_presentes.append(comida)
            convidados_aceitos.append([preco, convidado, comida])

if not convidados_aceitos:
    print("Nenhum convidado marcou presença na festa do calabreso!")
else:
    convidados_aceitos.sort()

    convidado_caro = convidados_aceitos[-1]
    print(f"Obrigado para o(a) {convidado_caro[1]} pelo(a) excelente {convidado_caro[2]}")
    
    if len(convidados_aceitos) > 1:
        convidado_barato = convidados_aceitos[0]
        print(f"Rapaz, {convidado_barato[1]} trouxe o(a) {convidado_barato[2]} que estava altamente mais ou menos!!!")

    print("Lista de convidados do Calabreso")
    for i in range(len(convidados_aceitos)):
        print(f"{i + 1}- {convidados_aceitos[i][1]}")