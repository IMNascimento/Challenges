import math

V, N = map(int, input().split())
resultados = []

for percentual in range(10, 100, 10):
    placas_necessarias = math.ceil(V * percentual * N / 100)
    resultados.append(placas_necessarias)

print(*resultados)