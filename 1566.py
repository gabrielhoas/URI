import sys
NC=int(input())
if NC >= 1 and NC < 100:
    for i in range(0, NC, 1):
        N=int(input())
        if N > 1 and N <= 3000000:
            h=[int(x) for x in input().split(maxsplit=N)]
            for j in range(0, len(h), 1):
                if h[j] < 20 or h[j] > 230:
                    sys.exit("O valor de altura deve ser maior ou igual que 20 e menor ou igual que 230.")
            h.sort()
            if i == 0:
                lista=[h]
            else:
                lista.append(h)
        else:
            sys.exit("A quantidade de pessoas deve ser maior que 1 e menor ou igual que 3000000.") 
    for k in range(0, NC, 1):
        print(*lista[k])
else:
    sys.exit("A quantidade de cidades deve ser maior ou igual que 1 e menor que 100.")