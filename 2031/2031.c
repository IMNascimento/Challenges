#include <stdio.h>
#include <string.h>

int main() {
    char resultados[9][2][10] = {
        {"ataque", "pedra"},
        {"pedra", "ataque"},
        {"pedra", "papel"},
        {"papel", "pedra"},
        {"papel", "ataque"},
        {"ataque", "papel"},
        {"papel", "papel"},
        {"pedra", "pedra"},
        {"ataque", "ataque"}
    };

    char resultado_final[9][20] = {
        "Jogador 1 venceu",
        "Jogador 2 venceu",
        "Jogador 1 venceu",
        "Jogador 2 venceu",
        "Jogador 2 venceu",
        "Jogador 1 venceu",
        "Ambos venceram",
        "Sem ganhador",
        "Aniquilacao mutua"
    };

    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        char jogador1[10], jogador2[10];
        scanf("%s %s", jogador1, jogador2);

        int resultado_index = -1;
        for (int j = 0; j < 9; j++) {
            if (strcmp(jogador1, resultados[j][0]) == 0 && strcmp(jogador2, resultados[j][1]) == 0) {
                resultado_index = j;
                break;
            }
        }

        if (resultado_index != -1) {
            printf("%s\n", resultado_final[resultado_index]);
        } else {
            printf("Sem ganhador\n");
        }
    }

    return 0;
}