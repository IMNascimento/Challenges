valores = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

total = 0.0 
quantidade = int(input())

for _ in range(quantidade):
    codigo, quantidade = map(int, input().split())
    total += valores[codigo] * quantidade 

print(f'{total:.2f}')