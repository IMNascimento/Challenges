valor_centavos = int(float(input()) * 100)
notas_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

quantidade = {}

for nota_moeda in notas_moedas:
    qtd_notas_moedas = valor_centavos // nota_moeda
    valor_centavos %= nota_moeda
    quantidade[nota_moeda] = qtd_notas_moedas

print("NOTAS:")
print(f"{quantidade[10000]} nota(s) de R$ 100.00")
print(f"{quantidade[5000]} nota(s) de R$ 50.00")
print(f"{quantidade[2000]} nota(s) de R$ 20.00")
print(f"{quantidade[1000]} nota(s) de R$ 10.00")
print(f"{quantidade[500]} nota(s) de R$ 5.00")
print(f"{quantidade[200]} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{(quantidade[100] % 200)} moeda(s) de R$ 1.00")
print(f"{(quantidade[50] % 100)} moeda(s) de R$ 0.50")
print(f"{(quantidade[25] % 50)} moeda(s) de R$ 0.25")
print(f"{(quantidade[10] % 25)} moeda(s) de R$ 0.10")
print(f"{(quantidade[5] % 10)} moeda(s) de R$ 0.05")
print(f"{(quantidade[1] % 5)} moeda(s) de R$ 0.01")