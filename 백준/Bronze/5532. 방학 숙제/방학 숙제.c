#include <stdio.h>

int main(void)
{
    int L, A, B, C, D, a = 1, b = 1, sum;
    
    scanf("%d %d %d %d %d", &L, &A, &B, &C, &D);
    while (A > C * a)
        a++;
    while (B > D * b)
        b++;
    if (a > b)
        sum = a;
    else
        sum = b;
    printf("%d", L - sum);
    
    return 0;
}