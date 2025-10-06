nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
aulas = int(input())
faltas = int(input())

media = (nota1+nota2+nota3) / 3 
presenca = (1 - (faltas/aulas)) * 100

print(f"Chris, você conseguiu média {media:.2f} e {presenca:.2f}% de presença.")

if media >= 8 and presenca >= 75:
    print("Chris está APROVADO por nota e por presença! 🎉\nPisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.")
elif 8 > media >= 7 and presenca >= 75:
    print("Chris está APROVADO! ✅\nSacomé, né? Passou raspando, mas a pizza ainda ficou longe.")
elif media >= 7 and presenca < 75:
    print("Chris ESTÁ REPROVADO por FALTA. ❌\nTrágico! Não adianta só saber, tem que aparecer.")
elif media < 7 and presenca >= 75:
    print("Chris ESTÁ REPROVADO por NOTA. ❌\nChris, já pro seu quarto ou eu vou te bater até você virar o avesso!")
else:
    print("Chris ESTÁ REPROVADO por NOTA e por FALTA. ❌\nChris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele.")