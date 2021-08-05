instancias = int(input())
if instancias > 0:
    resultado = []
    def teste(objeto):
            if 1 in objeto and 2 in objeto and 3 in objeto and 4 in objeto and 5 in objeto and 6 in objeto and 7 in objeto and 8 in objeto and 9 in objeto:
                return "SIM"
            else:
                return "NAO"
    for i in range(1, instancias+1, 1):
        linha1 = [int(x) for x in input().split(maxsplit=9)]
        linha2 = [int(x) for x in input().split(maxsplit=9)]
        linha3 = [int(x) for x in input().split(maxsplit=9)]
        linha4 = [int(x) for x in input().split(maxsplit=9)]
        linha5 = [int(x) for x in input().split(maxsplit=9)]
        linha6 = [int(x) for x in input().split(maxsplit=9)]
        linha7 = [int(x) for x in input().split(maxsplit=9)]
        linha8 = [int(x) for x in input().split(maxsplit=9)]
        linha9 = [int(x) for x in input().split(maxsplit=9)] 
        linha = [teste(linha1),teste(linha2),teste(linha3),teste(linha4),teste(linha5),teste(linha6),teste(linha7),teste(linha8),teste(linha9)]
        coluna1 = [linha1[0],linha2[0],linha3[0],linha4[0],linha5[0],linha6[0],linha7[0],linha8[0],linha9[0]]
        coluna2 = [linha1[1],linha2[1],linha3[1],linha4[1],linha5[1],linha6[1],linha7[1],linha8[1],linha9[1]]
        coluna3 = [linha1[2],linha2[2],linha3[2],linha4[2],linha5[2],linha6[2],linha7[2],linha8[2],linha9[2]]
        coluna4 = [linha1[3],linha2[3],linha3[3],linha4[3],linha5[3],linha6[3],linha7[3],linha8[3],linha9[3]]
        coluna5 = [linha1[4],linha2[4],linha3[4],linha4[4],linha5[4],linha6[4],linha7[4],linha8[4],linha9[4]]
        coluna6 = [linha1[5],linha2[5],linha3[5],linha4[5],linha5[5],linha6[5],linha7[5],linha8[5],linha9[5]]
        coluna7 = [linha1[6],linha2[6],linha3[6],linha4[6],linha5[6],linha6[6],linha7[6],linha8[6],linha9[6]]
        coluna8 = [linha1[7],linha2[7],linha3[7],linha4[7],linha5[7],linha6[7],linha7[7],linha8[7],linha9[7]]
        coluna9 = [linha1[8],linha2[8],linha3[8],linha4[8],linha5[8],linha6[8],linha7[8],linha8[8],linha9[8]]
        coluna = [teste(coluna1),teste(coluna2),teste(coluna3),teste(coluna4),teste(coluna5),teste(coluna6),teste(coluna7),teste(coluna8),teste(coluna9)]
        matriz1 = sum([linha1[0:3],linha2[0:3],linha3[0:3]],[])
        matriz2 = sum([linha4[0:3],linha5[0:3],linha6[0:3]],[])
        matriz3 = sum([linha7[0:3],linha8[0:3],linha9[0:3]],[])
        matriz4 = sum([linha1[3:6],linha2[3:6],linha3[3:6]],[])
        matriz5 = sum([linha4[3:6],linha5[3:6],linha6[3:6]],[])
        matriz6 = sum([linha7[3:6],linha8[3:6],linha9[3:6]],[])
        matriz7 = sum([linha1[6:9],linha2[6:9],linha3[6:9]],[])
        matriz8 = sum([linha4[6:9],linha5[6:9],linha6[6:9]],[])
        matriz9 = sum([linha7[6:9],linha8[6:9],linha9[6:9]],[])
        matriz = [teste(matriz1),teste(matriz2),teste(matriz3),teste(matriz4),teste(matriz5),teste(matriz6),teste(matriz7),teste(matriz8),teste(matriz9)]
        if "NAO" in linha or "NAO" in coluna or "NAO" in matriz:
            resultado.append("NAO")
        else:
            resultado.append("SIM")
    for j in range(1, instancias+1, 1):
        print("Instancia",j)
        print(resultado[j-1])
        if j <= instancias+1:
            print("")