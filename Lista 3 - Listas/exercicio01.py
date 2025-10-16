frases = ["Que tiro foi esse?", "Segura a marimba", "Tá com raiva? Morde as costas", "Bateu de frente é só rajadão"]

quantidade_de_novas_frases = int(input())

for i in range(quantidade_de_novas_frases):
    nova_frase = input()
    frases.append(nova_frase)

vistos = []
for frase in frases:
    if frase not in vistos:
        vistos.append(frase)

for frase in vistos:
    print(f'"{frase}": {frases.count(frase)}')

frases.sort()
print(frases)
