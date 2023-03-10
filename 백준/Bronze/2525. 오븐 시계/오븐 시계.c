#include <stdio.h>

int main(void)
{
    int A, B, C;

    scanf("%d %d", &A, &B);
    scanf("%d", &C);
    B += C % 60;
    if (59 < B)
    {
        A++;
        B -= 60;
    }
    A += C / 60;
    A = A % 24;
    printf("%d %d", A, B);
}