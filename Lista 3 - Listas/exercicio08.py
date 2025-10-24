FRASE_CANCELAR = "WhatsApp: 0 mensagens."
FRASE_ORGANIZAR = "CABOSSE! Bora simbora organizar essa festa."

grupo_influencers = ["Sofia Santino", "Doarda", "Ciclopin", "Bruna Pinheiro"]
grupo_cantores = [
    "Thiaguinho", "Little Thiago", 
    "Neiff", "O Diferenciado", 
    "Veigh", "Mc Loma"
]

lista_de_presenca = []
parada_cancelar = False
parada_organizar = False

while (parada_cancelar == False) and (parada_organizar == False):
    linha = input()
    
    if linha == FRASE_CANCELAR:
        parada_cancelar = True
    elif linha == FRASE_ORGANIZAR:
        parada_organizar = True
    else:
        partes = linha.split()
        nome_completo = " ".join(partes[:-3])
        lista_de_presenca.append(nome_completo)


if parada_cancelar:
    print("I hate to tell you this BUT")
    print("Bia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira")
    print()
    print("Como a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:")
    print("Essa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.")
    print("E o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.")
    print("Espera esfriar e você vai barbarizar quando tiver pronto")
    print("É isso, tchau meus amores")

elif parada_organizar:
    
    total_influencers = 0
    total_cantores = 0
    
    for nome in lista_de_presenca:
        if nome in grupo_influencers:
            total_influencers += 1
        elif nome in grupo_cantores:
            total_cantores += 1
            
    if "Mc Loma" in lista_de_presenca:
        lista_de_presenca.append("Mirella Santos")
        lista_de_presenca.append("Mariely Santos")

    convidados_formatado = ", ".join(lista_de_presenca)
    
    tem_influencer = total_influencers > 0
    tem_cantor = total_cantores > 0

    
    if (tem_influencer and tem_cantor) or (not tem_influencer and not tem_cantor):
        print("Cachaçaria na minha casa hoje, 21h.")
        print("Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!")
    
    elif tem_influencer:
        print("<TARDE DE FOFOCAS>")
        print(f"Convidados: {convidados_formatado}.")
        
        for i in range(total_influencers):
            pauta_lida = input()
            
            if pauta_lida == "Medo de ficar musculosa demais por causa da academia":
                print("AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!")
            elif pauta_lida == "O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?":
                print("Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)")
            elif pauta_lida == "Meu chefe só me dá um dia de folga, mas eu precisava de dois.":
                print("Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!")
            elif pauta_lida == "Pessoas que adoram se fazer de coitadinhas":
                print("Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir.")
            elif pauta_lida == "Essa história de que homem sofre calado":
                print("Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???")
        
        votos_concordia = int(input())
        if votos_concordia == 0:
            print("Apois me interne, me prenda, me jogue fora que eu tô maluca!")
        else:
            print("É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês.")

    elif tem_cantor:
        print("<PLANOS PARA FESTA>")
        print(f"Convidados: {convidados_formatado}.")
        print("Tipo de comemoração: Paredão - Show na minha casa!!")