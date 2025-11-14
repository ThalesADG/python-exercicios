NOTAS_DISPONIVEIS = [100, 50, 20, 10, 5]
TOTAL_DE_NOTAS = len(NOTAS_DISPONIVEIS)


def encontrar_combinacoes_com_vetor(valor_restante, index_da_nota):
    if valor_restante == 0:
        return [1, [0] * TOTAL_DE_NOTAS]
        
    if valor_restante < 0 or index_da_nota == TOTAL_DE_NOTAS:
        return [0, [0] * TOTAL_DE_NOTAS]

    [formas_sem_usar_nota, usos_sem_usar_nota] = encontrar_combinacoes_com_vetor( valor_restante, index_da_nota + 1)
    
    valor_da_nota_atual = NOTAS_DISPONIVEIS[index_da_nota]
    
    [formas_usando_nota, usos_usando_nota] = encontrar_combinacoes_com_vetor( valor_restante - valor_da_nota_atual, index_da_nota)
    
    total_de_formas = formas_sem_usar_nota + formas_usando_nota
    
    usos_combinados = [0] * TOTAL_DE_NOTAS

    for i in range(TOTAL_DE_NOTAS):
        usos_combinados[i] = usos_sem_usar_nota[i] + usos_usando_nota[i]
        
    if formas_usando_nota > 0:
        usos_combinados[index_da_nota] += formas_usando_nota
    
    return [total_de_formas, usos_combinados]


valor_da_conta = int(input())

print(f"Calculando possibilidades para o valor: {valor_da_conta}")

[total_possibilidades, contagem_de_uso] = encontrar_combinacoes_com_vetor(valor_da_conta, 0)

if total_possibilidades == 1:
    print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
elif total_possibilidades == 0:
    print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")

print(f"\nTotal de possibilidades: {total_possibilidades}")
print("\nUso das notas:")

for i in range(TOTAL_DE_NOTAS):
    nota = NOTAS_DISPONIVEIS[i]
    usos = contagem_de_uso[i]
    print(f"R${nota}: usada em {usos} combinações")