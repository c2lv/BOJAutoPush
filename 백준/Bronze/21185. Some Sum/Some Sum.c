#include <stdio.h>

int main(void)
{
    int n;

    scanf("%d", &n);
    if (n % 4 == 2)
        printf("Odd");
    else if (n % 4 == 0)
        printf("Even");
    else
        printf("Either");
    return 0;
}