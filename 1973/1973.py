N = int(input())
carneiros = list(map(int, input().split()))

estrelas_atacadas = 0
carneiros_nao_roubados = sum(carneiros)

i = 0
while 0 <= i < N:
    estrelas_atacadas += 1
    carneiros_nao_roubados -= 1
    if carneiros[i] % 2 == 1:
        i += 1
    else:
        i -= 1

print(estrelas_atacadas, carneiros_nao_roubados)