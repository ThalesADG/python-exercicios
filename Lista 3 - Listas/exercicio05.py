projeto = input()

componentes_validos = []
componentes_invalidos = []

if projeto == "Memória ROM Simples":
    requisitos = [["Redstone", 256], ["Repetidores", 64], ["Tochas de Redstone", 128]]
elif projeto == "Calculadora de 4 bits":
    requisitos = [["Redstone", 512], ["Repetidores", 128], ["Tochas de Redstone", 64], ["Lâmpadas de Redstone", 256]]
elif projeto == "Sequenciador Musical":
    requisitos = [["Redstone", 1024], ["Repetidores", 256], ["Blocos de Notas", 64], ["Observadores", 128]]
elif projeto == "Processador de 8 Bits":
    requisitos = [["Redstone", 4096], ["Repetidores", 1024], ["Lâmpadas de Redstone", 2048], ["Pistões Aderentes", 512]]
elif projeto == "Display de Vídeo 8x8":
    requisitos = [["Redstone", 2048], ["Repetidores", 512], ["Comparadores", 256], ["Pistões", 128]]
elif projeto == "Supercomputador V13":
    requisitos = [["Redstone", 8192], ["Repetidores", 2048], ["Comparadores", 1024], ["Pistões Aderentes", 1024]]

validos = [item[0] for item in requisitos]

receber = True
while receber:
    entrada = input()
    if entrada == "Construir!":
        suficientes = True
        totais_encontrados = []

        for req_nome, req_qtd in requisitos:
            total_encontrado = 0
            for nome, qtd in componentes_validos:
                if nome == req_nome:
                    total_encontrado += qtd

            totais_encontrados.append(total_encontrado)
            if total_encontrado < req_qtd:
                suficientes = False

        print()

        if suficientes:
            print(f"Viniccius13 conseguiu construir o {projeto}! Partiu programar!")
            print()
            print(f"Para construirmos a(o) {projeto}, utilizamos:")
            print()
            for nome, qtd in componentes_validos:
                print(f"{nome} : {qtd}")
            if len(componentes_invalidos) > 0:
                print()
                print("Mas, em nossa jornada, também coletamos:")
                print()
                for nome, qtd in componentes_invalidos:
                    print(f"{nome} : {qtd}")
            receber = False
        else:
            print(f"Ainda não é possível construir o {projeto}! Faltam:")
            print()
            for i in range(len(requisitos)):
                req_nome = requisitos[i][0]
                req_qtd = requisitos[i][1]
                total_encontrado = totais_encontrados[i]
                faltando = req_qtd - total_encontrado
                if faltando > 0:
                    packs = faltando // 64
                    if packs == 0:
                        packs = 1
                    print(f"{packs} pack(s) de {req_nome}")
            print()

    else:
        lista_palavras = entrada.split()
        quantidade = int(lista_palavras[-1])
        componente = " ".join(lista_palavras[:-1])

        if componente in validos:
            item_ja_existe = False
            for item in componentes_validos:
                if item[0] == componente:
                    item[1] += quantidade
                    item_ja_existe = True

            if not item_ja_existe:
                componentes_validos.append([componente, quantidade])
            
            if componente == "Redstone":
                print(f"Mais redstone! A energia que move o progresso! (+{quantidade} Redstone)")
            elif componente == "Repetidores":
                print(f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{quantidade} Repetidores)")
            elif componente == "Tochas de Redstone":
                print(f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{quantidade} Tochas de Redstone)")
            elif componente == "Lâmpadas de Redstone":
                print(f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{quantidade} Lâmpadas de Redstone)")
            elif componente == "Blocos de Notas":
                print(f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{quantidade} Blocos de Notas)")
            elif componente == "Observadores":
                print(f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{quantidade} Observadores)")
            elif componente == "Comparadores":
                print(f"Comparadores para a lógica! A precisão é a alma do negócio. (+{quantidade} Comparadores)")
            elif componente == "Pistões":
                print(f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{quantidade} Pistões)")
            elif componente == "Pistões Aderentes":
                print(f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{quantidade} Pistões Aderentes)")
        else:
            item_ja_existe = False
            for item in componentes_invalidos:
                if item[0] == componente:
                    item[1] += quantidade
                    item_ja_existe = True

            if not item_ja_existe:
                componentes_invalidos.append([componente, quantidade])

            print(f"Hmm, {componente} não parece ser útil para este projeto.")
