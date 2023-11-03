def ordem_de_ordenacao(num, m):
    if num < 0:
        return (0, num)
    if num % 2 == 1:
        return (1, num % m, -num)
    else:
        return (2, num % m, num)

caso = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    numeros = []
    for _ in range(N):
        numero = int(input())
        numeros.append(numero)

    numeros.sort(key=lambda x: ordem_de_ordenacao(x, M))

    print(f"{abs(N)} {abs(M)}")
    for num in numeros:
        print(abs(num))

    caso += 1
#não concluido ainda tem casos de erro 5% restante para o acerto