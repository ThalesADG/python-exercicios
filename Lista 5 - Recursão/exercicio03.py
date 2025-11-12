ALFABETO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Decifrando mensagem do Trickster...")

chave_inicial = input()
frase_criptografada = input()

def decifrar_recursivo(frase, chave_atual, indice=0, mensagem_decifrada="", armadilhas=[]):
    if indice == len(frase):
        return mensagem_decifrada, armadilhas

    letra = frase[indice]

    if letra in ALFABETO:
        Ci = ALFABETO.index(letra)
        Ki = ALFABETO.index(chave_atual)
        Mi = (Ci - Ki) % 26
        letra_decifrada = ALFABETO[Mi]

        return decifrar_recursivo(frase, letra_decifrada, indice + 1, mensagem_decifrada + letra_decifrada, armadilhas)

    else:
        armadilhas.append(indice)
        return decifrar_recursivo(frase, chave_atual, indice + 1, mensagem_decifrada, armadilhas)


mensagem_final, armadilhas = decifrar_recursivo(frase_criptografada, chave_inicial)

if armadilhas:
    armadilhas_str = [str(i) for i in armadilhas]
    print(f"Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: {', '.join(armadilhas_str)}")
else:
    print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")


print(f"Mensagem revelada: {mensagem_final}")
