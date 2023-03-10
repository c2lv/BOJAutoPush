#include <stdio.h>

int main(void)
{
    int n, car[5], cnt = 0;

    scanf("%d", &n);
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &car[i]);
        if (car[i] == n)
            cnt++;
    }
    printf("%d", cnt);

    return 0;
}