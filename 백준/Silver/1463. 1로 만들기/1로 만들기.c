#include <stdio.h>
#include <stdlib.h>

int min(int x, int y)
{
    return x < y ? x : y;
}

int main(void)
{
    int N;

    scanf("%d", &N);
    
    int *X = (int *)malloc(sizeof(int) * (N + 1));
    X[1] = 0;
    X[2] = 1;
    X[3] = 1;
    for (int i = 4; i < N + 1; i++)
    {
        X[i] = X[i - 1] + 1;
        if (i % 2 == 0)
            X[i] = min(X[i / 2] + 1, X[i]);
        if (i % 3 == 0)
            X[i] = min(X[i / 3] + 1, X[i]);
    }
    printf("%d", X[N]);
    free(X);

    return 0;
}