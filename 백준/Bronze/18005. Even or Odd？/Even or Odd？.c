#include <stdio.h>

int main(void)
{
    int n;

    scanf("%d", &n);
    if (n % 4 == 2)
        printf("1");
    else if (n % 4 == 0)
        printf("2");
    else
        printf("0");
    return 0;
}