def encontrar_menor_caminho(matrix, linha, coluna, passos_dados, max_passos, memo):
    
    tamanho = len(matrix)
    
    if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
        return float('inf')

    if matrix[linha][coluna] == 'A' or matrix[linha][coluna] == '.':
        return float('inf')

    if passos_dados > max_passos:
        return float('inf')

    if passos_dados >= memo[linha][coluna]:
        return float('inf')

    memo[linha][coluna] = passos_dados

    if matrix[linha][coluna] == 'S':
        return passos_dados

    celula_original = matrix[linha][coluna]
    
    matrix[linha][coluna] = '.'

    custo_cima = encontrar_menor_caminho(matrix, linha - 1, coluna, passos_dados + 1, max_passos, memo)
    custo_baixo = encontrar_menor_caminho(matrix, linha + 1, coluna, passos_dados + 1, max_passos, memo)
    custo_esq = encontrar_menor_caminho(matrix, linha, coluna - 1, passos_dados + 1, max_passos, memo)
    custo_dir = encontrar_menor_caminho(matrix, linha, coluna + 1, passos_dados + 1, max_passos, memo)

    matrix[linha][coluna] = celula_original
    
    return min(custo_cima, custo_baixo, custo_esq, custo_dir)


horario_str = input()

partes_horario = horario_str.split(':')
hh = int(partes_horario[0])
mm = int(partes_horario[1])

n = int(input())

mapa = []
pos_inicial_lin, pos_inicial_col = -1, -1

for i in range(n):
    linha_atual = list(input())
    if 'B' in linha_atual:
        pos_inicial_lin = i
        pos_inicial_col = linha_atual.index('B')
    mapa.append(linha_atual)

valor_infinito = float('inf') 
memoizacao = [[valor_infinito for _ in range(n)] for _ in range(n)]

minutos_limite = 60 - mm 
print(f"O relógio marca {hh} horas e {mm} minuto(s)! Byte tem apenas {minutos_limite} minuto(s) para escapar!")

tempo_necessario = encontrar_menor_caminho(mapa, pos_inicial_lin, pos_inicial_col, 0, minutos_limite, memoizacao)

if tempo_necessario <= minutos_limite:
    print(f"CONSEGUIMOS!! Byte precisou de {tempo_necessario} minuto(s) para conseguir escapar!")
    
    minutos_de_folga = minutos_limite - tempo_necessario
    
    if minutos_de_folga > 10:
        print(f"Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {minutos_de_folga} minutos para elas acordarem")
    else:
        print("Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim.")

else:
    print("NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!")
