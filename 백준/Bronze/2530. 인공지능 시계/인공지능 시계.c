#include <stdio.h>

int main(void)
{
    int A, B, C, D;

    scanf("%d %d %d", &A, &B, &C);
    scanf("%d", &D);
    C += D % 60;
    if (59 < C)
    {
        B++;
        C -= 60;
    }
    B += D % 3600 / 60;
    if (59 < B)
    {
        A++;
        B -= 60;
    }
    A += D / 3600;
    A = A % 24;
    printf("%d %d %d", A, B, C);
}