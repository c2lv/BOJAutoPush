#include <stdio.h>

int main(void)
{
    int N;

    scanf("%d", &N);
    for (int i = 0; i < 2 * N - 1; i++)
    {
        if (i < N)
        {
            for (int j = i; j < N - 1; j++)
                printf(" ");
            for (int k = 0; k < 2 * i + 1; k++)
                printf("*");
        }
        else
        {
            for (int l = 0; l < i - N + 1; l++)
                printf(" ");
            for (int m = 0; m < 4 * N - 2 * i - 3; m++)
                printf("*");
        }
        printf("\n");
    }
    return 0;
}