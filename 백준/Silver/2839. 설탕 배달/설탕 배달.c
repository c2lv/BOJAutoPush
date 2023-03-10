#include <stdio.h>

int main(void)
{
    int N, a = 0, b = 0;

    scanf("%d", &N);
    if (N == 4 || N == 7)
    {
        printf("-1");
        return 0;
    }
    else if (N % 5 == 0)
        a = N / 5;
    else if (N % 3 == 0)
        b = N / 3;
    else if ((N - 5) % 3 == 0)
    {
        a = 1;
        b = (N - 5) / 3;
    }
    else // ((N - 10) % 3 == 0)
    {
        a = 2;
        b = (N - 10) / 3;
    }

    if (b >= 5)
    {
        a += b / 5 * 3;
        b -= b / 5 * 5;
    }
    printf("%d", a + b);
    
    return 0;
}