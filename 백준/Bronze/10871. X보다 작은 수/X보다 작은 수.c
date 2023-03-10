#include <stdio.h>

int main(void)
{
	int N, X, A[10000];

    scanf("%d %d", &N, &X);
    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    for (int j = 0; j < N; j++)
    {
        if (A[j] < X)
            printf("%d ", A[j]);
    }
    
    return 0;
}