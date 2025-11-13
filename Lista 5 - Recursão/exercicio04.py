def eh_seguro(ala_teste, lote_teste, posicoes):
    for ala_anterior in range(ala_teste):
        lote_anterior = posicoes[ala_anterior]
        if lote_anterior == lote_teste:
            return False
        if abs(ala_anterior - ala_teste) == abs(lote_anterior - lote_teste):
            return False
    return True


def contar_solucoes(ala_atual, n, ala_proibida, lote_proibido, posicoes):
    if ala_atual == n:
        return 1

    total_count = 0
    
    for lote_atual in range(n):
        eh_lote_proibido = (ala_atual == ala_proibida and lote_atual == lote_proibido)
        
        if (not eh_lote_proibido) and eh_seguro(ala_atual, lote_atual, posicoes): 
            posicoes[ala_atual] = lote_atual
            total_count += contar_solucoes(ala_atual + 1, n, ala_proibida, lote_proibido, posicoes)
            
    return total_count


def processar_entradas():
    ala_ocupada = int(input())
    lote_ocupado = int(input())

    eh_valido = (1 <= ala_ocupada <= n and 1 <= lote_ocupado <= n)

    if eh_valido:
        print(f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({ala_ocupada}, {lote_ocupado})!")
        print()

        ala_proibida = ala_ocupada - 1
        lote_proibido = lote_ocupado - 1
        posicoes = [-1] * n 

        total_possibilidades = contar_solucoes(0, n, ala_proibida, lote_proibido, posicoes)

        print(f"Rogério e Chaguinha conseguiram encontrar {total_possibilidades} possíveis posições para as almas se posicionarem sem conflitos!")

        if total_possibilidades == 0:
            print("Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!")
        elif 1 <= total_possibilidades <= 10:
            print("Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!")
        elif total_possibilidades > 50:
            print("Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.")
        elif total_possibilidades > 10:
            print("Uau! São tantas opções que eles até se perderam contando!")
        
    else:
        print(f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({ala_ocupada}, {lote_ocupado}). Assim eles nunca vão conseguir sair do cemitério!")
        processar_entradas()


n = int(input())
processar_entradas()
