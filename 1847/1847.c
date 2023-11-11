#include <stdio.h>

int main() {
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);

    if (A > B && B <= C) {
        printf(":)\n");
    } else if (A < B && B >= C) {
        printf(":(\n");
    } else if (A < B && B < C && (B - A) > (C - B)) {
        printf(":(\n");
    } else if (A < B && B < C && (B - A) <= (C - B)) {
        printf(":)\n");
    } else if (A > B && B > C && (A - B) > (B - C)) {
        printf(":)\n");
    } else if (A > B && B > C && (A - B) <= (B - C)) {
        printf(":(\n");
    } else if (A == B && B < C) {
        printf(":)\n");
    } else {
        printf(":(\n");
    }

    return 0;
}