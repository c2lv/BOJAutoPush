#include <stdio.h>
#include <math.h>

int main(void)
{
    int A, B, C, num[10], len = 0, c, n, sum;
    
    scanf("%d %d %d", &A, &B, &C);
    sum = A * B * C;
    for (int i = 0; i < 10; i++)
        num[i] = 0;
    c = sum;
    while (c)
    {
        c /= 10;
        len++;
    }
    for (int j = len; j > 0; j--)
    {
        n = sum / pow(10, j - 1);
        num[n]++;
        sum = sum % (int)pow(10, j - 1);
    }
    for (int k = 0; k < 10; k++)
        printf("%d\n", num[k]);
    
    return 0;
}