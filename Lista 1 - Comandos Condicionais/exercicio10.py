print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")

quant_pessoas = int(input())

if quant_pessoas == 0:
    quant_cervejas_sozinho = int(input())
    print()
    print("Relatório da situação de Ted:")
    print("Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.")
    print(f"- Quantidade de cervejas bebidas por Ted: {quant_cervejas_sozinho} cervejas.")

else:
    print("Hora da lista dos amigos da vez!")

    e_barney = False
    e_robin = False
    e_marshall = False
    e_lily = False

    nome1 = ""
    nome2 = ""
    nome3 = ""
    nome4 = ""

    lugar = ""
    quant_total_cervejas = None

    if quant_pessoas == 1:
        nome1 = input()
    elif quant_pessoas == 2:
        nome1 = input()
        nome2 = input()
    elif quant_pessoas == 3:
        nome1 = input()
        nome2 = input()
        nome3 = input()
    elif quant_pessoas == 4:
        nome1 = input()
        nome2 = input()
        nome3 = input()
        nome4 = input()

    if nome1 != "":
        if nome1 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
            e_barney = True
        elif nome1 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
            e_robin = True
        elif nome1 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
            e_marshall = True
        elif nome1 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
            e_lily = True
        else:
            print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    if nome2 != "":
        if nome2 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
            e_barney = True
        elif nome2 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
            e_robin = True
        elif nome2 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
            e_marshall = True
        elif nome2 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
            e_lily = True
        else:
            print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    if nome3 != "":
        if nome3 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
            e_barney = True
        elif nome3 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
            e_robin = True
        elif nome3 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
            e_marshall = True
        elif nome3 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
            e_lily = True
        else:
            print(f"{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    if nome4 != "":
        if nome4 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
            e_barney = True
        elif nome4 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
            e_robin = True
        elif nome4 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
            e_marshall = True
        elif nome4 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
            e_lily = True
        else:
            print(f"{nome4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    lugar = input()
    if lugar == "MacLaren’s Pub":
        quant_media_cervejas = int(input())
        quant_total_cervejas = (quant_pessoas + 1) * quant_media_cervejas

    if quant_pessoas == 2 and e_marshall and e_lily:
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    if quant_pessoas == 2 and e_barney and e_marshall:
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    if quant_pessoas == 4 and e_barney and e_robin and e_marshall and e_lily:
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")

    if e_barney and lugar == "Arena de Laser Tag":
        print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")

    if quant_pessoas == 1 and e_robin and lugar == "Carmichael’s":
        print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")

    if lugar == "MacLaren’s Pub":
        if e_barney or e_robin or e_marshall or e_lily:
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        else:
            print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")

    print()
    print("Relatório da situação de Ted:")

    nomes_consoladores = ""
    if quant_pessoas == 1:
        nomes_consoladores = nome1
    elif quant_pessoas == 2:
        nomes_consoladores = f"{nome1} e {nome2}"
    elif quant_pessoas == 3:
        nomes_consoladores = f"{nome1}, {nome2} e {nome3}"
    elif quant_pessoas == 4:
        nomes_consoladores = f"{nome1}, {nome2}, {nome3} e {nome4}"

    print(f"- Ted foi consolado por: {nomes_consoladores}.")
    print(f"- O local de afogar as mágoas foi: {lugar}.")

    if quant_pessoas == 1:
        frase_quantidade = "Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas."
    elif quant_pessoas == 2:
        frase_quantidade = "Duas pessoas se compadeceram com a situação do pobre Ted."
    elif quant_pessoas == 3:
        frase_quantidade = "Três pessoas! Ted conseguiu se divertir bastante."
    elif quant_pessoas == 4:
        if e_barney and e_robin and e_marshall and e_lily:
            frase_quantidade = "O quinteto junto consegue resolver qualquer problema!"
        else:
            frase_quantidade = "Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre."

    print(f"- {frase_quantidade}")

    if quant_total_cervejas is not None:
        print(f"- Quantidade de cervejas bebidas pelo grupo: {quant_total_cervejas} cervejas.")

    print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")
