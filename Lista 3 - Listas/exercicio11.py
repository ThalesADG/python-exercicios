board = []
i = 0
while i < 9:
    linha = input().split()
    board.append(linha)
    i += 1

vazios = []
i = 0
while i < 9:
    j = 0
    while j < 9:
        if board[i][j] == '.':
            vazios.append([i, j])
        j += 1
    i += 1

indice = 0
while indice < len(vazios):
    linha = vazios[indice][0]
    coluna = vazios[indice][1]
    num_atual = board[linha][coluna]
    achou = False
    inicio = '1'

    if num_atual != '.':
        inicio = str(int(num_atual) + 1)

    num = inicio
    while int(num) <= 9 and not achou:
        valido = True

        j = 0
        while j < 9:
            if board[linha][j] == num:
                valido = False
            j += 1

        i = 0
        while i < 9:
            if board[i][coluna] == num:
                valido = False
            i += 1

        inicio_linha = (linha // 3) * 3
        inicio_coluna = (coluna // 3) * 3
        i = inicio_linha
        while i < inicio_linha + 3:
            j = inicio_coluna
            while j < inicio_coluna + 3:
                if board[i][j] == num:
                    valido = False
                j += 1
            i += 1

        if valido:
            board[linha][coluna] = num
            achou = True
            indice += 1
        else:
            num = str(int(num) + 1)

    if not achou:
        board[linha][coluna] = '.'
        indice -= 1

print("Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!")
i = 0
while i < 9:
    print(" ".join(board[i]))
    i += 1
