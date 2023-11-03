metros = int(input())
pistas = []
toques = 0
pista_atual = 1
for x in range(metros):
    e, m, d = map(int, input().split())
    pistas.append([int(e),int(m), int(d)])

for i in range(metros):
    if pistas[i][pista_atual] == 1:
        # Papai Noel precisa mudar de pista, escolhendo a que está livre
        if pistas[i][(pista_atual + 1) % 3] == 0:
            pista_atual = (pista_atual + 1) % 3
        else:
            pista_atual = (pista_atual + 2) % 3
        toques += 1

print(toques)
#incompleto não rodou a logica