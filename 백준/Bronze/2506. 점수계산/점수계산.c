#include <stdio.h>

int main(void)
{
    int N, p[100], sum = 0, K = 1;

    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &p[i]);
        if (p[i] == 1)
        {
            sum += K;
            K++;
        }
        else // (p[i] == 0)
            K = 1;
    }
    printf("%d", sum);

    return 0;
}