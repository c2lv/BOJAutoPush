#include <stdio.h>
#include <stdlib.h>

int ft_sum_123(int n)
{
    int ret, *sum_123 = (int *)malloc(sizeof(int) * (n + 1));

    sum_123[1] = 1;
    sum_123[2] = 2;
    sum_123[3] = 4;
    for (int i = 4; i < n + 1; i++)
        sum_123[i] = sum_123[i - 3] + sum_123[i - 2] + sum_123[i - 1];
    ret = sum_123[n];
    free(sum_123);

    return ret;
    /* 재귀함수로 만들어 똑같은 기능을 하지만 느림
    if (n == 1)
        return 1;
    else if (n == 2)
        return 2;
    else if (n == 3)
        return 4;
    else if (n > 3)
        return ft_sum_123(n - 3) + ft_sum_123(n - 2) + ft_sum_123(n - 1);
    */
}

int main(void)
{
    int T, n;

    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%d", &n);
        printf("%d\n", ft_sum_123(n));
    }

    return 0;
}