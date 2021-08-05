valor=round(float(input()),2)
lista=[100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]
dinheiro=[]
for custo in lista:
    dinheiro.append(int(valor/custo))
    valor-=dinheiro[len(dinheiro)-1]*custo
print("NOTAS:")
print(dinheiro[0],"nota(s) de R$ 100.00")
print(dinheiro[1],"nota(s) de R$ 50.00")
print(dinheiro[2],"nota(s) de R$ 20.00")
print(dinheiro[3],"nota(s) de R$ 10.00")
print(dinheiro[4],"nota(s) de R$ 5.00")
print(dinheiro[5],"nota(s) de R$ 2.00")
print("MOEDAS:")
print(dinheiro[6],"moeda(s) de R$ 1.00")
print(dinheiro[7],"moeda(s) de R$ 0.50")
print(dinheiro[8],"moeda(s) de R$ 0.25")
print(dinheiro[9],"moeda(s) de R$ 0.10")
print(dinheiro[10],"moeda(s) de R$ 0.05")
print(dinheiro[11],"moeda(s) de R$ 0.01")