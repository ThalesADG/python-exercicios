print("Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!")

fronts_em_campo = 6
backs_em_campo = 6
fronts_no_morto = 0
backs_no_morto = 0

ataque_do_morto = False

time_atacante = input()
while time_atacante != "Front-End" and time_atacante != "Back-End":
    print("Entrada inválida!")
    time_atacante = input()

while fronts_em_campo > 0 and backs_em_campo > 0:

    resultado_ataque = input()
    while resultado_ataque != "acertou" and resultado_ataque != "errou":
        print("Entrada inválida!")
        resultado_ataque = input()

    if resultado_ataque == "acertou":
        if not ataque_do_morto:
            print(f"{time_atacante} acertou um jogador!")
            if time_atacante == "Front-End":
                backs_em_campo -= 1
                backs_no_morto += 1
                time_atacante = "Back-End"
            else:
                fronts_em_campo -= 1
                fronts_no_morto += 1
                time_atacante = "Front-End"
            ataque_do_morto = True

        else:
            print(f"O morto do {time_atacante} acertou um jogador!")
            if time_atacante == "Front-End":
                fronts_no_morto -= 1
                fronts_em_campo += 1
                backs_em_campo -= 1
                backs_no_morto += 1
                time_atacante = "Back-End"
            else:
                backs_no_morto -= 1
                backs_em_campo += 1
                fronts_em_campo -= 1
                fronts_no_morto += 1
                time_atacante = "Front-End"
            ataque_do_morto = True
        
        print(f"Back-End: {backs_em_campo} dev(s) em campo. | Front-End: {fronts_em_campo} dev(s) em campo.")

    else:
        precisa_defesa = False
        if ataque_do_morto:
            precisa_defesa = True
        elif not ataque_do_morto and ((time_atacante == "Front-End" and fronts_no_morto > 0) or (time_atacante == "Back-End" and backs_no_morto > 0)):
            precisa_defesa = True

        if not precisa_defesa:
            if time_atacante == "Front-End":
                time_atacante = "Back-End"
            else:
                time_atacante = "Front-End"
            ataque_do_morto = False
        
        else:
            resultado_defesa = input()
            while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                print("Entrada inválida!")
                resultado_defesa = input()

            if resultado_defesa == "pegou":
                if time_atacante == "Front-End":
                    time_atacante = "Back-End"
                else:
                    time_atacante = "Front-End"
                ataque_do_morto = False
            
            else:
                if not ataque_do_morto:
                    ataque_do_morto = True
                else:
                    ataque_do_morto = False

if backs_em_campo == 0:
    print(f"Vitória do Front-End! Restaram {fronts_em_campo} devs ainda segurando o layout!")
elif fronts_em_campo == 0:
    print(f"Vitória do Back-End! Restaram {backs_em_campo} devs ainda mantendo o servidor de pé!")