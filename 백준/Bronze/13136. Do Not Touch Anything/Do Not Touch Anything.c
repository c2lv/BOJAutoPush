#include <stdio.h>

int main(void)
{
    unsigned long long R, C, N, a = 1, b = 1;

    scanf("%llu %llu %llu", &R, &C, &N);

    while (a * N < R)
        a++;
    while (b * N < C)
        b++;
    printf("%llu", a * b);
    return 0;
}