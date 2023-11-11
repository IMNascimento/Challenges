notas = []
notas_validas = 0

while notas_validas < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        notas_validas += 1
    else:
        print("nota invalida")

media = sum(notas) / 2
print(f"media = {media:.2f}")