#include <stdio.h>
#include <stdlib.h>

int main() {
    int hi, mi, hf, mf;
    
    scanf("%d %d %d %d", &hi, &mi, &hf, &mf);
    
    if (hi == mi && hf == mf) {
        printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)\n");
    } else if (hi > hf) {
        int calci = hi * 60 + mi;
        int calcf = (hf + 24) * 60 + mf;
        int result = calci - calcf;
        int time = abs(result) / 60;
        int minutos = abs(result) % 60;
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", abs(time), abs(minutos));
    } else if (hi == hf && mf < mi) {
        int calci = hi * 60 + mi;
        int calcf = (hf + 24) * 60 + mf;
        int result = calci - calcf;
        int time = abs(result) / 60;
        int minutos = abs(result) % 60;
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", abs(time), abs(minutos));
    } else {
        int calci = hi * 60 + mi;
        int calcf = hf * 60 + mf;
        int result = calci - calcf;
        int time = abs(result) / 60;
        int minutos = abs(result) % 60;
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", abs(time), abs(minutos));
    }
    
    return 0;
}