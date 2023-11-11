#include <stdio.h>

int main() {
    double salario, ir;

    scanf("%lf", &salario);

    if (salario <= 2000.00) {
        ir = 0.0;
    } else if (salario <= 3000.00) {
        ir = (salario - 2000.00) * 0.08;
    } else if (salario <= 4500.00) {
        ir = 1000.00 * 0.08 + (salario - 3000.00) * 0.18;
    } else {
        ir = 1000.00 * 0.08 + 1500.00 * 0.18 + (salario - 4500.00) * 0.28;
    }

    if (ir == 0.0) {
        printf("Isento\n");
    } else {
        printf("R$ %.2f\n", ir);
    }

    return 0;
}