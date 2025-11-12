def particao(n, k):
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return particao(n, k - 1) + particao(n - k, k)
print("DOCES OU TRAVESSURAS???")
doces = int(input())
quant_particao = particao(doces, doces)
print(f"sem travessuras por hoje! tenho {quant_particao} sacolinhas pra vocês")
if quant_particao % 2 == 0:
    print("doces equilibrados, sem travessuras!")
else:
    print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")
