operacao = input() 
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
elementos_acima_diagonal_secundaria = 0

for i in range(11):
    for j in range(12 - i, 12):
        soma += matriz[i][j]
        elementos_acima_diagonal_secundaria += 1

if operacao == 'M':
    resultado = soma / elementos_acima_diagonal_secundaria
else:
    resultado = soma

print(f'{resultado:.1f}')
#erro Wrong answer (70%)
# -3603.3 apresentada
# +72020.9 esperada
