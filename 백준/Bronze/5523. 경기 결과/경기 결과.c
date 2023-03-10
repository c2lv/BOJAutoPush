#include <stdio.h>

int main(void)
{
    int n;
    int a;
    int b;
    int i;
    int win[2] = { 0, };

    scanf("%d", &n);
    i = 0;
    while (i < n)
    {
        scanf("%d %d", &a, &b);
        if (b < a)
            win[0] += 1;
        if (a < b)
            win[1] += 1;
        i++;
    }
    printf("%d %d", win[0], win[1]);
        
    return (0);
}