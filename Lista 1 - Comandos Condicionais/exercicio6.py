item = input().capitalize()
valor = float(input())
responsavel = input().capitalize()
evento = input().capitalize()

if valor > 100 and responsavel != "Angela":
    status = "Reprovada"
    frase = "Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!"
else:
    if responsavel == "Angela":
        status = "Aprovada"
        if valor > 100:
            frase = "Apenas eu tenho discernimento para gastos desta magnitude."
        else:
            frase = "Compra feita por mim, obviamente dentro dos padrões de excelência."

    elif responsavel == "Michael":
        if item == "Mágica" or item == "Fantasia":
            status = "Reprovada"
            frase = "O Comitê não financia frivolidades e palhaçadas, Michael."
        elif valor > 60:
            status = "Aprovada com ressalvas"
            if evento == "Natal":
                frase = "O espírito natalino de Michael é... excessivo. A nota será conferida."
            else:
                frase = "Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!"
        else:
            status = "Aprovada"
            frase = "Uma compra surpreendentemente sensata vinda do Michael. Suspeito."

    elif evento == "Halloween":
        if item == "Abóbora":
            if valor <= 30:
                status = "Aprovada"
                frase = "Uma abóbora de tamanho e custo razoáveis. Eficiente."
            else:
                status = "Aprovada com ressalvas"
                frase = "Por que uma abóbora precisa ser tão cara? Extravagância."
        else:
            status = "Aprovada com ressalvas"
            frase = "Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo."

    elif evento == "Aniversário":
        if item == "Bolo" and valor <= 40:
            status = "Aprovada"
            frase = "Um bolo modesto para celebrar mais um ano de produtividade, parabéns!"
        elif item == "Sorvete de menta com chocolate":
            status = "Reprovada"
            frase = "Este sabor de sorvete é uma abominação e não entrará em meu evento."
        else:
            status = "Aprovada"
            frase = "Itens de aniversário devem ser práticos, não uma distração do trabalho."

    elif valor > 50:
        status = "Aprovada com ressalvas"
        frase = "Está dentro do orçamento, mas não quer dizer que não vou verificar!"
    else:
        status = "Aprovada"
        frase = "Esta compra não viola nenhum regulamento... por enquanto."

print(f"Compra {status}!\n{frase}")