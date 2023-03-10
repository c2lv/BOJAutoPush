#include <stdio.h>

int main(void)
{
	int N, a, cl = 0;

    scanf("%d", &N);

    if (N < 10)
        N *= 10;
    a = N;

    while (1)
    {
        a = (a % 10 * 10) + ((a / 10 + a % 10) % 10);
        cl++;
        if (N == a)
            break;
    }

    printf("%d", cl);

    return 0;
}