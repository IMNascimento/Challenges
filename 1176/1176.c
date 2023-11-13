#include <stdio.h>

int main() {
    long long int fibonacci[62];
    fibonacci[0] = 0;
    fibonacci[1] = 1;

    for (int i = 2; i < 62; i++) {
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }

    int teste;
    scanf("%d", &teste);

    for (int j = 1; j <= teste; j++) {
        int n;
        scanf("%d", &n);
        printf("Fib(%d) = %lld\n", n, fibonacci[n]);
    }

    return 0;
}