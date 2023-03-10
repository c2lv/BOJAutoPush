#include <stdio.h>

void swap(char *a, char *b)
{
    char temp;
    
    temp = *a;
    *a = *b;
    *b = temp;
}

int main(void)
{   
    char A[3], B[3];
    int revA = 0, revB = 0, repeat;

    scanf("%s %s", &A, &B);

    swap(&A[0], &A[2]);
    swap(&B[0], &B[2]);
    for (int i = 0; i < 3; i++)
    {
        revA *= 10;
        revA += A[i] - '0';
    }
    for (int j = 0; j < 3; j++)
    {
        revB *= 10;
        revB += B[j] - '0';
    }
    if (revA > revB)
        repeat = revA;
    else
        repeat = revB;
    printf("%d", repeat);

    return 0;
}