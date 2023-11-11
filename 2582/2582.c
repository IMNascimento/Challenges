#include <stdio.h>

int main() {
    // Dicionário que mapeia a soma dos botões para a música correspondente
    char *musicas[] = {
        "PROXYCITY",
        "P.Y.N.G.",
        "DNSUEY!",
        "SERVERS",
        "HOST!",
        "CRIPTONIZE",
        "OFFLINE DAY",
        "SALT",
        "ANSWER!",
        "RAR?",
        "WIFI ANTENNAS"
    };

    int C;
    scanf("%d", &C);

    for (int i = 0; i < C; i++) {
        int X, Y;
        scanf("%d %d", &X, &Y);
        int soma = X + Y;
        printf("%s\n", musicas[soma]);
    }

    return 0;
}