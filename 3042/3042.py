while True:
    metros = int(input())
    if metros == 0 or metros == None or not metros:
        break

    pistas = []
    toques = 0
    pista_atual = 1
    for x in range(metros):
        e, m, d = map(int, input().split())
        pistas.append([int(e),int(m), int(d)])

    for i in pistas:
        if i[0] == 0 and i[1] == 1 and i[2] == 1:
            calculo = 0 - pista_atual
            pista_atual = 0
            toques += abs(calculo)
        elif i[0] == 1 and i[1] == 1 and i[2] == 0:
            calculo = 2 - pista_atual
            pista_atual = 2
            toques += abs(calculo)
        elif i[0] == 1 and i[1] == 0 and i[2] == 1:
            calculo = 1 - pista_atual
            pista_atual = 1
            toques += abs(calculo)
        else:
            pass
    print(toques)