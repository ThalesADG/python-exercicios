ANDRE = "andre"
BRUNO = "bruno"
CLARA = "clara"

andre_bolinhas = int(input())
bruno_bolinhas = int(input())
clara_bolinhas = int(input())

andre_erros = 0
bruno_erros = 0
clara_erros = 0

andre_ativo = andre_bolinhas > 0
bruno_ativo = bruno_bolinhas > 0
clara_ativo = clara_bolinhas > 0

jogadores_ativos = 0
if andre_ativo:
    jogadores_ativos += 1
if bruno_ativo:
    jogadores_ativos += 1
if clara_ativo:
    jogadores_ativos += 1
    
turno = 0

while jogadores_ativos > 1:
    
    # Vez do André
    if turno % 3 == 0:
        if andre_ativo:
            resultado = input()
            if resultado == "acertou":
                andre_erros = 0
                if bruno_ativo:
                    andre_bolinhas += 1
                    bruno_bolinhas -= 1
                    if bruno_bolinhas == 0:
                        print(f"{BRUNO} saiu do jogo")
                        bruno_ativo = False
                        jogadores_ativos -= 1
                if clara_ativo:
                    andre_bolinhas += 1
                    clara_bolinhas -= 1
                    if clara_bolinhas == 0:
                        print(f"{CLARA} saiu do jogo")
                        clara_ativo = False
                        jogadores_ativos -= 1
            else: # errou
                andre_erros += 1
                if andre_erros == 3:
                    print(f"{ANDRE} perdeu feio")
                    andre_ativo = False
                    jogadores_ativos -= 1

    # Vez do Bruno
    elif turno % 3 == 1:
        if bruno_ativo:
            resultado = input()
            if resultado == "acertou":
                bruno_erros = 0
                if andre_ativo:
                    bruno_bolinhas += 1
                    andre_bolinhas -= 1
                    if andre_bolinhas == 0:
                        print(f"{ANDRE} saiu do jogo")
                        andre_ativo = False
                        jogadores_ativos -= 1
                if clara_ativo:
                    bruno_bolinhas += 1
                    clara_bolinhas -= 1
                    if clara_bolinhas == 0:
                        print(f"{CLARA} saiu do jogo")
                        clara_ativo = False
                        jogadores_ativos -= 1
            else: # errou
                bruno_erros += 1
                if bruno_erros == 3:
                    print(f"{BRUNO} perdeu feio")
                    bruno_ativo = False
                    jogadores_ativos -= 1
    
    # Vez da Clara
    elif turno % 3 == 2:
        if clara_ativo:
            resultado = input()
            if resultado == "acertou":
                clara_erros = 0
                if andre_ativo:
                    clara_bolinhas += 1
                    andre_bolinhas -= 1
                    if andre_bolinhas == 0:
                        print(f"{ANDRE} saiu do jogo")
                        andre_ativo = False
                        jogadores_ativos -= 1
                if bruno_ativo:
                    clara_bolinhas += 1
                    bruno_bolinhas -= 1
                    if bruno_bolinhas == 0:
                        print(f"{BRUNO} saiu do jogo")
                        bruno_ativo = False
                        jogadores_ativos -= 1
            else: # errou
                clara_erros += 1
                if clara_erros == 3:
                    print(f"{CLARA} perdeu feio")
                    clara_ativo = False
                    jogadores_ativos -= 1

    turno += 1

if andre_ativo:
    print(f"{ANDRE} ganhou")
elif bruno_ativo:
    print(f"{BRUNO} ganhou")
elif clara_ativo:
    print(f"{CLARA} ganhou")

print("a quantidade final de bolas foi:")
print(f"{ANDRE}: {andre_bolinhas}")
print(f"{BRUNO}: {bruno_bolinhas}")
print(f"{CLARA}: {clara_bolinhas}")