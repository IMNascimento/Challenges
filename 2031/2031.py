resultados = {
    ('ataque', 'pedra'): 'Jogador 1 venceu',
    ('pedra','ataque'): 'Jogador 2 venceu',
    ('pedra', 'papel'): 'Jogador 1 venceu',
    ('papel', 'pedra'): 'Jogador 2 venceu',
    ('papel', 'ataque'): 'Jogador 2 venceu',
    ('ataque','papel'): 'Jogador 1 venceu',
    ('papel', 'papel'): 'Ambos venceram',
    ('pedra', 'pedra'): 'Sem ganhador',
    ('ataque', 'ataque'): 'Aniquilacao mutua',
}

N = int(input())  

for _ in range(N):
    jogador1 = input() 
    jogador2 = input()  

    resultado = resultados.get((jogador1, jogador2), 'Sem ganhador')

    print(resultado)